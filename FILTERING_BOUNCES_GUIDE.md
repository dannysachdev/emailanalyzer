# How to Filter Bounces and Clean Your Email Lists

The `comprehensive_email_details.csv` file now includes an `Original_Recipient` column that identifies who your outbound emails were sent to. This is especially useful for identifying problematic email addresses from bounces, auto-replies, and delivery failures.

## Quick Start

### 1. Open the CSV file
Open `comprehensive_email_details.csv` in your spreadsheet application (Excel, Google Sheets, etc.)

### 2. Filter for Bounced Emails
- Click on the "Category Name" column header
- Filter to show only "Bounces"
- Look at the "Original_Recipient" column to see which email addresses bounced

### 3. Extract the List
- Copy all email addresses from the "Original_Recipient" column
- Remove any empty cells
- Save this list for removal from your mailing lists

## What Gets Extracted?

The `Original_Recipient` column contains data for these categories:

| Category | Extraction Rate | What It Tells You |
|----------|----------------|-------------------|
| **Bounces** | ~2% | Email addresses that no longer exist or reject mail |
| **Automatic Replies** | ~17% | Mailboxes that are no longer monitored |
| **Action Required** | ~22% | Addresses with delivery issues (SPF, authentication) |
| **Out of Office** | ~11% | Users who are away (less critical for filtering) |

## Example Workflow in Excel

```
1. Open comprehensive_email_details.csv in Excel
2. Select the entire data range
3. Click Data > Filter
4. Filter "Category Name" = "Bounces"
5. Filter "Original_Recipient" ≠ (empty)
6. Copy the Original_Recipient column
7. Paste into a new sheet
8. Remove duplicates (Data > Remove Duplicates)
9. Export this list to update your CRM/email platform
```

## Example Workflow in Google Sheets

```
1. Upload comprehensive_email_details.csv to Google Sheets
2. Select the header row
3. Click Data > Create a filter
4. Click the filter icon in "Category Name" column
5. Uncheck "Select all", then check only "Bounces"
6. Click the filter icon in "Original_Recipient" column
7. Uncheck "(Blanks)"
8. Copy the visible Original_Recipient values
9. Paste into a new sheet and remove duplicates
```

## Sample Python Script to Extract Bounce List

```python
import csv

bounce_list = set()

with open('comprehensive_email_details.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        # Get bounces with original recipient
        if row['Category'] == 'bounces' and row.get('Original_Recipient'):
            bounce_list.add(row['Original_Recipient'])

# Save to file
with open('bounced_emails.txt', 'w') as f:
    for email in sorted(bounce_list):
        f.write(email + '\n')

print(f"Extracted {len(bounce_list)} unique bounced email addresses")
```

## What to Do with the List

Once you have your list of problematic email addresses:

1. **Update your CRM** - Mark these contacts as "bounced" or "unsubscribed"
2. **Remove from mailing lists** - Delete or suppress these addresses in your email platform
3. **Update contact database** - Flag these records for review or removal
4. **Improve deliverability** - Cleaning your list improves sender reputation and deliverability rates

## Statistics from Current Data

Based on the analysis of 50,215 emails:
- **1,062 original recipients identified** (2.1% extraction rate)
- **710 unique email addresses** found
- **978 bounced emails** with recipient info
- **36 auto-reply addresses** no longer in use

## Why Extraction Rate is Low

The extraction rate is ~2% because:
- The body preview is limited to 500 characters
- Some bounce messages don't include the recipient in the first 500 chars
- Some bounce formats aren't covered by the extraction patterns
- Many emails are not bounces/auto-replies (they're legitimate responses)

This is still valuable because it identifies the most critical bounces that should be removed from your lists.

## Need Help?

If you need to extract more recipients or have a specific email format that isn't being captured, you can:
1. Run the full analysis with access to complete .eml files (not just previews)
2. Add custom extraction patterns to the `extract_original_recipient()` method in `analyze_emails.py`
3. Manually review bounces in the "Bounces" category
