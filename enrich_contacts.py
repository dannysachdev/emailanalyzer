#!/usr/bin/env python3
"""
Contact Enrichment - Enriches contact information with additional data
"""

import json
import csv
import re
from collections import defaultdict


class ContactEnricher:
    def __init__(self, contacts_file='extracted_contacts.json'):
        self.contacts_file = contacts_file
        self.contacts = []
        self.enriched_contacts = []
        
        # Load contacts
        with open(contacts_file, 'r', encoding='utf-8') as f:
            self.contacts = json.load(f)
    
    def extract_domain_info(self, email):
        """Extract domain and company info from email"""
        if not email or '@' not in email:
            return None
        
        domain = email.split('@')[1].lower()
        
        # Common free email providers
        free_providers = {
            'gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 
            'aol.com', 'icloud.com', 'protonmail.com', 'mail.com',
            'yandex.com', 'zoho.com', 'gmx.com', 'inbox.com'
        }
        
        is_free_email = domain in free_providers
        
        # Extract company from domain
        company_from_domain = ''
        if not is_free_email:
            # Remove common TLDs and subdomains
            parts = domain.split('.')
            if len(parts) >= 2:
                # Get main domain name (before TLD)
                company_from_domain = parts[-2]
                # Capitalize first letter
                company_from_domain = company_from_domain.capitalize()
        
        return {
            'domain': domain,
            'is_free_email': is_free_email,
            'company_from_domain': company_from_domain
        }
    
    def infer_name_from_email(self, email):
        """Try to infer name from email address"""
        if not email or '@' not in email:
            return None
        
        local_part = email.split('@')[0].lower()
        
        # Skip if it looks like a generic address
        generic_patterns = [
            'info', 'admin', 'support', 'contact', 'sales', 'marketing',
            'noreply', 'no-reply', 'donotreply', 'postmaster', 'webmaster',
            'help', 'service', 'team', 'group'
        ]
        
        if any(pattern in local_part for pattern in generic_patterns):
            return None
        
        # Try to parse name patterns
        # firstname.lastname@domain.com
        if '.' in local_part:
            parts = local_part.split('.')
            if len(parts) == 2 and all(len(p) > 1 for p in parts):
                first_name = parts[0].capitalize()
                last_name = parts[1].capitalize()
                return f"{first_name} {last_name}"
        
        # firstname_lastname@domain.com
        if '_' in local_part:
            parts = local_part.split('_')
            if len(parts) == 2 and all(len(p) > 1 for p in parts):
                first_name = parts[0].capitalize()
                last_name = parts[1].capitalize()
                return f"{first_name} {last_name}"
        
        # firstnamelastname@domain.com (if reasonable length)
        if 4 <= len(local_part) <= 20 and local_part.isalpha():
            return local_part.capitalize()
        
        return None
    
    def extract_linkedin_potential(self, contact):
        """Create LinkedIn search hints"""
        linkedin_search = []
        
        if contact.get('enriched_name'):
            linkedin_search.append(contact['enriched_name'])
        
        if contact.get('company_enriched'):
            linkedin_search.append(contact['company_enriched'])
        
        return ' '.join(linkedin_search) if linkedin_search else ''
    
    def categorize_response_type(self, contact):
        """Categorize what type of response this was"""
        category = contact.get('category', '').lower()
        subject = contact.get('original_subject', '').lower()
        
        if category == 'out_of_office':
            if 'maternity' in subject or 'parental' in subject:
                return 'Out of Office - Parental Leave'
            elif 'vacation' in subject:
                return 'Out of Office - Vacation'
            else:
                return 'Out of Office - General'
        elif category == 'replies':
            if 'interested' in subject or 'meeting' in subject or 'call' in subject:
                return 'Reply - Interested'
            else:
                return 'Reply - General'
        elif category == 'automatic_replies':
            return 'Auto-Reply'
        elif category == 'contact_info':
            return 'Contact Info Update'
        else:
            return 'Other'
    
    def calculate_lead_score(self, contact):
        """Calculate a simple lead score based on available information"""
        score = 0
        
        # Base score for being a response
        score += 10
        
        # Higher score for actual replies vs auto-responses
        if contact.get('response_type', '').startswith('Reply'):
            score += 30
        elif contact.get('response_type', '').startswith('Out of Office'):
            score += 20
        
        # Bonus for having rich information
        if contact.get('phones'):
            score += 15
        
        if contact.get('enriched_name'):
            score += 10
        
        if contact.get('title'):
            score += 15
        
        if contact.get('company_enriched'):
            score += 10
        
        # Bonus for corporate email (not free email)
        if not contact.get('is_free_email', False):
            score += 20
        
        return score
    
    def enrich_all_contacts(self):
        """Enrich all contacts with additional information"""
        print(f"Enriching {len(self.contacts)} contacts...")
        
        for idx, contact in enumerate(self.contacts, 1):
            if idx % 100 == 0:
                print(f"Progress: {idx}/{len(self.contacts)} contacts enriched...")
            
            enriched = contact.copy()
            
            # Get primary email
            primary_email = contact['emails'][0] if contact['emails'] else None
            
            if primary_email:
                # Extract domain info
                domain_info = self.extract_domain_info(primary_email)
                if domain_info:
                    enriched['domain'] = domain_info['domain']
                    enriched['is_free_email'] = domain_info['is_free_email']
                    enriched['company_from_domain'] = domain_info['company_from_domain']
                
                # Infer name if not available
                if not contact['names']:
                    inferred_name = self.infer_name_from_email(primary_email)
                    if inferred_name:
                        enriched['inferred_name'] = inferred_name
            
            # Consolidate best name
            if contact['names']:
                # Use the longest name (likely most complete)
                enriched['enriched_name'] = max(contact['names'], key=len)
            elif enriched.get('inferred_name'):
                enriched['enriched_name'] = enriched['inferred_name']
            else:
                enriched['enriched_name'] = ''
            
            # Consolidate best company
            if contact['company']:
                enriched['company_enriched'] = contact['company']
            elif enriched.get('company_from_domain'):
                enriched['company_enriched'] = enriched['company_from_domain']
            else:
                enriched['company_enriched'] = ''
            
            # Add LinkedIn search string
            enriched['linkedin_search'] = self.extract_linkedin_potential(enriched)
            
            # Categorize response type
            enriched['response_type'] = self.categorize_response_type(contact)
            
            # Calculate lead score
            enriched['lead_score'] = self.calculate_lead_score(enriched)
            
            # Format phone numbers
            if contact['phones']:
                enriched['primary_phone'] = contact['phones'][0]
            else:
                enriched['primary_phone'] = ''
            
            self.enriched_contacts.append(enriched)
        
        print(f"\n✓ Enriched {len(self.enriched_contacts)} contacts")
    
    def generate_statistics(self):
        """Generate enrichment statistics"""
        stats = {
            'total_contacts': len(self.enriched_contacts),
            'with_corporate_email': 0,
            'with_phone': 0,
            'with_name': 0,
            'with_title': 0,
            'with_company': 0,
            'high_quality_leads': 0,  # Score >= 70
            'medium_quality_leads': 0,  # Score 50-69
            'low_quality_leads': 0,  # Score < 50
            'response_types': defaultdict(int),
            'top_domains': defaultdict(int),
            'top_companies': defaultdict(int),
        }
        
        for contact in self.enriched_contacts:
            if not contact.get('is_free_email', False):
                stats['with_corporate_email'] += 1
            
            if contact.get('primary_phone'):
                stats['with_phone'] += 1
            
            if contact.get('enriched_name'):
                stats['with_name'] += 1
            
            if contact.get('title'):
                stats['with_title'] += 1
            
            if contact.get('company_enriched'):
                stats['with_company'] += 1
            
            # Lead quality
            score = contact.get('lead_score', 0)
            if score >= 70:
                stats['high_quality_leads'] += 1
            elif score >= 50:
                stats['medium_quality_leads'] += 1
            else:
                stats['low_quality_leads'] += 1
            
            # Response type
            resp_type = contact.get('response_type', 'Unknown')
            stats['response_types'][resp_type] += 1
            
            # Domain
            domain = contact.get('domain', '')
            if domain:
                stats['top_domains'][domain] += 1
            
            # Company
            company = contact.get('company_enriched', '')
            if company:
                stats['top_companies'][company] += 1
        
        return stats
    
    def print_summary(self):
        """Print enrichment summary"""
        stats = self.generate_statistics()
        
        print("\n" + "=" * 80)
        print("CONTACT ENRICHMENT SUMMARY")
        print("=" * 80)
        
        print(f"\nTotal enriched contacts: {stats['total_contacts']}")
        
        print("\nData Completeness:")
        total = stats['total_contacts']
        print(f"  Corporate email addresses: {stats['with_corporate_email']:5d} ({stats['with_corporate_email']/total*100:.1f}%)")
        print(f"  With phone numbers       : {stats['with_phone']:5d} ({stats['with_phone']/total*100:.1f}%)")
        print(f"  With names               : {stats['with_name']:5d} ({stats['with_name']/total*100:.1f}%)")
        print(f"  With job titles          : {stats['with_title']:5d} ({stats['with_title']/total*100:.1f}%)")
        print(f"  With company names       : {stats['with_company']:5d} ({stats['with_company']/total*100:.1f}%)")
        
        print("\nLead Quality Distribution:")
        print(f"  High Quality (70+)       : {stats['high_quality_leads']:5d} ({stats['high_quality_leads']/total*100:.1f}%)")
        print(f"  Medium Quality (50-69)   : {stats['medium_quality_leads']:5d} ({stats['medium_quality_leads']/total*100:.1f}%)")
        print(f"  Lower Quality (<50)      : {stats['low_quality_leads']:5d} ({stats['low_quality_leads']/total*100:.1f}%)")
        
        print("\nResponse Types:")
        for resp_type, count in sorted(stats['response_types'].items(), key=lambda x: x[1], reverse=True):
            print(f"  {resp_type:30s}: {count:5d}")
        
        print("\nTop 10 Domains:")
        for domain, count in sorted(stats['top_domains'].items(), key=lambda x: x[1], reverse=True)[:10]:
            print(f"  {domain:40s}: {count:5d}")
        
        print("\nTop 10 Companies:")
        for company, count in sorted(stats['top_companies'].items(), key=lambda x: x[1], reverse=True)[:10]:
            print(f"  {company:40s}: {count:5d}")
        
        print("=" * 80)
    
    def save_to_csv(self, output_file='enriched_contacts.csv'):
        """Save enriched contacts to CSV"""
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                'Lead Score',
                'Name',
                'Primary Email',
                'All Emails',
                'Primary Phone',
                'All Phones',
                'Job Title',
                'Company',
                'Domain',
                'Is Free Email',
                'Response Type',
                'LinkedIn Search',
                'Category',
                'Original Subject',
                'Date',
                'To',
                'Body'
            ])
            
            # Sort by lead score (highest first)
            sorted_contacts = sorted(self.enriched_contacts, 
                                   key=lambda x: x.get('lead_score', 0), 
                                   reverse=True)
            
            for contact in sorted_contacts:
                writer.writerow([
                    contact.get('lead_score', 0),
                    contact.get('enriched_name', ''),
                    contact['emails'][0] if contact['emails'] else '',
                    '; '.join(contact['emails']),
                    contact.get('primary_phone', ''),
                    '; '.join(contact['phones']),
                    contact.get('title', ''),
                    contact.get('company_enriched', ''),
                    contact.get('domain', ''),
                    'Yes' if contact.get('is_free_email', False) else 'No',
                    contact.get('response_type', ''),
                    contact.get('linkedin_search', ''),
                    contact.get('category', ''),
                    contact.get('original_subject', ''),
                    contact.get('date', ''),
                    contact.get('to', ''),
                    contact.get('body', '')
                ])
        
        print(f"✓ Saved enriched contacts to: {output_file}")
    
    def save_to_json(self, output_file='enriched_contacts.json'):
        """Save enriched contacts to JSON"""
        # Sort by lead score
        sorted_contacts = sorted(self.enriched_contacts, 
                               key=lambda x: x.get('lead_score', 0), 
                               reverse=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(sorted_contacts, f, indent=2, ensure_ascii=False)
        
        print(f"✓ Saved enriched contacts to: {output_file}")
    
    def export_high_quality_leads(self, output_file='high_quality_leads.csv', min_score=70):
        """Export only high quality leads"""
        high_quality = [c for c in self.enriched_contacts if c.get('lead_score', 0) >= min_score]
        
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                'Lead Score',
                'Name',
                'Email',
                'Phone',
                'Job Title',
                'Company',
                'LinkedIn Search',
                'Response Type',
                'To',
                'Body'
            ])
            
            for contact in sorted(high_quality, key=lambda x: x.get('lead_score', 0), reverse=True):
                writer.writerow([
                    contact.get('lead_score', 0),
                    contact.get('enriched_name', ''),
                    contact['emails'][0] if contact['emails'] else '',
                    contact.get('primary_phone', ''),
                    contact.get('title', ''),
                    contact.get('company_enriched', ''),
                    contact.get('linkedin_search', ''),
                    contact.get('response_type', ''),
                    contact.get('to', ''),
                    contact.get('body', '')
                ])
        
        print(f"✓ Exported {len(high_quality)} high quality leads to: {output_file}")


def main():
    import os
    
    if not os.path.exists('extracted_contacts.json'):
        print("Error: extracted_contacts.json not found!")
        print("Please run extract_contact_info.py first.")
        return
    
    print("Starting contact enrichment...")
    
    # Create enricher
    enricher = ContactEnricher('extracted_contacts.json')
    
    # Enrich all contacts
    enricher.enrich_all_contacts()
    
    # Print summary
    enricher.print_summary()
    
    # Save outputs
    print("\nSaving results...")
    enricher.save_to_csv('enriched_contacts.csv')
    enricher.save_to_json('enriched_contacts.json')
    enricher.export_high_quality_leads('high_quality_leads.csv', min_score=70)
    
    print("\n✓ Contact enrichment complete!")
    print("  - Full database: enriched_contacts.csv / enriched_contacts.json")
    print("  - High quality leads: high_quality_leads.csv")


if __name__ == '__main__':
    main()
