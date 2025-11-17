# Quick Start Guide

## Setup

1. **Download the email data** (if not already done):
   ```bash
   # Download relpies1114.zip from the v1.0.0 release
   curl -L -o relpies1114.zip "https://github.com/dannysachdev/emailanalyzer/releases/download/v1.0.0/relpies1114.zip"
   
   # Extract
   unzip relpies1114.zip
   ```

2. **Verify directory structure**:
   ```bash
   ls -la
   # Should see: relpies1114/ directory with 50,215 .eml files
   ```

## Usage

### Option 1: Run Full Pipeline (Recommended)

**Single command to do everything:**
```bash
python3 run_full_analysis.py
```

This will:
1. Analyze and categorize all 50,215 emails
2. Extract contact info from 556+ responses
3. Enrich the database with lead scoring
4. Generate all output files

**Time**: ~60 seconds  
**Outputs**: 5 files ready for use

### Option 2: Run Individual Steps

**Step 1: Analyze emails**
```bash
python3 analyze_emails.py
```
Output: `analysis_report.txt`, `categories.json`, `email_categories.csv`

**Step 2: Extract contacts**
```bash
python3 extract_contact_info.py
```
Output: `extracted_contacts.csv`, `extracted_contacts.json`

**Step 3: Enrich database**
```bash
python3 enrich_contacts.py
```
Output: `enriched_contacts.csv`, `high_quality_leads.csv`

## Output Files Explained

### 1. analysis_report.txt
📊 **Detailed email categorization report**
- 50,215 emails categorized into 12 types
- Full listings of each category
- Use for: Understanding email campaign results

### 2. categories.json
📁 **Machine-readable email categories**
- JSON format for programmatic access
- Use for: API integration, custom processing

### 3. email_categories.csv
📊 **All emails with categories in CSV format (50,215 emails)**
- Each email with its assigned category
- Columns: Email Filename, Category, Category Name
- Use for: Spreadsheet analysis, filtering, pivot tables

### 4. enriched_contacts.csv
👥 **Full contact database (388 contacts)**
- Sorted by lead score (highest first)
- Includes: name, email, phone, title, company
- Use for: CRM import, full contact list

### 5. high_quality_leads.csv
⭐ **Best leads only (245 contacts)**
- Score ≥ 70 (high quality)
- Ready for immediate action
- Use for: Priority follow-up, LinkedIn outreach

### 6. extracted_contacts.json
📋 **Raw contact data in JSON**
- All extracted information
- Use for: Custom processing, database import

## What You Get

### By Category
- **50,215 emails** analyzed
- **49,204 bounces** (98%) - Clean your lists!
- **316 out-of-office** (0.63%)
- **208 automatic replies** (0.41%)
- **33 human replies** (0.07%)

### Extracted Contacts
- **388 total contacts** with engagement
- **387 corporate emails** (99.7%)
- **245 high-quality leads** (63.1%)
- **118 phone numbers** extracted (30.4%)

### Top Companies in Database
1. Fortinet (15 contacts)
2. Kuehne-Nagel (12 contacts)
3. Veeam (12 contacts)
4. Diligent (10 contacts)
5. D&H Distributing (5 contacts)

## Next Steps

### 1. Import to CRM
```bash
# Use enriched_contacts.csv
# Import fields: Email, Name, Phone, Title, Company, Lead Score
```

### 2. Start with High-Quality Leads
```bash
# Open high_quality_leads.csv
# Sort by lead score
# Start outreach with top 50
```

### 3. LinkedIn Outreach
- Use "LinkedIn Search" column from CSV
- Search for contacts on LinkedIn
- Personalize connection requests

### 4. Follow-up Campaigns
- **Out of Office**: Schedule follow-up after return
- **Auto-Replies**: Send additional information
- **Replies**: Immediate personal follow-up
- **Interested**: Schedule meetings/calls

## Sample Lead Record

```csv
Lead Score: 110
Name: Maddie Kane
Email: bgmartinez4@utep.edu
Phone: 915-504-4813
Title: Manager, Event & Marketing
Company: UTEP
LinkedIn Search: Maddie Kane UTEP
Response Type: Reply - Interested
```

## Tips

### Maximize Value
1. **Clean your lists**: 98% bounce rate means list quality issues
2. **Prioritize engagement**: Focus on the 388 engaged contacts
3. **Research top companies**: Many contacts from same companies
4. **Time follow-ups**: Check OOO dates before contacting

### Data Quality
- ✅ 99.7% corporate emails (verified, professional)
- ✅ 99% have names extracted
- ✅ 30% have phone numbers
- ⚠️ Some titles may need cleaning (from signatures)

### Best Practices
- **Verify info**: Double-check phone numbers before calling
- **Personalize**: Reference their original response
- **Segment**: Different approaches for OOO vs replies
- **Update CRM**: Keep contact database current

## Troubleshooting

**"Directory not found"**
```bash
# Make sure relpies1114.zip is extracted
unzip -q relpies1114.zip
```

**"categories.json not found"**
```bash
# Run analysis first
python3 analyze_emails.py
```

**"No module named..."**
```bash
# All scripts use Python standard library only
# Just need Python 3.6+
python3 --version
```

## Questions?

Check these files for more details:
- `README.md` - Full documentation
- `ANALYSIS_SUMMARY.md` - Email analysis results
- `CONTACT_DATABASE_SUMMARY.md` - Contact database details
