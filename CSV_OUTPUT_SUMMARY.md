# CSV Output Files Summary

## Analysis Completed Successfully! ✅

The email analyzer has been run successfully on **50,215 emails**. Below is a summary of the generated CSV output files.

---

## Generated CSV Files

### 1. comprehensive_email_details.csv ⭐ NEW!
- **Size**: ~6-8 MB
- **Rows**: 50,216 (including header)
- **Description**: **ALL EMAIL DATA IN ONE FILE** - Complete details including To, Body, and Category
- **Columns**:
  - `Email Filename` - Name of the email file
  - `Category` - Internal category code
  - `Category Name` - Human-readable category name
  - `From` - Sender email address
  - `To` - Recipient email address(es)
  - `Subject` - Email subject line
  - `Date` - Email date/time
  - `Body Preview` - First 500 characters of email body

**Sample Data**:
```csv
Email Filename,Category,Category Name,From,To,Subject,Date,Body Preview
"test_reply.eml","replies","Replies","john.doe@example.com","sales@company.com","Re: Business proposal","Mon, 14 Nov 2024 10:30:00 -0500","Hi, Thanks for reaching out! I'm interested..."
```

**Key Features**:
- ✅ Single file with all email details
- ✅ Includes recipient information (To field)
- ✅ Includes email body content (first 500 chars)
- ✅ Perfect for importing to databases or spreadsheets
- ✅ Search through email bodies for keywords

📖 **See [COMPREHENSIVE_EXPORT.md](COMPREHENSIVE_EXPORT.md) for detailed documentation**

---

### 2. email_categories.csv
- **Size**: 5.8 MB
- **Rows**: 50,216 (including header)
- **Description**: Complete categorization of all emails
- **Columns**:
  - `Email Filename` - Name of the email file
  - `Category` - Internal category code
  - `Category Name` - Human-readable category name

**Sample Data**:
```csv
Email Filename,Category,Category Name
ACTION REQUIRED  Your email host is not configured correctly! - proofpoint-pps@ppops.net - 2025-11-14 1501.eml,action_required,Action Required
ACTION REQUIRED  Your email host is not configured correctly! - proofpoint-pps@ppops.net - 2025-11-14 1502.eml,action_required,Action Required
```

**Category Distribution**:
- Bounces: 49,204 (97.99%)
- Out of Office: 316 (0.63%)
- Other: 298 (0.59%)
- Automatic Replies: 208 (0.41%)
- Spam Filters: 63 (0.13%)
- Security Alerts: 38 (0.08%)
- Replies: 33 (0.07%)
- Verification Requests: 27 (0.05%)
- Action Required: 18 (0.04%)
- Unsubscribe: 9 (0.02%)
- Contact Info: 1 (0.00%)

---

### 3. enriched_contacts.csv
- **Size**: 114 KB
- **Rows**: 389 (including header)
- **Description**: Full enriched contact database with all 388 unique contacts
- **Columns**:
  - `Lead Score` - Quality score (0-110+)
  - `Name` - Contact name
  - `Primary Email` - Main email address
  - `All Emails` - All email addresses found (semicolon-separated)
  - `Primary Phone` - Main phone number
  - `All Phones` - All phone numbers found (semicolon-separated)
  - `Job Title` - Contact's job title
  - `Company` - Company name
  - `Domain` - Email domain
  - `Is Free Email` - Yes/No indicator
  - `Response Type` - Type of response (Reply, Out of Office, etc.)
  - `LinkedIn Search` - Suggested LinkedIn search string
  - `Category` - Email category
  - `Original Subject` - Subject line of original email
  - `Date` - Date of email
  - `To` - Recipient email address(es) ⭐ NEW
  - `Body` - Email body preview (first 2000 chars) ⭐ NEW

**Sample Data**:
```csv
Lead Score,Name,Primary Email,Phone,Job Title,Company,Response Type
110,NFX Investment Team,danny@beeleads.ai,8082280892,"> traditional lead generation...",NFX.,Reply - Interested
110,Maddie Kane,bgmartinez4@utep.edu,9157475481,"> Manager, Event & Marketing",Utep,Reply - Interested
100,Jason Kenney,jason.kenney@fulcrumcollaborations.com,8044104060,Marketing Manager,Fulcrumcollaborations,Out of Office - General
```

**Key Statistics**:
- Total contacts: 388
- Corporate emails: 387 (99.7%)
- With phone numbers: 118 (30.4%)
- With names: 386 (99.5%)
- With job titles: 50 (12.9%)
- High quality leads (70+): 244 (62.9%)

---

### 4. high_quality_leads.csv
- **Size**: 29 KB
- **Rows**: 245 (including header)
- **Description**: Filtered list of high-quality leads (lead score ≥ 70)
- **Columns**:
  - `Lead Score` - Quality score (70-110+)
  - `Name` - Contact name
  - `Email` - Email address
  - `Phone` - Phone number
  - `Job Title` - Contact's job title
  - `Company` - Company name
  - `LinkedIn Search` - Suggested LinkedIn search string
  - `Response Type` - Type of response
  - `To` - Recipient email address(es) ⭐ NEW
  - `Body` - Email body preview ⭐ NEW

**Sample Data**:
```csv
Lead Score,Name,Email,Phone,Job Title,Company,LinkedIn Search,Response Type
110,NFX Investment Team,danny@beeleads.ai,8082280892,"> traditional lead generation...",NFX.,NFX Investment Team NFX.,Reply - Interested
110,Maddie Kane,bgmartinez4@utep.edu,9157475481,"> Manager, Event & Marketing",Utep,Maddie Kane Utep,Reply - Interested
100,Jason Kenney,jason.kenney@fulcrumcollaborations.com,8044104060,Marketing Manager,Fulcrumcollaborations,Jason Kenney Fulcrumcollaborations,Out of Office - General
```

**Top Companies** (in high-quality leads):
1. Fortinet - 11 contacts
2. Kuehne-nagel - 11 contacts
3. Veeam - 11 contacts
4. Diligent - 10 contacts
5. Dandh - 5 contacts

---

### 5. extracted_contacts.csv
- **Size**: 85 KB
- **Rows**: 389 (including header)
- **Description**: Raw extracted contact data (before enrichment)
- **Columns**:
  - `Primary Email` - Main email address
  - `All Emails` - All email addresses found
  - `Name(s)` - Contact name(s)
  - `Phone(s)` - Phone number(s)
  - `Title` - Job title
  - `Company` - Company name
  - `Category` - Email category
  - `Original Subject` - Subject line
  - `Date` - Date of email
  - `To` - Recipient email address(es) ⭐ NEW
  - `Body` - Email body preview (first 2000 chars) ⭐ NEW

**Sample Data**:
```csv
Primary Email,All Emails,Name(s),Phone(s),Title,Company,Category,Original Subject,Date
aheath@tkcincorporated.com,aheath@tkcincorporated.com,Angela Heath,,,,replies,Re: Guaranteed meetings with content syndication,"Sat, 15 Nov 2025 07:02:02 -0500"
jeremy@birddogsw.com,jeremy@birddogsw.com; sales@birddogsw.com,,8777945950,,,replies,Re: Guaranteed meetings with content syndication,"Fri, 14 Nov 2025 15:07:32 -0500"
```

---

## Analysis Pipeline Summary

**Total Processing Time**: 54.5 seconds (0.9 minutes)

**Pipeline Steps Completed**:
1. ✅ Email Categorization (53.1 seconds) - Analyzed all 50,215 emails
2. ✅ Contact Extraction (1.3 seconds) - Extracted from 558 relevant emails
3. ✅ Contact Enrichment (0.0 seconds) - Enriched 388 contacts with lead scoring

**Additional Output Files** (non-CSV):
- `analysis_report.txt` - Detailed categorization report with full email listings
- `categories.json` - Machine-readable JSON format of email categories
- `extracted_contacts.json` - Raw contact data in JSON format
- `enriched_contacts.json` - Enriched contact data in JSON format

---

## How to Use These Files

### For Complete Email Analysis ⭐ NEW
Use **comprehensive_email_details.csv** - ALL email data in one file (To, Body, Category, everything!)

### For CRM Import
Use **enriched_contacts.csv** - Contains complete contact information with lead scores, To, and Body

### For Immediate Follow-up
Use **high_quality_leads.csv** - Contains only the best quality leads with To and Body

### For Email Campaign Analysis
Use **email_categories.csv** - Shows complete breakdown of all email responses

### For Data Processing
Use **extracted_contacts.csv** or the JSON files for programmatic access

---

## Working with CSV Files - Code Examples

This section provides practical code examples for reading and extracting data from the generated CSV files.

### Python Examples

#### Example 1: Read Email Categories (Standard Library)
```python
import csv

# Read and display email categories
with open('email_categories.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"File: {row['Email Filename']}")
        print(f"Category: {row['Category Name']}")
        print()
```

#### Example 2: Filter by Category
```python
import csv

# Find all replies
with open('email_categories.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    replies = [row for row in reader if row['Category'] == 'replies']
    print(f"Found {len(replies)} reply emails")
    
    # Display first 5 replies
    for reply in replies[:5]:
        print(f"  - {reply['Email Filename']}")
```

#### Example 3: Read Enriched Contacts
```python
import csv

# Read contact database
with open('enriched_contacts.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        print(f"Name: {row['Name']}")
        print(f"Email: {row['Primary Email']}")
        print(f"Lead Score: {row['Lead Score']}")
        print(f"Company: {row['Company']}")
        print()
```

#### Example 4: Filter High-Quality Leads with Phone Numbers
```python
import csv

# Find contacts with lead score >= 90 AND phone numbers
with open('enriched_contacts.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    
    top_leads_with_phone = [
        row for row in reader 
        if int(row['Lead Score']) >= 90 and row['Primary Phone']
    ]
    
    print(f"Found {len(top_leads_with_phone)} top leads with phone numbers:")
    for lead in top_leads_with_phone:
        print(f"  {lead['Name']} - {lead['Primary Email']} - {lead['Primary Phone']}")
```

#### Example 5: Extract Specific Company Contacts
```python
import csv

# Find all contacts from a specific company
target_company = "Fortinet"

with open('enriched_contacts.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    company_contacts = [
        row for row in reader 
        if target_company.lower() in row['Company'].lower()
    ]
    
    print(f"Found {len(company_contacts)} contacts from {target_company}:")
    for contact in company_contacts:
        print(f"  {contact['Name']} ({contact['Job Title']})")
        print(f"    Email: {contact['Primary Email']}")
        print(f"    Phone: {contact['Primary Phone']}")
        print()
```

#### Example 6: Using Pandas for Advanced Analysis
```python
import pandas as pd

# Read CSV with pandas
df = pd.read_csv('enriched_contacts.csv')

# Display basic statistics
print("Contact Database Summary:")
print(f"Total contacts: {len(df)}")
print(f"Contacts with phones: {df['Primary Phone'].notna().sum()}")
print(f"Average lead score: {df['Lead Score'].mean():.1f}")

# Group by company and count
top_companies = df['Company'].value_counts().head(10)
print("\nTop 10 Companies:")
print(top_companies)

# Filter and export
high_quality = df[df['Lead Score'] >= 90]
high_quality.to_csv('my_top_leads.csv', index=False)
print(f"\nExported {len(high_quality)} high-quality leads to my_top_leads.csv")
```

#### Example 7: Search Email Bodies for Keywords
```python
import csv

# Search comprehensive email details for specific keywords
keywords = ["interested", "schedule", "meeting"]

with open('comprehensive_email_details.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    
    matches = []
    for row in reader:
        body = row.get('Body Preview', '').lower()
        if any(keyword in body for keyword in keywords):
            matches.append(row)
    
    print(f"Found {len(matches)} emails containing keywords: {', '.join(keywords)}")
    
    # Display first 5 matches
    for match in matches[:5]:
        print(f"\nFrom: {match['From']}")
        print(f"Subject: {match['Subject']}")
        print(f"Body: {match['Body Preview'][:100]}...")
```

### JavaScript/Node.js Examples

#### Example 8: Read CSV with Node.js
```javascript
const fs = require('fs');
const csv = require('csv-parser');

// Read enriched contacts
const contacts = [];

fs.createReadStream('enriched_contacts.csv')
  .pipe(csv())
  .on('data', (row) => {
    contacts.push(row);
  })
  .on('end', () => {
    console.log(`Loaded ${contacts.length} contacts`);
    
    // Filter high-quality leads
    const highQualityLeads = contacts.filter(c => parseInt(c['Lead Score']) >= 80);
    console.log(`High-quality leads: ${highQualityLeads.length}`);
    
    // Display top 5
    highQualityLeads.slice(0, 5).forEach(lead => {
      console.log(`${lead.Name} - ${lead['Primary Email']} (Score: ${lead['Lead Score']})`);
    });
  });
```

**Note**: Install the csv-parser package first: `npm install csv-parser`

### Command-Line Examples

#### Example 9: Using standard Unix tools
```bash
# Count total emails
wc -l email_categories.csv

# Count replies
grep ",replies," email_categories.csv | wc -l

# Extract all reply emails
grep ",replies," email_categories.csv > replies_only.csv

# View high-quality leads (score >= 90)
head -1 enriched_contacts.csv > top_leads.csv
awk -F',' '$1 >= 90' enriched_contacts.csv >> top_leads.csv

# Search for specific company
grep -i "fortinet" enriched_contacts.csv

# Get unique companies
cut -d',' -f8 enriched_contacts.csv | sort | uniq
```

#### Example 10: Using csvkit for Advanced Operations
```bash
# Install csvkit: pip install csvkit

# View first 10 rows nicely formatted
csvlook enriched_contacts.csv | head -n 20

# Get summary statistics
csvstat enriched_contacts.csv

# Filter contacts with phone numbers
csvgrep -c "Primary Phone" -r ".+" enriched_contacts.csv > contacts_with_phones.csv

# Sort by lead score (descending)
csvsort -c "Lead Score" -r enriched_contacts.csv > sorted_leads.csv

# Convert to JSON
csvjson enriched_contacts.csv > contacts.json

# Search email bodies for keywords
csvgrep -c "Body Preview" -m "interested" comprehensive_email_details.csv
```

### SQL Examples (After Import)

#### Example 11: Import to SQLite and Query
```bash
# Import to SQLite database
sqlite3 emails.db << EOF
.mode csv
.import email_categories.csv email_categories
.import enriched_contacts.csv enriched_contacts
EOF
```

```sql
-- Query examples
-- Count emails by category
SELECT Category_Name, COUNT(*) as Count 
FROM email_categories 
GROUP BY Category_Name 
ORDER BY Count DESC;

-- Find top leads
SELECT Name, Primary_Email, Lead_Score, Company 
FROM enriched_contacts 
WHERE Lead_Score >= 90 
ORDER BY Lead_Score DESC;

-- Find contacts from specific companies
SELECT Name, Primary_Email, Job_Title, Company 
FROM enriched_contacts 
WHERE Company IN ('Fortinet', 'Veeam', 'Diligent')
ORDER BY Company, Lead_Score DESC;
```

### Excel/Google Sheets Tips

#### Working with Large Files
1. **Excel**: Use "Data" → "From Text/CSV" → Select file → Load
2. **Google Sheets**: File → Import → Upload → select file
3. **LibreOffice Calc**: File → Open → Select CSV → Adjust import settings

#### Common Operations
- **Filter by category**: Use AutoFilter (Data → Filter)
- **Sort by lead score**: Select column → Sort Z to A
- **Find keywords in body**: Use Ctrl+F (Find & Replace)
- **Create pivot tables**: Insert → PivotTable
- **Extract subsets**: Filter → Copy visible cells → Paste to new sheet

### Best Practices

1. **Always use UTF-8 encoding** when opening CSV files to handle special characters
2. **Keep original files** - work on copies when filtering or modifying data
3. **Use pandas or csvkit** for large files (50,000+ rows) for better performance
4. **Validate data** after import to ensure no rows were skipped
5. **Handle special characters** - fields with commas are enclosed in quotes automatically

### Common Issues and Solutions

**Issue**: File won't open in Excel  
**Solution**: Use "Data" → "From Text/CSV" instead of double-clicking the file

**Issue**: Special characters appear as gibberish  
**Solution**: Ensure UTF-8 encoding is selected during import

**Issue**: Filtering is slow  
**Solution**: Import to a database (SQLite, PostgreSQL) for faster queries

**Issue**: Need to merge multiple CSV files  
**Solution**: Use pandas `concat()` or csvkit's `csvstack` command

---

## Next Steps

1. **Import to CRM**: Upload enriched_contacts.csv to your CRM system
2. **Prioritize Outreach**: Start with high_quality_leads.csv (sorted by lead score)
3. **LinkedIn Connection**: Use the LinkedIn Search column to find contacts
4. **Follow-up Strategy**: 
   - Immediate action: Reply - Interested contacts
   - Scheduled follow-up: Out of Office contacts (check return dates)
   - Additional nurturing: Auto-Reply contacts

---

## Files Location

All CSV files are located in the repository root directory:
```
/home/runner/work/emailanalyzer/emailanalyzer/
├── email_categories.csv
├── enriched_contacts.csv
├── high_quality_leads.csv
└── extracted_contacts.csv
```

**Note**: These files are excluded from git commits via `.gitignore` to avoid repository bloat.
