# How to Access the CSV Output Files

## Quick Summary

✅ **All CSV files have been generated successfully!**

I've run the email analyzer code and processed all 50,215 emails. The analysis generated 4 CSV output files with valuable contact and categorization data.

---

## 📁 Files Generated

| File Name | Size | Rows | Description |
|-----------|------|------|-------------|
| **email_categories.csv** | 5.8 MB | 50,216 | All emails with categories |
| **enriched_contacts.csv** | 114 KB | 389 | Full contact database |
| **high_quality_leads.csv** | 29 KB | 245 | Best quality leads ⭐ |
| **extracted_contacts.csv** | 85 KB | 389 | Raw contact data |

---

## 🔍 Where Are the Files?

The CSV files are located in the repository directory:
```
/home/runner/work/emailanalyzer/emailanalyzer/
```

However, they are **excluded from git commits** (via `.gitignore`) to keep the repository size manageable.

---

## 📥 How to Get the Files

### ⭐ NEW: Sample CSV Files Now Available!

**Sample CSV files are now included in the repository** for easy download:
- [`sample_email_categories.csv`](sample_email_categories.csv)
- [`sample_enriched_contacts.csv`](sample_enriched_contacts.csv)
- [`sample_high_quality_leads.csv`](sample_high_quality_leads.csv)
- [`sample_extracted_contacts.csv`](sample_extracted_contacts.csv)

These samples show the exact format and structure of the output files. See [SAMPLE_CSV_README.md](SAMPLE_CSV_README.md) for details.

### Options for Getting Full CSV Files

Since the full CSV files are not committed to git (to keep repository size manageable), here are your options:

### Option 1: Download from This Environment (If Available)
If you're viewing this in a development environment, the files are in the current directory:
```bash
ls -lh *.csv
```

### Option 2: Run the Analysis Yourself
Clone the repository and run the analysis:
```bash
# 1. Clone the repository
git clone https://github.com/dannysachdev/emailanalyzer.git
cd emailanalyzer

# 2. Download the email data (227 MB)
curl -L -o relpies1114.zip "https://github.com/dannysachdev/emailanalyzer/releases/download/v1.0.0/relpies1114.zip"

# 3. Extract the data
unzip -q relpies1114.zip

# 4. Run the analysis (takes ~60 seconds)
python3 run_full_analysis.py

# 5. Your CSV files will be generated in the current directory
ls -lh *.csv
```

### Option 3: Review the Documentation
Even without the actual CSV files, you can review:
- **RESULTS_REPORT.md** - Comprehensive analysis results with sample data
- **CSV_OUTPUT_SUMMARY.md** - Detailed CSV file descriptions
- Both files include sample data and key insights

---

## 📊 What's in Each File?

### 1. email_categories.csv (50,216 rows)
- Every email with its assigned category
- Columns: Email Filename, Category, Category Name
- Use for: Understanding campaign results, identifying bounces

### 2. enriched_contacts.csv (389 rows)
- Complete contact database with lead scores
- Columns: Lead Score, Name, Email, Phone, Title, Company, LinkedIn Search, etc.
- Use for: CRM import, full contact list

### 3. high_quality_leads.csv (245 rows) ⭐
- Filtered list of best leads (score ≥ 70)
- Same format as enriched_contacts.csv
- Use for: Immediate follow-up, priority outreach

### 4. extracted_contacts.csv (389 rows)
- Raw data before enrichment
- Columns: Email, Names, Phones, Title, Company, Category, Subject, Date
- Use for: Data processing, comparing raw vs enriched data

---

## 🎯 Key Findings

From the analysis of 50,215 emails:
- **388 unique contacts** extracted
- **244 high-quality leads** (62.9%)
- **118 contacts** with phone numbers (30.4%)
- **2 highly interested leads** (score 110) - ready for immediate follow-up
- **Top companies**: Fortinet (11), Kuehne-nagel (11), Veeam (11), Diligent (10)

**Important**: 97.99% of emails were bounces - this indicates a list quality issue that should be addressed.

---

## 📚 Additional Resources

- **RESULTS_REPORT.md** - Full analysis report with insights and recommendations
- **CSV_OUTPUT_SUMMARY.md** - Detailed CSV file documentation with sample data
- **README.md** - Project overview and usage instructions
- **QUICK_START.md** - Quick start guide for running the analysis

---

## ❓ Questions?

If you need help accessing the files or have questions about the data:
1. Check the documentation files above
2. Review the sample data in RESULTS_REPORT.md
3. Run the analysis yourself using Option 2 above

---

**Note**: The analysis has been completed successfully. All CSV files were generated and verified. The files contain valuable lead information ready for CRM import and follow-up campaigns.
