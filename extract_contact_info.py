#!/usr/bin/env python3
"""
Contact Information Extractor - Extracts contact details from categorized emails
"""

import os
import re
import email
from email import policy
from email.utils import parseaddr, getaddresses
from pathlib import Path
import json
import csv


class ContactInfoExtractor:
    def __init__(self, emails_dir, categories_file='categories.json'):
        self.emails_dir = Path(emails_dir)
        self.categories_file = categories_file
        self.contacts = []
        
        # Load categorized emails
        with open(categories_file, 'r') as f:
            self.categories = json.load(f)
    
    def parse_email(self, filepath):
        """Parse an email file and return email object"""
        try:
            with open(filepath, 'rb') as f:
                msg = email.message_from_binary_file(f, policy=policy.default)
            return msg
        except Exception as e:
            print(f"Error parsing {filepath}: {e}")
            return None
    
    def extract_phone_numbers(self, text):
        """Extract phone numbers from text"""
        if not text:
            return []
        
        # Various phone number patterns
        patterns = [
            r'\+?1?\s*\(?(\d{3})\)?[\s.-]?(\d{3})[\s.-]?(\d{4})',  # US/Canada
            r'\+\d{1,3}\s*\d{1,14}',  # International
            r'\d{3}[-.\s]?\d{3}[-.\s]?\d{4}',  # Standard
        ]
        
        phones = []
        for pattern in patterns:
            matches = re.findall(pattern, text)
            for match in matches:
                if isinstance(match, tuple):
                    phone = ''.join(match)
                else:
                    phone = match
                # Clean up
                phone = re.sub(r'[^\d+]', '', phone)
                if len(phone) >= 10:
                    phones.append(phone)
        
        return list(set(phones))
    
    def extract_alternate_emails(self, text):
        """Extract additional email addresses from text"""
        if not text:
            return []
        
        # Email pattern
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        emails = re.findall(email_pattern, text)
        
        # Filter out common system emails
        system_emails = ['noreply', 'no-reply', 'mailer-daemon', 'postmaster', 
                        'donotreply', 'do-not-reply', 'bounce', 'notification']
        
        filtered_emails = []
        for e in emails:
            if not any(sys in e.lower() for sys in system_emails):
                filtered_emails.append(e.lower())
        
        return list(set(filtered_emails))
    
    def extract_signature_info(self, text):
        """Extract name, title, company from email signature"""
        if not text:
            return {}
        
        info = {}
        
        # Look for common signature patterns
        lines = text.split('\n')
        
        # Title patterns
        title_keywords = [
            r'\b(CEO|CTO|CFO|COO|CMO|VP|Director|Manager|Lead|Head|Chief|President|Senior|Junior|Specialist|Engineer|Developer|Analyst|Coordinator|Administrator)\b',
        ]
        
        # Company patterns (often after "at", "@", or on separate line)
        company_pattern = r'(?:at|@)\s+([A-Z][A-Za-z0-9\s&.,]+(?:Inc|LLC|Ltd|Corp|Co|Company)?)'
        
        for line in lines[:15]:  # Check first 15 lines for signature
            line = line.strip()
            if not line or len(line) > 100:
                continue
            
            # Look for title
            for pattern in title_keywords:
                if re.search(pattern, line, re.IGNORECASE):
                    info['title'] = line
                    break
            
            # Look for company
            company_match = re.search(company_pattern, line)
            if company_match:
                info['company'] = company_match.group(1).strip()
        
        return info
    
    def extract_contact_from_email(self, filepath, category):
        """Extract all contact information from a single email"""
        msg = self.parse_email(filepath)
        if not msg:
            return None
        
        contact = {
            'category': category,
            'filename': str(filepath.name),
            'emails': [],
            'phones': [],
            'names': [],
            'title': '',
            'company': '',
            'original_subject': '',
            'date': '',
            'to': '',
            'body': '',
        }
        
        # Get basic info from headers
        contact['original_subject'] = msg.get('Subject', '')
        contact['date'] = msg.get('Date', '')
        contact['to'] = msg.get('To', '')
        
        # Extract from From header
        from_header = msg.get('From', '')
        from_name, from_email = parseaddr(from_header)
        
        if from_email and '@' in from_email:
            contact['emails'].append(from_email.lower())
        
        if from_name and from_name != from_email:
            # Clean up name
            from_name = re.sub(r'["\']', '', from_name)
            from_name = re.sub(r'\s+', ' ', from_name).strip()
            if from_name and len(from_name) > 2:
                contact['names'].append(from_name)
        
        # Extract Reply-To if different
        reply_to = msg.get('Reply-To', '')
        if reply_to:
            reply_name, reply_email = parseaddr(reply_to)
            if reply_email and reply_email.lower() != from_email.lower():
                contact['emails'].append(reply_email.lower())
            if reply_name and reply_name != reply_email and reply_name != from_name:
                reply_name = re.sub(r'["\']', '', reply_name)
                reply_name = re.sub(r'\s+', ' ', reply_name).strip()
                if reply_name and len(reply_name) > 2:
                    contact['names'].append(reply_name)
        
        # Get email body
        body = ''
        try:
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == 'text/plain':
                        body = part.get_payload(decode=True).decode('utf-8', errors='ignore')
                        break
            else:
                body = msg.get_payload(decode=True).decode('utf-8', errors='ignore')
        except:
            pass
        
        if body:
            # Store the body (limit to first 2000 chars for CSV compatibility)
            contact['body'] = body[:2000].replace('\n', ' ').replace('\r', ' ').strip()
            
            # Extract phones
            phones = self.extract_phone_numbers(body)
            contact['phones'].extend(phones)
            
            # Extract alternate emails
            alt_emails = self.extract_alternate_emails(body)
            for e in alt_emails:
                if e not in contact['emails']:
                    contact['emails'].append(e)
            
            # Extract signature info
            sig_info = self.extract_signature_info(body)
            if 'title' in sig_info:
                contact['title'] = sig_info['title']
            if 'company' in sig_info:
                contact['company'] = sig_info['company']
        
        # Remove duplicates
        contact['emails'] = list(set(contact['emails']))
        contact['phones'] = list(set(contact['phones']))
        contact['names'] = list(set(contact['names']))
        
        # Only return if we have useful info
        if contact['emails'] or contact['phones'] or contact['names']:
            return contact
        
        return None
    
    def extract_from_categories(self, target_categories=None):
        """Extract contacts from specific categories"""
        if target_categories is None:
            # Default: categories that likely have useful contact info
            target_categories = [
                'replies',
                'out_of_office',
                'automatic_replies',
                'contact_info',
            ]
        
        print(f"Extracting contact information from categories: {', '.join(target_categories)}")
        
        total_emails = 0
        for category in target_categories:
            if category in self.categories:
                total_emails += len(self.categories[category])
        
        print(f"Processing {total_emails} emails...")
        
        processed = 0
        for category in target_categories:
            if category not in self.categories:
                continue
            
            email_files = self.categories[category]
            for email_file in email_files:
                processed += 1
                if processed % 100 == 0:
                    print(f"Progress: {processed}/{total_emails} emails processed...")
                
                filepath = self.emails_dir / email_file
                if not filepath.exists():
                    continue
                
                contact = self.extract_contact_from_email(filepath, category)
                if contact:
                    self.contacts.append(contact)
        
        print(f"\n✓ Extracted information from {len(self.contacts)} emails")
        return self.contacts
    
    def deduplicate_contacts(self):
        """Merge contacts with same email address"""
        email_to_contact = {}
        
        for contact in self.contacts:
            primary_email = contact['emails'][0] if contact['emails'] else None
            
            if not primary_email:
                continue
            
            if primary_email in email_to_contact:
                # Merge with existing
                existing = email_to_contact[primary_email]
                
                # Merge emails
                for e in contact['emails']:
                    if e not in existing['emails']:
                        existing['emails'].append(e)
                
                # Merge phones
                for p in contact['phones']:
                    if p not in existing['phones']:
                        existing['phones'].append(p)
                
                # Merge names
                for n in contact['names']:
                    if n not in existing['names']:
                        existing['names'].append(n)
                
                # Keep non-empty title and company
                if not existing['title'] and contact['title']:
                    existing['title'] = contact['title']
                if not existing['company'] and contact['company']:
                    existing['company'] = contact['company']
            else:
                email_to_contact[primary_email] = contact
        
        self.contacts = list(email_to_contact.values())
        print(f"After deduplication: {len(self.contacts)} unique contacts")
    
    def save_to_csv(self, output_file='extracted_contacts.csv'):
        """Save contacts to CSV file"""
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                'Primary Email',
                'All Emails',
                'Name(s)',
                'Phone(s)',
                'Title',
                'Company',
                'Category',
                'Original Subject',
                'Date',
                'To',
                'Body'
            ])
            
            for contact in self.contacts:
                writer.writerow([
                    contact['emails'][0] if contact['emails'] else '',
                    '; '.join(contact['emails']),
                    '; '.join(contact['names']),
                    '; '.join(contact['phones']),
                    contact['title'],
                    contact['company'],
                    contact['category'],
                    contact['original_subject'],
                    contact['date'],
                    contact['to'],
                    contact['body']
                ])
        
        print(f"✓ Saved contacts to: {output_file}")
    
    def save_to_json(self, output_file='extracted_contacts.json'):
        """Save contacts to JSON file"""
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(self.contacts, f, indent=2, ensure_ascii=False)
        
        print(f"✓ Saved contacts to: {output_file}")
    
    def print_summary(self):
        """Print summary statistics"""
        print("\n" + "=" * 80)
        print("CONTACT EXTRACTION SUMMARY")
        print("=" * 80)
        
        print(f"\nTotal unique contacts: {len(self.contacts)}")
        
        # Count by category
        category_counts = {}
        for contact in self.contacts:
            cat = contact['category']
            category_counts[cat] = category_counts.get(cat, 0) + 1
        
        print("\nContacts by category:")
        for cat, count in sorted(category_counts.items(), key=lambda x: x[1], reverse=True):
            print(f"  {cat:20s}: {count:5d}")
        
        # Count fields
        with_phones = sum(1 for c in self.contacts if c['phones'])
        with_names = sum(1 for c in self.contacts if c['names'])
        with_title = sum(1 for c in self.contacts if c['title'])
        with_company = sum(1 for c in self.contacts if c['company'])
        
        print("\nField availability:")
        print(f"  With phone numbers  : {with_phones:5d} ({with_phones/len(self.contacts)*100:.1f}%)")
        print(f"  With names          : {with_names:5d} ({with_names/len(self.contacts)*100:.1f}%)")
        print(f"  With title          : {with_title:5d} ({with_title/len(self.contacts)*100:.1f}%)")
        print(f"  With company        : {with_company:5d} ({with_company/len(self.contacts)*100:.1f}%)")
        
        print("=" * 80)


def main():
    # Path to the emails directory
    emails_dir = './relpies1114'
    
    if not os.path.exists(emails_dir):
        print(f"Error: Directory '{emails_dir}' not found!")
        print("Please run analyze_emails.py first to categorize the emails.")
        return
    
    if not os.path.exists('categories.json'):
        print("Error: categories.json not found!")
        print("Please run analyze_emails.py first to categorize the emails.")
        return
    
    # Create extractor
    extractor = ContactInfoExtractor(emails_dir)
    
    # Extract from relevant categories
    print("Starting contact information extraction...")
    print("Targeting: replies, out_of_office, automatic_replies, and contact_info categories")
    print()
    
    extractor.extract_from_categories([
        'replies',
        'out_of_office',
        'automatic_replies',
        'contact_info',
    ])
    
    # Deduplicate
    print("\nDeduplicating contacts...")
    extractor.deduplicate_contacts()
    
    # Print summary
    extractor.print_summary()
    
    # Save outputs
    print("\nSaving results...")
    extractor.save_to_csv('extracted_contacts.csv')
    extractor.save_to_json('extracted_contacts.json')
    
    print("\n✓ Contact extraction complete!")
    print("  - CSV format: extracted_contacts.csv")
    print("  - JSON format: extracted_contacts.json")


if __name__ == '__main__':
    main()
