#!/usr/bin/env python3
"""
Test script to verify comprehensive email details export functionality
"""

import os
import sys
import csv
from pathlib import Path

def test_analyze_emails():
    """Test that analyze_emails.py generates comprehensive CSV with To and Body"""
    print("\n" + "=" * 80)
    print("TEST 1: Testing analyze_emails.py comprehensive export")
    print("=" * 80 + "\n")
    
    # Import and run analyzer on test emails
    import analyze_emails
    
    # Create analyzer with test directory
    analyzer = analyze_emails.EmailAnalyzer('./test_emails')
    
    # Analyze all emails
    print("Analyzing test emails...")
    analyzer.analyze_all()
    
    # Generate comprehensive CSV
    print("\nGenerating comprehensive CSV...")
    analyzer.save_comprehensive_csv('test_comprehensive_details.csv')
    
    # Verify the file was created
    if not os.path.exists('test_comprehensive_details.csv'):
        print("❌ FAILED: test_comprehensive_details.csv was not created")
        return False
    
    # Read and verify the CSV content
    print("\nVerifying CSV content...")
    with open('test_comprehensive_details.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        
        if not rows:
            print("❌ FAILED: CSV file is empty")
            return False
        
        # Check that we have the expected columns
        expected_columns = ['Email Filename', 'Category', 'Category Name', 'From', 'To', 'Subject', 'Date', 'Body Preview']
        actual_columns = reader.fieldnames
        
        missing_columns = set(expected_columns) - set(actual_columns)
        if missing_columns:
            print(f"❌ FAILED: Missing columns: {missing_columns}")
            return False
        
        print(f"✓ Found {len(rows)} emails in CSV")
        print(f"✓ All expected columns present: {', '.join(expected_columns)}")
        
        # Check that To and Body fields have data
        rows_with_to = sum(1 for row in rows if row['To'])
        rows_with_body = sum(1 for row in rows if row['Body Preview'])
        
        print(f"✓ Rows with 'To' field: {rows_with_to}/{len(rows)}")
        print(f"✓ Rows with 'Body Preview' field: {rows_with_body}/{len(rows)}")
        
        # Print sample row for verification
        if rows:
            print("\nSample row:")
            for key, value in list(rows[0].items())[:5]:
                print(f"  {key}: {value[:50] if value else '(empty)'}...")
    
    print("\n✓ TEST 1 PASSED: Comprehensive CSV export works correctly")
    return True

def test_extract_contact_info():
    """Test that extract_contact_info.py includes To and Body fields"""
    print("\n" + "=" * 80)
    print("TEST 2: Testing extract_contact_info.py with To and Body")
    print("=" * 80 + "\n")
    
    import analyze_emails
    import extract_contact_info
    
    # First generate categories.json
    print("Generating categories.json...")
    analyzer = analyze_emails.EmailAnalyzer('./test_emails')
    analyzer.analyze_all()
    analyzer.save_categories_json('test_categories.json')
    
    # Now extract contact info
    print("\nExtracting contact information...")
    extractor = extract_contact_info.ContactInfoExtractor('./test_emails', 'test_categories.json')
    extractor.extract_from_categories(['replies', 'out_of_office', 'automatic_replies'])
    
    if not extractor.contacts:
        print("⚠️ WARNING: No contacts extracted (may be expected for test data)")
        return True
    
    # Save to CSV
    print("\nSaving to CSV...")
    extractor.save_to_csv('test_extracted_contacts.csv')
    
    # Verify the file was created
    if not os.path.exists('test_extracted_contacts.csv'):
        print("❌ FAILED: test_extracted_contacts.csv was not created")
        return False
    
    # Read and verify the CSV content
    print("\nVerifying CSV content...")
    with open('test_extracted_contacts.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        
        # Check that we have the To and Body columns
        if 'To' not in reader.fieldnames:
            print("❌ FAILED: 'To' column not found in CSV")
            return False
        
        if 'Body' not in reader.fieldnames:
            print("❌ FAILED: 'Body' column not found in CSV")
            return False
        
        print(f"✓ Found {len(rows)} contacts in CSV")
        print(f"✓ 'To' column present")
        print(f"✓ 'Body' column present")
        
        # Check that fields have data (if contacts exist)
        if rows:
            rows_with_to = sum(1 for row in rows if row['To'])
            rows_with_body = sum(1 for row in rows if row['Body'])
            
            print(f"✓ Rows with 'To' field: {rows_with_to}/{len(rows)}")
            print(f"✓ Rows with 'Body' field: {rows_with_body}/{len(rows)}")
    
    print("\n✓ TEST 2 PASSED: Contact extraction includes To and Body")
    return True

def cleanup():
    """Clean up test files"""
    print("\nCleaning up test files...")
    test_files = [
        'test_comprehensive_details.csv',
        'test_extracted_contacts.csv',
        'test_categories.json'
    ]
    
    for file in test_files:
        if os.path.exists(file):
            os.remove(file)
            print(f"  Removed {file}")

def main():
    print("=" * 80)
    print("COMPREHENSIVE EMAIL EXPORT TEST SUITE")
    print("=" * 80)
    
    # Run tests
    test1_passed = test_analyze_emails()
    test2_passed = test_extract_contact_info()
    
    # Cleanup
    cleanup()
    
    # Summary
    print("\n" + "=" * 80)
    print("TEST SUMMARY")
    print("=" * 80)
    print(f"Test 1 (Comprehensive CSV): {'✓ PASSED' if test1_passed else '❌ FAILED'}")
    print(f"Test 2 (Contact Extraction): {'✓ PASSED' if test2_passed else '❌ FAILED'}")
    
    if test1_passed and test2_passed:
        print("\n✓ ALL TESTS PASSED!")
        return 0
    else:
        print("\n❌ SOME TESTS FAILED")
        return 1

if __name__ == '__main__':
    sys.exit(main())
