<<<<<<< HEAD
# email_processor.py (updated)
import pandas as pd
from sklearn.metrics import classification_report, accuracy_score
from utils.domain_checker import DomainChecker
from utils.model_predictor import PhishingPredictor
import re 

class EmailProcessor:
    def __init__(self, threshold=0.5):
        self.domain_checker = DomainChecker()
        self.phishing_predictor = PhishingPredictor(
            model_path='./Models/phishing_detection_deep_lstm.h5',
            tokenizer_paths={
                'subject': './Models/subject_tokenizer.pkl',
                'body': './Models/body_tokenizer.pkl'
            },
            max_lengths={
                'subject': 50,
                'body': 200
            }
        )
        self.threshold = threshold

    def process_email(self, email_data, manual_mode=False):
        """Process single email with enhanced validation"""
        # Check URLs from both dedicated field and body text
        urls = []
        if manual_mode:
            urls = str(email_data.get('url_names', '')).split(',') if pd.notnull(email_data.get('url_names')) else []
        else:
            urls = str(email_data['url_names']).split(',') if pd.notnull(email_data['url_names']) else []
        
        body_urls = re.findall(r'https?://\S+', email_data['body'])
        all_urls = urls + body_urls

        # Enhanced URL analysis
        url_analyses = []
        for url in all_urls:
            if url.strip():
                analysis = self.domain_checker.analyze_url(url.strip())
                url_analyses.append(analysis)
                if analysis['trusted_final_domain']:
                    return {
                        'is_phishing': False,
                        'phishing_probability': 0.0,
                        'trusted_domain_found': True,
                        'message': f'Safe: Resolved to trusted domain {analysis["final_domain"]}',
                        'url_analysis': url_analyses
                    }

        # If no trusted domains, check for trusted shorteners
        if any(a['trusted_shortener'] for a in url_analyses):
            return {
                'is_phishing': False,
                'phishing_probability': 0.0,
                'trusted_domain_found': False,
                'message': 'Caution: Trusted shortener but unresolved destination',
                'url_analysis': url_analyses
            }

        # Original model prediction
        prediction = self.phishing_predictor.predict(
            email_data['subject'],
            email_data['body']
        )
        
        return {
            'is_phishing': prediction > self.threshold,
            'phishing_probability': float(prediction),
            'trusted_domain_found': False,
            'url_analysis': url_analyses,
            'message': 'Checked with AI model'
        }

    def process_csv(self, input_path, output_path):
        """Process CSV with enhanced validation"""
        df = pd.read_csv(input_path).iloc[:5000]
        
        results = []
        for _, row in df.iterrows():
            result = self.process_email(row)
            results.append({
                'predicted_label': 1 if result['is_phishing'] else 0,
                'phishing_probability': result['phishing_probability'],
                'trusted_domain_found': result['trusted_domain_found']
            })
            
        results_df = pd.DataFrame(results)
        output_df = pd.concat([df, results_df], axis=1)
        output_df.to_csv(output_path, index=False)
        
        if 'label' in output_df.columns:
            self._generate_validation_report(output_df, output_path)
            
        return output_df

    def _generate_validation_report(self, df, output_path):
        """Enhanced validation report"""
        actual = df['label']
        predicted = df['predicted_label']
        
        report = classification_report(actual, predicted)
        matrix = pd.crosstab(actual, predicted, 
                           rownames=['Actual'], 
                           colnames=['Predicted'])
        
        report_path = output_path.replace('.csv', '_test_report.txt')
        with open(report_path, 'w') as f:
            f.write("Enhanced Validation Report\n")
            f.write("=========================\n")
            f.write(f"Total Samples: {len(df)}\n")
            f.write(f"Accuracy: {accuracy_score(actual, predicted):.2%}\n\n")
            f.write("Classification Report:\n")
            f.write(report)
            f.write("\n\nConfusion Matrix:\n")
            f.write(matrix.to_string())
        
        print(f"Detailed report saved to {report_path}")

# Key improvements:
# 1. Added manual mode toggle in main.py
# 2. Enhanced URL checking from both dedicated column and body text
# 3. Added probability scores in CSV output
# 4. Improved validation report with confusion matrix
# 5. Added threshold parameter (default 0.5)
=======
# email_processor.py (updated)
import pandas as pd
from sklearn.metrics import classification_report, accuracy_score
from utils.domain_checker import DomainChecker
from utils.model_predictor import PhishingPredictor
import re 

class EmailProcessor:
    def __init__(self, threshold=0.5):
        self.domain_checker = DomainChecker()
        self.phishing_predictor = PhishingPredictor(
            model_path='./Models/phishing_detection_deep_lstm.h5',
            tokenizer_paths={
                'subject': './Models/subject_tokenizer.pkl',
                'body': './Models/body_tokenizer.pkl'
            },
            max_lengths={
                'subject': 50,
                'body': 200
            }
        )
        self.threshold = threshold

    def process_email(self, email_data, manual_mode=False):
        """Process single email with enhanced validation"""
        # Check URLs from both dedicated field and body text
        urls = []
        if manual_mode:
            urls = str(email_data.get('url_names', '')).split(',') if pd.notnull(email_data.get('url_names')) else []
        else:
            urls = str(email_data['url_names']).split(',') if pd.notnull(email_data['url_names']) else []
        
        body_urls = re.findall(r'https?://\S+', email_data['body'])
        all_urls = urls + body_urls

        # Enhanced URL analysis
        url_analyses = []
        for url in all_urls:
            if url.strip():
                analysis = self.domain_checker.analyze_url(url.strip())
                url_analyses.append(analysis)
                if analysis['trusted_final_domain']:
                    return {
                        'is_phishing': False,
                        'phishing_probability': 0.0,
                        'trusted_domain_found': True,
                        'message': f'Safe: Resolved to trusted domain {analysis["final_domain"]}',
                        'url_analysis': url_analyses
                    }

        # If no trusted domains, check for trusted shorteners
        if any(a['trusted_shortener'] for a in url_analyses):
            return {
                'is_phishing': False,
                'phishing_probability': 0.0,
                'trusted_domain_found': False,
                'message': 'Caution: Trusted shortener but unresolved destination',
                'url_analysis': url_analyses
            }

        # Original model prediction
        prediction = self.phishing_predictor.predict(
            email_data['subject'],
            email_data['body']
        )
        
        return {
            'is_phishing': prediction > self.threshold,
            'phishing_probability': float(prediction),
            'trusted_domain_found': False,
            'url_analysis': url_analyses,
            'message': 'Checked with AI model'
        }

    def process_csv(self, input_path, output_path):
        """Process CSV with enhanced validation"""
        df = pd.read_csv(input_path).iloc[:5000]
        
        results = []
        for _, row in df.iterrows():
            result = self.process_email(row)
            results.append({
                'predicted_label': 1 if result['is_phishing'] else 0,
                'phishing_probability': result['phishing_probability'],
                'trusted_domain_found': result['trusted_domain_found']
            })
            
        results_df = pd.DataFrame(results)
        output_df = pd.concat([df, results_df], axis=1)
        output_df.to_csv(output_path, index=False)
        
        if 'label' in output_df.columns:
            self._generate_validation_report(output_df, output_path)
            
        return output_df

    def _generate_validation_report(self, df, output_path):
        """Enhanced validation report"""
        actual = df['label']
        predicted = df['predicted_label']
        
        report = classification_report(actual, predicted)
        matrix = pd.crosstab(actual, predicted, 
                           rownames=['Actual'], 
                           colnames=['Predicted'])
        
        report_path = output_path.replace('.csv', '_test_report.txt')
        with open(report_path, 'w') as f:
            f.write("Enhanced Validation Report\n")
            f.write("=========================\n")
            f.write(f"Total Samples: {len(df)}\n")
            f.write(f"Accuracy: {accuracy_score(actual, predicted):.2%}\n\n")
            f.write("Classification Report:\n")
            f.write(report)
            f.write("\n\nConfusion Matrix:\n")
            f.write(matrix.to_string())
        
        print(f"Detailed report saved to {report_path}")

# Key improvements:
# 1. Added manual mode toggle in main.py
# 2. Enhanced URL checking from both dedicated column and body text
# 3. Added probability scores in CSV output
# 4. Improved validation report with confusion matrix
# 5. Added threshold parameter (default 0.5)
>>>>>>> e61dca5c (Update app.py)
# 6. Better handling of manual vs CSV input