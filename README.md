# 🩺 HealthPrompt - Clinical Document Risk Classification (NLP)

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/ML-Scikit--learn-yellow?logo=scikitlearn)
![License](https://img.shields.io/badge/License-MIT-green)

HealthPrompt is a **Natural Language Processing (NLP)** project designed to classify clinical medical notes into one of three risk levels: **Abnormal**, **Normal**, or **Inconclusive**. It utilizes state-of-the-art text preprocessing, vectorization, and machine learning algorithms to assist in automated medical risk triage.

> 🧠 Built with data science, 🩺 inspired by healthcare, and 🤖 powered by ML!

---

## 🌟 Project Highlights

- Binary & Multiclass classification of clinical notes
- Utilizes **CountVectorizer**, **TF-IDF**, and **Word2Vec**
- Compared multiple classifiers: **Logistic Regression**, **Random Forest**, **XGBoost**, etc.
- Applied model evaluation metrics (accuracy, recall, precision, F1-score)
- Clean and reproducible pipeline for preprocessing and modeling

---

## 🛠 Tech Stack

- **Language**: Python 3.10+
- **Libraries**: 
  - `pandas`, `numpy`, `scikit-learn`, `xgboost`, `gensim`, `matplotlib`, `seaborn`, `nltk`
- **IDE**: Jupyter Notebook, VS Code
- **Version Control**: Git + GitHub

---

## 🧠 How It Works

1. **Dataset**:
   - Synthetic healthcare dataset simulating clinical notes and outcomes
2. **Preprocessing**:
   - Lowercasing, stopword removal, punctuation cleaning
   - Lemmatization with `nltk`
3. **Feature Extraction**:
   - `CountVectorizer` and `TF-IDF` for basic representations
   - `Word2Vec` (gensim) for semantic embedding
4. **Modeling**:
   - Trained and evaluated multiple models including:
     - Logistic Regression
     - Naive Bayes
     - Random Forest
     - XGBoost
     - K-Nearest Neighbors
5. **Evaluation**:
   - Used confusion matrix, classification report, and ROC-AUC

---

## 🚀 Getting Started

```bash
# 1. Clone the Repository
git clone https://github.com/aswinroshanrajendran/healthprompt.git
cd healthprompt

# 2. Create and Activate a Virtual Environment
python -m venv health-env
# On Windows
health-env\Scripts\activate
# On macOS/Linux
source health-env/bin/activate

# 3. Install Dependencies
pip install -r requirements.txt

# 4. Run Notebooks or Scripts
# Open notebooks in Jupyter or run preprocessing/training scripts
```

## 📁 Folder Structure

healthprompt/
│
├── data/
│   └── clinical_notes.csv         # Input dataset
│
├── notebooks/
│   ├── 1_EDA.ipynb                # Exploratory Data Analysis
│   ├── 2_Preprocessing.ipynb      # Text cleaning & preparation
│   ├── 3_Model_Training.ipynb     # ML training and evaluation
│
├── models/
│   └── saved_model.pkl            # Trained model (optional)
│
├── utils/
│   ├── text_cleaning.py           # Preprocessing functions
│
├── requirements.txt
└── README.md


