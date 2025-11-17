# Sample CSV Files

This directory contains **sample CSV files** that demonstrate the output format of the email analyzer tool.

## 📁 Available Sample Files

### 1. sample_email_categories.csv
**Sample email categorization data** showing how emails are classified into different categories.

- **Columns**: Email Filename, Category, Category Name
- **Sample Size**: 17 rows (representing different categories)
- **Use Case**: Understanding email categorization output format

**Categories Included**:
- Bounces - Failed delivery notifications
- Out of Office - Vacation/away messages  
- Replies - Human responses
- Automatic Replies - Auto-responders
- Spam Filters - Email security blocks
- Security Alerts - Account security notifications
- Verification Requests - Email verification
- Action Required - Urgent action emails
- Unsubscribe - Unsubscribe confirmations
- Contact Info - Contact updates
- Other - Uncategorized emails

---

### 2. sample_enriched_contacts.csv
**Sample enriched contact database** with complete contact information and lead scoring.

- **Columns**: Lead Score, Name, Primary Email, All Emails, Primary Phone, All Phones, Job Title, Company, Domain, Is Free Email, Response Type, LinkedIn Search, Category, Original Subject, Date
- **Sample Size**: 15 contacts
- **Use Case**: CRM import format, lead scoring examples

**Features**:
- Lead scores ranging from 50-110
- Corporate email addresses
- Phone numbers (where available)
- Job titles and company information
- LinkedIn search strings for easy lookup
- Response type categorization

---

### 3. sample_high_quality_leads.csv
**Sample high-quality leads** filtered for lead score ≥ 70.

- **Columns**: Lead Score, Name, Email, Phone, Job Title, Company, LinkedIn Search, Response Type
- **Sample Size**: 11 high-quality contacts
- **Use Case**: Priority follow-up list

**Highlights**:
- Only includes leads with score 70 or higher
- Ready for immediate outreach
- Includes "Reply - Interested" contacts (highest priority)
- Complete contact information for follow-up

---

### 4. sample_extracted_contacts.csv
**Sample raw contact data** before enrichment processing.

- **Columns**: Primary Email, All Emails, Name(s), Phone(s), Title, Company, Category, Original Subject, Date
- **Sample Size**: 15 contacts
- **Use Case**: Understanding data extraction process, raw data format

**Purpose**:
- Shows data before enrichment
- Useful for comparing raw vs enriched data
- Demonstrates contact extraction from emails

---

## 🎯 How to Use These Samples

### For Testing
Use these sample files to:
- Test your CRM import process
- Understand the data structure
- Develop data processing scripts
- Preview the output format before running the full analysis

### For Learning
Review these samples to:
- See what information the analyzer extracts
- Understand lead scoring methodology
- Learn about different response types
- Explore contact enrichment features

### For Development
Use as reference when:
- Building integrations with the email analyzer
- Developing custom data processing pipelines
- Creating reports or dashboards
- Testing data import/export functionality

---

## 📊 Sample Data Statistics

The sample data includes:
- **15 unique contacts** across various companies
- **Lead scores**: 50-110 (full range)
- **11 contacts** with phone numbers (73%)
- **Top sample companies**: NFX, Utep, Fortinet, Veeam, Kuehne-nagel, Diligent, etc.
- **Response types**: Reply - Interested, Out of Office, Automatic Reply

---

## 🚀 Running the Full Analysis

To generate actual CSV files from your email data:

```bash
# 1. Clone the repository
git clone https://github.com/dannysachdev/emailanalyzer.git
cd emailanalyzer

# 2. Download the email data
# (Place your email .eml files in relpies1114/ directory)

# 3. Run the full analysis
python3 run_full_analysis.py

# 4. Your CSV files will be generated:
# - email_categories.csv
# - enriched_contacts.csv
# - high_quality_leads.csv
# - extracted_contacts.csv
```

---

## 📝 Notes

- These are **sample files** with representative data, not actual analysis results
- The actual analysis can process tens of thousands of emails
- Sample data is fictional and for demonstration purposes only
- Field names and structure match the actual output format
- Use these samples to understand the output before running your own analysis

---

## 📖 Related Documentation

- **README.md** - Main project documentation
- **CSV_OUTPUT_SUMMARY.md** - Detailed CSV format documentation
- **RESULTS_REPORT.md** - Example analysis results
- **HOW_TO_ACCESS_CSV_FILES.md** - Guide for accessing CSV outputs
- **QUICK_START.md** - Quick start guide

---

## ✅ File Format Compatibility

All sample CSV files:
- Use standard CSV format (comma-separated)
- Include headers in the first row
- Are compatible with Excel, Google Sheets, and other spreadsheet applications
- Can be imported into most CRM systems
- Follow UTF-8 encoding

---

## 💡 Tips

1. **Import to Excel/Google Sheets**: Simply open or import these files to explore the data structure
2. **Test CRM Import**: Use these samples to configure your CRM import settings
3. **Data Validation**: Compare your actual results against these samples to verify output format
4. **Learning Tool**: Study the lead scoring to understand what makes a high-quality lead

---

For questions or issues, please refer to the main documentation or create an issue on GitHub.
