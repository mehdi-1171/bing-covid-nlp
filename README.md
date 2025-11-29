# 🦠 bing-covid-nlp

## Description
Classifying Bing COVID-19 queries into Specific vs Generic using NLP

This project focuses on classifying COVID-19–related search queries from Bing into two categories:

> Specific queries → contain references to particular locations, timelines, or entities

> Generic queries → general questions about COVID-19 symptoms, spread, prevention, etc.

The goal is to use Natural Language Processing (NLP) techniques to automatically detect the “specificity” of a query.
This helps search engines, health organizations, and information systems understand public needs more accurately.

## 📌 Project Goals

* Build a clean and reproducible NLP pipeline
* Classify queries into Specific vs Generic
* Compare machine learning models (Logistic Regression, SVM, Random Forest, XGBoost)
* Evaluate deep learning models (LSTM / BERT)
* Analyze which keywords strongly indicate specific vs generic intent
* Provide explainability (e.g., SHAP, LIME)

## 📁 Dataset

BingCoronavirusQuerySet 

Includes anonymized COVID-19–related queries collected during the pandemic.

Each row typically contains:

- Query — text entered by a user
- Label — specific or generic

## 🏗️ Project Structure
```
bing-covid-nlp/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_exploration.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_baseline_models.ipynb
│   └── 04_bert_model.ipynb
│
├── src/
│   ├── data_preprocessing.py
│   ├── train_baseline.py
│   ├── train_bert.py
│   └── utils.py
│
├── models/
│   └── saved_models/
│
├── results/
│   ├── metrics.json
│   ├── confusion_matrix.png
│   └── feature_importance.png
│
├── requirements.txt
└── README.md
```

## 🔧 Installation

```
git clone https://github.com/mehdi_1171/bing-covid-nlp
cd bing-covid-nlp
pip install -r requirements.txt

```

## 🧹 Preprocessing Steps

- Text normalization
- Lowercasing
- Removing URLs, numbers, stopwords
- Lemmatization
- TF-IDF vectorization or tokenization (for deep learning)

## 🤖 Models Used
- Baseline ML Models:
    - Logistic Regression 
    - SVM
    - Random Forest
    - Naive Bayes
    - XGBoost

- Deep Learning Models

    - LSTM with pretrained embeddings 
    - BERT (bert-base-uncased)


## 📊 Evaluation Metrics

- Accuracy
- Precision / Recall / F1-score
- ROC-AUC
- Confusion Matrix

## 📝 Results
```
_____________________________________
|       Model         |  Accuracy   |
_____________________________________
| Logistic Regression |	  0.89      |
_____________________________________
|        SVM          |   0.90      |
_____________________________________
|       BERT	      |   0.95      |    
_____________________________________
```

## 🧠 Explainability

To understand why a query is predicted as Specific vs Generic:

- SHAP (feature influence)
- LIME (local explanations)


## 🚀 How to Run

- Train baseline model:
```
python src/train_baseline.py
```

- Train BERT model:
```
python src/train_bert.py

```

🧩 Future Improvements

- Add more granular classification (e.g., symptoms / prevention / statistics)
- Deploy model as an API (FastAPI / Flask)
- Create a simple web interface
- Add data augmentation for short queries

📜 License

MIT License