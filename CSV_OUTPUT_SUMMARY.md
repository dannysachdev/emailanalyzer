# CSV Output Files Summary

## Analysis Completed Successfully! ✅

The email analyzer has been run successfully on **50,215 emails**. Below is a summary of the generated CSV output files.

---

## Generated CSV Files

### 1. email_categories.csv
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

### 2. enriched_contacts.csv
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

### 3. high_quality_leads.csv
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

### 4. extracted_contacts.csv
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

### For CRM Import
Use **enriched_contacts.csv** - Contains complete contact information with lead scores

### For Immediate Follow-up
Use **high_quality_leads.csv** - Contains only the best quality leads ready for outreach

### For Email Campaign Analysis
Use **email_categories.csv** - Shows complete breakdown of all email responses

### For Data Processing
Use **extracted_contacts.csv** or the JSON files for programmatic access

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
