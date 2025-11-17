#!/usr/bin/env python3
"""
Email Analyzer - Categorizes emails from relpies1114 directory into different types
"""

import os
import re
import email
from email import policy
from collections import defaultdict
from pathlib import Path
import json
import csv


class EmailAnalyzer:
    def __init__(self, emails_dir):
        self.emails_dir = Path(emails_dir)
        self.categories = {
            'bounces': [],
            'replies': [],
            'out_of_office': [],
            'contact_info': [],
            'automatic_replies': [],
            'verification_requests': [],
            'action_required': [],
            'delivery_delays': [],
            'unsubscribe': [],
            'spam_filters': [],
            'security_alerts': [],
            'other': []
        }
        
    def parse_email(self, filepath):
        """Parse an email file and return email object"""
        try:
            with open(filepath, 'rb') as f:
                msg = email.message_from_binary_file(f, policy=policy.default)
            return msg
        except Exception as e:
            print(f"Error parsing {filepath}: {e}")
            return None
    
    def categorize_email(self, filepath, msg):
        """Categorize email based on headers and content"""
        if msg is None:
            return 'other'
        
        filename = filepath.name
        subject = msg.get('Subject', '').lower()
        from_addr = msg.get('From', '').lower()
        auto_submitted = msg.get('Auto-Submitted', '').lower()
        x_auto_response = msg.get('X-Auto-Response-Suppress', '').lower()
        
        # Get email body for content analysis
        body = ''
        try:
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == 'text/plain':
                        body = part.get_payload(decode=True).decode('utf-8', errors='ignore').lower()
                        break
            else:
                body = msg.get_payload(decode=True).decode('utf-8', errors='ignore').lower()
        except:
            body = ''
        
        # Check for bounces (expanded patterns)
        bounce_patterns_subject = [
            'mailer-daemon',
            'delivery failure',
            'delivery status notification',
            'undeliverable',
            'returned mail',
            'mail delivery failed',
            'bounce',
            'message was not delivered',
            "message couldn't be delivered",
            "your message couldn't be delivered",
            'undelivered mail',
            'invalid email address',
            'your email to',
            'mail not delivered',
            'message not delivered',
            'failed',
            'delivery notification',
            'blocked sender',
            'spam detection',
            'incumplimiento de política',  # Spanish: policy violation
            'no longer employed',
            'is no longer with',
            'deprecated domain',
        ]
        
        bounce_patterns_body = [
            'hop count exceeded',
            'user unknown',
            'mailbox unavailable',
            'recipient address rejected',
            'delivery has failed',
            'delivery has been delayed',
            'permanently failed',
            'recipient not found',
        ]
        
        if (
            any(pattern in subject for pattern in bounce_patterns_subject) or
            any(pattern in from_addr for pattern in ['mailer-daemon', 'postmaster', 'no-reply', 'noreply']) and 
            any(keyword in subject for keyword in ['delivery', 'failed', 'undeliv', 'bounce', 'message']) or
            any(pattern in body[:1000] for pattern in bounce_patterns_body)
        ):
            return 'bounces'
        
        # Check for delivery delays (not failures)
        if 'delivery status notification (delay)' in subject:
            return 'delivery_delays'
        
        # Check for out of office
        if (
            'out of office' in subject or
            'out of the office' in subject or
            'ooo' in subject or
            'maternity leave' in subject or
            'parental leave' in subject or
            ('automatic reply' in subject and ('vacation' in body or 'away' in body or 'office' in body)) or
            'away from office' in body[:500] or
            'currently out of office' in body[:500] or
            'will be out of the office' in body[:500]
        ):
            return 'out_of_office'
        
        # Check for automatic replies
        if (
            'automatic reply' in subject or
            'autoresponse' in subject or
            'auto-reply' in subject or
            auto_submitted == 'auto-replied' or
            'x-autoresponder' in str(msg).lower()[:1000]
        ):
            return 'automatic_replies'
        
        # Check for contact info updates
        if (
            'new contact' in subject or
            'updated contact' in subject or
            'contact information' in subject or
            'email address change' in subject or
            'new email address' in subject or
            'contact details' in subject
        ):
            return 'contact_info'
        
        # Check for verification/validation emails
        if (
            'verification' in subject or
            'verify your email' in subject or
            'confirm your email' in subject or
            'email verification' in subject or
            'validate' in subject
        ):
            return 'verification_requests'
        
        # Check for action required emails
        if (
            'action required' in subject or
            'action needed' in subject or
            'urgent' in subject
        ):
            return 'action_required'
        
        # Check for unsubscribe confirmations
        if (
            'unsubscribe' in subject or
            'subscription' in subject and 'remove' in body or
            'opt out' in subject or
            'opt-out' in subject
        ):
            return 'unsubscribe'
        
        # Check for spam filters and security blocks
        if (
            'spam detection' in subject or
            'blocked sender' in subject or
            'cold email shield' in from_addr or
            'shield@mixmax' in from_addr or
            'yooz@invitations' in from_addr or
            'proofpoint' in from_addr or
            'seg-az notification' in subject or
            'trustwave' in from_addr
        ):
            return 'spam_filters'
        
        # Check for security alerts
        if (
            'security alert' in subject or
            'suspicious activity' in subject or
            'login attempt' in subject
        ):
            return 'security_alerts'
        
        # Check for replies (Re: in subject) - but not auto-replies
        if (subject.startswith('re:') or subject.startswith('re ')) and auto_submitted != 'auto-replied':
            return 'replies'
        
        return 'other'
    
    def analyze_all(self):
        """Analyze all emails in the directory"""
        # Find all .eml files recursively
        email_files = list(self.emails_dir.rglob('*.eml'))
        total = len(email_files)
        
        print(f"Found {total} email files to analyze...")
        
        for idx, filepath in enumerate(email_files, 1):
            if idx % 5000 == 0:
                print(f"Progress: {idx}/{total} emails processed...")
            
            msg = self.parse_email(filepath)
            category = self.categorize_email(filepath, msg)
            # Store relative path from emails_dir
            rel_path = filepath.relative_to(self.emails_dir)
            self.categories[category].append(str(rel_path))
        
        print(f"\nAnalysis complete! Processed {total} emails.")
        return self.categories
    
    def generate_report(self, output_file='analysis_report.txt'):
        """Generate a detailed report of the analysis"""
        with open(output_file, 'w') as f:
            f.write("=" * 80 + "\n")
            f.write("EMAIL ANALYSIS REPORT\n")
            f.write("=" * 80 + "\n\n")
            
            total = sum(len(emails) for emails in self.categories.values())
            f.write(f"Total emails analyzed: {total}\n\n")
            
            # Sort categories by count
            sorted_categories = sorted(self.categories.items(), 
                                     key=lambda x: len(x[1]), 
                                     reverse=True)
            
            f.write("SUMMARY BY CATEGORY:\n")
            f.write("-" * 80 + "\n")
            for category, emails in sorted_categories:
                count = len(emails)
                percentage = (count / total * 100) if total > 0 else 0
                category_name = category.replace('_', ' ').title()
                f.write(f"{category_name:30s}: {count:6d} ({percentage:5.2f}%)\n")
            
            f.write("\n" + "=" * 80 + "\n\n")
            
            # Detailed listings
            for category, emails in sorted_categories:
                if emails:
                    category_name = category.replace('_', ' ').title()
                    f.write(f"\n{category_name.upper()} ({len(emails)} emails)\n")
                    f.write("-" * 80 + "\n")
                    for email_name in sorted(emails)[:100]:  # Show first 100
                        f.write(f"  {email_name}\n")
                    if len(emails) > 100:
                        f.write(f"  ... and {len(emails) - 100} more\n")
                    f.write("\n")
        
        print(f"\nDetailed report saved to: {output_file}")
    
    def save_categories_json(self, output_file='categories.json'):
        """Save categories to JSON file"""
        with open(output_file, 'w') as f:
            json.dump(self.categories, f, indent=2)
        print(f"Categories saved to: {output_file}")
    
    def save_categories_csv(self, output_file='email_categories.csv'):
        """Save categorized emails to CSV file"""
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Email Filename', 'Category', 'Category Name'])
            
            # Write all emails with their categories
            for category, emails in sorted(self.categories.items()):
                category_name = category.replace('_', ' ').title()
                for email_file in sorted(emails):
                    writer.writerow([email_file, category, category_name])
        
        print(f"Categories CSV saved to: {output_file}")
    
    def extract_original_recipient(self, msg, body, category):
        """Extract the original recipient email address from bounce messages and other notifications"""
        if not msg or not body:
            return ''
        
        # For bounces, action_required, spam_filters, and auto-replies, 
        # try to extract who the original email was sent to
        
        # Common patterns in bounce messages and notifications
        patterns = [
            # "The following message to <email@example.com>"
            r'the following message to\s*<?([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})>?',
            # "Your message to email@example.com"
            r'your message to\s+([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})',
            # "Your email to email@example.com"
            r'your email to\s+([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})',
            # "message to email@example.com failed"
            r'message to\s+([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})\s+(?:failed|could not)',
            # "Delivery to email@example.com failed"
            r'delivery (?:to|of your message to)\s+([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})',
            # "recipient address rejected: email@example.com"
            r'recipient address rejected:\s+([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})',
            # "To: <email@example.com>" in body
            r'To:\s*<?([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})>?',
            # "email inbox email@example.com is no longer"
            r'email inbox\s+([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})\s+is no longer',
            # "This email inbox email@example.com"
            r'this email inbox\s+([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})',
            # For action required: "to email@example.com with the Subject"
            r'to\s+([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})\s+with the subject',
            # "delivering your message to email@example.com"
            r'delivering your message to\s+([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})',
        ]
        
        body_lower = body.lower()
        
        # Try each pattern
        for pattern in patterns:
            match = re.search(pattern, body_lower, re.IGNORECASE)
            if match:
                email_addr = match.group(1).lower()
                # Filter out beeleads emails (those are the senders, not recipients)
                if not any(domain in email_addr for domain in ['beeleads', 'danny@', 'claire@', 'emma@', 'brian@', 'maddie@']):
                    return email_addr
        
        # Check email headers for original recipient info
        headers_to_check = [
            'X-Failed-Recipients',
            'Original-Recipient',
            'Final-Recipient',
        ]
        
        for header in headers_to_check:
            value = msg.get(header, '')
            if value:
                # Extract email from header value
                match = re.search(r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})', value)
                if match:
                    email_addr = match.group(1).lower()
                    if not any(domain in email_addr for domain in ['beeleads', 'danny@', 'claire@', 'emma@', 'brian@', 'maddie@']):
                        return email_addr
        
        return ''
    
    def save_comprehensive_csv(self, output_file='comprehensive_email_details.csv'):
        """Save all email details including To, Body, and category to a single comprehensive CSV file"""
        print(f"\nGenerating comprehensive email details file...")
        
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                'Email Filename',
                'Category',
                'Category Name',
                'From',
                'To',
                'Subject',
                'Date',
                'Body Preview',
                'Original_Recipient'
            ])
            
            total_emails = sum(len(emails) for emails in self.categories.values())
            processed = 0
            
            # Process all emails with their categories
            for category, email_files in sorted(self.categories.items()):
                category_name = category.replace('_', ' ').title()
                
                for email_file in sorted(email_files):
                    processed += 1
                    if processed % 5000 == 0:
                        print(f"Progress: {processed}/{total_emails} emails processed...")
                    
                    filepath = self.emails_dir / email_file
                    if not filepath.exists():
                        continue
                    
                    # Parse email to get full details
                    msg = self.parse_email(filepath)
                    if msg:
                        from_addr = msg.get('From', '')
                        to_addr = msg.get('To', '')
                        subject = msg.get('Subject', '')
                        date = msg.get('Date', '')
                        
                        # Get email body (first 500 chars for preview)
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
                            body = ''
                        
                        # Extract original recipient (who the outbound email was sent to)
                        full_body = body  # Keep full body for extraction
                        
                        # Clean and limit body for CSV
                        if body:
                            body = body[:500].replace('\n', ' ').replace('\r', ' ').strip()
                        
                        # Extract original recipient email address
                        original_recipient = self.extract_original_recipient(msg, full_body, category)
                        
                        writer.writerow([
                            email_file,
                            category,
                            category_name,
                            from_addr,
                            to_addr,
                            subject,
                            date,
                            body,
                            original_recipient
                        ])
        
        print(f"✓ Comprehensive email details saved to: {output_file}")
    
    def print_summary(self):
        """Print a summary of the analysis"""
        total = sum(len(emails) for emails in self.categories.values())
        
        print("\n" + "=" * 80)
        print("ANALYSIS SUMMARY")
        print("=" * 80)
        print(f"\nTotal emails analyzed: {total}\n")
        
        # Sort categories by count
        sorted_categories = sorted(self.categories.items(), 
                                 key=lambda x: len(x[1]), 
                                 reverse=True)
        
        for category, emails in sorted_categories:
            count = len(emails)
            percentage = (count / total * 100) if total > 0 else 0
            category_name = category.replace('_', ' ').title()
            print(f"{category_name:30s}: {count:6d} ({percentage:5.2f}%)")
        
        print("=" * 80)


def main():
    # Path to the emails directory
    emails_dir = './relpies1114'
    
    if not os.path.exists(emails_dir):
        print(f"Error: Directory '{emails_dir}' not found!")
        print("Please ensure the relpies1114.zip file has been extracted.")
        return
    
    # Create analyzer
    analyzer = EmailAnalyzer(emails_dir)
    
    # Analyze all emails
    print("Starting email analysis...")
    analyzer.analyze_all()
    
    # Print summary
    analyzer.print_summary()
    
    # Generate detailed report
    analyzer.generate_report('analysis_report.txt')
    
    # Save categories to JSON
    analyzer.save_categories_json('categories.json')
    
    # Save categories to CSV
    analyzer.save_categories_csv('email_categories.csv')
    
    # Save comprehensive details to CSV
    analyzer.save_comprehensive_csv('comprehensive_email_details.csv')
    
    print("\n✓ Analysis complete!")
    print("  - Summary displayed above")
    print("  - Detailed report: analysis_report.txt")
    print("  - JSON data: categories.json")
    print("  - CSV data: email_categories.csv")
    print("  - Comprehensive details: comprehensive_email_details.csv (includes To, Body)")


if __name__ == '__main__':
    main()
