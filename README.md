# Email Analyzer

A Python tool to analyze and categorize large volumes of emails into different types.

## Overview

This tool processes email files (.eml format) and automatically categorizes them into:

- **Bounces** - Failed delivery notifications, undeliverable mail
- **Out of Office** - Vacation and away messages
- **Automatic Replies** - Auto-responders
- **Replies** - Human responses to emails
- **Contact Info** - Contact information updates
- **Verification Requests** - Email verification and validation requests
- **Action Required** - Urgent action needed emails
- **Spam Filters** - Messages blocked by email security systems
- **Security Alerts** - Account security notifications
- **Unsubscribe** - Unsubscribe confirmations
- **Other** - Emails that don't fit other categories

## Usage

1. Download and extract the email archive (if not already done):
```bash
# The relpies1114.zip file should be in the repository root or releases
unzip relpies1114.zip
```

2. Run the analyzer:
```bash
python3 analyze_emails.py
```

3. Review the results:
   - **Console Output**: Summary statistics showing count and percentage for each category
   - **analysis_report.txt**: Detailed report with all email filenames organized by category
   - **categories.json**: Machine-readable JSON format with all categorized emails

## Results

The analyzer processes all emails in the `relpies1114/` directory recursively and provides:

- Real-time progress updates
- Category-based statistics
- Detailed listings of emails in each category
- JSON export for further processing

## Categories Explained

### Bounces
Failed email deliveries including:
- Undeliverable messages
- Invalid email addresses
- Mailbox full/unavailable
- Blocked senders
- Delivery failures

### Out of Office
Automatic away messages for:
- Vacations
- Maternity/parental leave
- Extended absences

### Automatic Replies
Automated acknowledgment messages that aren't out-of-office

### Replies
Human responses to outgoing emails, including:
- Direct replies
- Forwarded responses
- Engagement from prospects

### Spam Filters
Messages from email security systems:
- Cold email shields (e.g., Mixmax)
- Spam detection systems
- Blocked sender notifications

## Requirements

- Python 3.6+
- Standard library only (no external dependencies)