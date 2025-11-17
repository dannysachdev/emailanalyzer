# Email Analysis Summary

## Dataset
- **Source**: relpies1114.zip from v1.0.0 release
- **Total Emails Analyzed**: 50,215

## Results by Category

| Category | Count | Percentage | Description |
|----------|-------|------------|-------------|
| **Bounces** | 49,204 | 97.99% | Failed delivery notifications, undeliverable mail, invalid addresses |
| **Out of Office** | 316 | 0.63% | Vacation and away messages, maternity/parental leave |
| **Other** | 298 | 0.59% | Miscellaneous emails not fitting other categories |
| **Automatic Replies** | 208 | 0.41% | Auto-responders and acknowledgment messages |
| **Spam Filters** | 63 | 0.13% | Blocked by email security (Mixmax, Proofpoint, etc.) |
| **Security Alerts** | 38 | 0.08% | Account security and login notifications |
| **Replies** | 33 | 0.07% | Human responses to outgoing emails |
| **Verification Requests** | 27 | 0.05% | Email verification and validation requests |
| **Action Required** | 18 | 0.04% | Urgent action needed notifications |
| **Unsubscribe** | 9 | 0.02% | Unsubscribe confirmations |
| **Contact Info** | 1 | 0.00% | Contact information updates |
| **Delivery Delays** | 0 | 0.00% | Delayed delivery notifications |

## Key Findings

1. **Overwhelming Bounce Rate**: 98% of emails are bounces, indicating:
   - Many invalid or outdated email addresses in the campaign
   - Potential data quality issues
   - Need for email list cleaning and verification

2. **Low Engagement**: Only 0.07% (33 emails) are actual human replies, suggesting:
   - Low response rate to outgoing campaigns
   - Most responses are automated (out of office, auto-replies)

3. **Email Security Challenges**: 0.13% blocked by spam filters indicates:
   - Some recipients have cold email protection systems
   - Need to review sender reputation and email practices

## Outputs Generated

- **analysis_report.txt**: Detailed report with full email listings by category
- **categories.json**: Machine-readable JSON format for programmatic access
- **Console output**: Real-time progress and summary statistics

## Usage

Run the analyzer with:
```bash
python3 analyze_emails.py
```

The script automatically:
1. Scans all .eml files recursively in relpies1114/
2. Parses email headers and content
3. Categorizes based on subject, sender, and body patterns
4. Generates reports and JSON output
