# 📧 Phishing Email Detection System

An industry-level **Phishing Email Detection System** that leverages **machine learning**, **deep learning**, and **trusted domain validation** to identify and classify malicious emails. This hybrid approach improves cybersecurity by automating the detection of phishing attempts based on email content, sender/receiver details, and embedded URLs.

---

## 🚀 Features

- 📊 Analyzes 200,000+ email records
- 🧠 ML & DL models including Logistic Regression, Naive Bayes, Decision Tree, ANN, MLP, and LSTM
- 🔍 Regex-powered sender/receiver & URL extraction
- 🛡️ Trusted domain validation from HR-approved list
- ⚡ Hybrid system with real-world applicability
- 📈 Achieves 73.49% final accuracy with enhanced validation

---

## 🧱 Tech Stack

- **Python** 🐍  
- **Pandas / NumPy** – Data manipulation  
- **Scikit-learn** – ML models  
- **TensorFlow / Keras** – Deep Learning models  
- **Regex** – Text feature extraction  
- **JSON** – Trusted domain integration  
- **Matplotlib / Seaborn** – Evaluation visualization

---



---

## 📊 Dataset Description

- **Total Records**: 200,000+
- **Columns**:  
  - `sender`  
  - `receiver`  
  - `subject`  
  - `body`  
  - `label` (phishing or legitimate)

---

## 🔍 Preprocessing & Feature Engineering

- Extracted names/emails from `sender` and `receiver` using **regex**
- Extracted URLs from the `body` and created a new `url_name` column
- Removed irrelevant columns to reduce noise
- Exported cleaned data to `cleaned_data.csv` for modeling

---

## 🤖 Machine Learning Models

| Model               | Accuracy | F1-Score (Phishing) |
|--------------------|----------|---------------------|
| Logistic Regression| 67.05%   | 59%                 |
| Naive Bayes        | 63.64%   | 48%                 |
| Decision Tree      | 51.70%   | 34%                 |

---

## 🧠 Deep Learning Models

| Model               | Accuracy | F1-Score (Phishing) |
|--------------------|----------|---------------------|
| ANN                | 68.71%   | 57%                 |
| MLP                | 62.91%   | 52%                 |
| LSTM               | 60.64%   | 50%                 |

---

## 🛡️ Enhanced Hybrid Detection System

A two-phase validation:

1. ✅ **Trusted Domain Check**  
   - Uses a JSON file with whitelisted domains  
   - If email contains trusted domain → **Legitimate**

2. 🔍 **LSTM-Based Classification**  
   - If no trusted domain → **Classify using LSTM**

### 📈 Final Performance:

- **Accuracy**: 73.49%  
- **Precision (Phishing)**: 50%  
- **Recall (Phishing)**: 98%  
- **F1-Score (Phishing)**: 66%  

---

## 🏆 Technical Achievements

- Processed 200k+ records efficiently
- Regex-driven automated extraction pipelines
- Built & benchmarked 6 ML/DL models
- Integrated real-time domain validation
- Achieved **enterprise-grade accuracy** and low false positives

---

## 🎓 Learning Outcomes

- Mastered feature engineering for cybersecurity data
- Built end-to-end ML pipelines
- Hands-on with ANN, MLP, LSTM architectures
- Implemented hybrid validation for industry deployment
- Developed deep understanding of phishing detection techniques

---

## 🧩 Challenges & Solutions

| Challenge                               | Solution                                             |
|----------------------------------------|------------------------------------------------------|
| Low precision in ML models             | Hybrid LSTM + Trusted Domains                        |
| Processing large datasets              | Batch processing + efficient regex                   |
| Balancing false positives/negatives   | Priority logic using domain trust + model confidence |

---

## 🌍 Real-World Impact

This project delivers a **scalable, accurate, and production-ready** phishing detection system. The combination of LSTM deep learning with real-world trusted domain validation makes it highly suitable for deployment in enterprise environments where cybersecurity is critical.

---

## 🙋 Author

**Brijesh Rakhasiya**  
🎓 AIML Student | 🔐 Cybersecurity Enthusiast | 🤖 Machine Learning Practitioner  

---

## 📜 License

This project is licensed under the **GNU General Public License (GPL)**.  
You are free to use, modify, and distribute it under the terms of the [GPL v3](https://www.gnu.org/licenses/gpl-3.0.html).





