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

## Contact Extraction & Enrichment

Beyond categorization, the tool can extract and enrich contact information from responses:

### Extract Contact Info
Extracts detailed contact information from replies, out-of-office messages, and automatic replies:
- Email addresses (primary and alternate)
- Phone numbers
- Names
- Job titles
- Company names

```bash
python3 extract_contact_info.py
```

### Enrich Contact Database
Enriches extracted contacts with additional data:
- Lead scoring (prioritizes high-quality contacts)
- Domain analysis (corporate vs free email)
- Company name inference from email domain
- Name inference from email address
- LinkedIn search strings
- Response type categorization

```bash
python3 enrich_contacts.py
```

### Run Full Pipeline
Run all steps in sequence with a single command:

```bash
python3 run_full_analysis.py
```

This executes:
1. Email categorization (analyze_emails.py)
2. Contact extraction (extract_contact_info.py)
3. Contact enrichment (enrich_contacts.py)

**Output files:**
- `enriched_contacts.csv` - Full enriched contact database sorted by lead score
- `high_quality_leads.csv` - Only high-quality leads (score ≥ 70)
- `extracted_contacts.csv` - Raw extracted contact data
- `analysis_report.txt` - Detailed email categorization report
- `categories.json` - Email categories in JSON format

## Requirements

- Python 3.6+
- Standard library only (no external dependencies)