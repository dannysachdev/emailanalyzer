#!/usr/bin/env python3
"""
Full Email Analysis Pipeline
Runs all analysis steps in sequence:
1. Categorize emails
2. Extract contact information
3. Enrich contact database
"""

import os
import sys
import time


def run_step(step_name, script_name):
    """Run a single step of the pipeline"""
    print("\n" + "=" * 80)
    print(f"STEP: {step_name}")
    print("=" * 80 + "\n")
    
    start_time = time.time()
    
    # Import and run the script
    if script_name == 'analyze_emails':
        import analyze_emails
        analyze_emails.main()
    elif script_name == 'extract_contact_info':
        import extract_contact_info
        extract_contact_info.main()
    elif script_name == 'enrich_contacts':
        import enrich_contacts
        enrich_contacts.main()
    
    elapsed = time.time() - start_time
    print(f"\n✓ {step_name} completed in {elapsed:.1f} seconds")


def main():
    print("=" * 80)
    print("FULL EMAIL ANALYSIS PIPELINE")
    print("=" * 80)
    print("\nThis pipeline will:")
    print("1. Analyze and categorize all emails")
    print("2. Extract contact information from responses")
    print("3. Enrich the contact database with additional data")
    print("\n" + "=" * 80 + "\n")
    
    # Check if emails directory exists
    if not os.path.exists('./relpies1114'):
        print("Error: relpies1114 directory not found!")
        print("Please extract the relpies1114.zip file first.")
        return 1
    
    total_start = time.time()
    
    try:
        # Step 1: Categorize emails
        run_step("1. Email Categorization", "analyze_emails")
        
        # Step 2: Extract contact info
        run_step("2. Contact Information Extraction", "extract_contact_info")
        
        # Step 3: Enrich contacts
        run_step("3. Contact Database Enrichment", "enrich_contacts")
        
    except Exception as e:
        print(f"\n✗ Pipeline failed with error: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    total_elapsed = time.time() - total_start
    
    print("\n" + "=" * 80)
    print("PIPELINE COMPLETE!")
    print("=" * 80)
    print(f"\nTotal time: {total_elapsed:.1f} seconds ({total_elapsed/60:.1f} minutes)")
    print("\nGenerated files:")
    print("  1. analysis_report.txt - Detailed email categorization")
    print("  2. categories.json - Email categories in JSON format")
    print("  3. extracted_contacts.csv - Raw extracted contacts")
    print("  4. enriched_contacts.csv - Enriched contact database (sorted by lead score)")
    print("  5. high_quality_leads.csv - Best quality leads only")
    print("\n✓ All analysis complete! Check the files above for results.")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
