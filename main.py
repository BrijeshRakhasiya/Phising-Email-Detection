<<<<<<< HEAD
# main.py
from email_processor import EmailProcessor

def main():
    processor = EmailProcessor()
    
    # ====== CHOOSE MODE ======
    manual_test = True  # Set to False for CSV processing
    
    if manual_test:
        # Manual email test
        email = {
            'subject': 'Account Verification Required',
            'body': 'Click here: www.tryhackme.com',
            'url_names': 'www.google.com'
        }
        result = processor.process_email(email, manual_mode=True)
        print("\nManual Test Result:")
        print(f"Subject: {email['subject']}")
        print(f"Phishing Prediction: {result['is_phishing']}")
        print(f"Trusted Domain Found: {result['trusted_domain_found']}")
        print(f"Probability: {result['phishing_probability']:.2%}")
    else:
        # CSV processing
        input_csv = './Notebook/data/new_test_merged.csv'
        output_csv = './Test_data_csv/processed_emails_test.csv'
        
        print("\nProcessing batch of emails...")
        processed_df = processor.process_csv(input_csv, output_path=output_csv)
        print(f"Processed {len(processed_df)} emails. Results saved to {output_csv}")

if __name__ == "__main__":
=======
# main.py
from email_processor import EmailProcessor

def main():
    processor = EmailProcessor()
    
    # ====== CHOOSE MODE ======
    manual_test = False  # Set to False for CSV processing
    
    if manual_test:
        # Manual email test
        email = {
            'subject': 'Account Verification Required',
            'body': 'Click here: www.tryhackme.com',
            'url_names': 'www.tryhackme.com'
        }
        result = processor.process_email(email, manual_mode=True)
        print("\nManual Test Result:")
        print(f"Subject: {email['subject']}")
        print(f"Phishing Prediction: {result['is_phishing']}")
        print(f"Trusted Domain Found: {result['trusted_domain_found']}")
        print(f"Probability: {result['phishing_probability']:.2%}")
    else:
        # CSV processing
        input_csv = './Notebook/data/new_test_merged.csv'
        output_csv = './Test_data_csv/processed_emails_test.csv'
        
        print("\nProcessing batch of emails...")
        processed_df = processor.process_csv(input_csv, output_path=output_csv)
        print(f"Processed {len(processed_df)} emails. Results saved to {output_csv}")

if __name__ == "__main__":
>>>>>>> e61dca5c (Update app.py)
    main()