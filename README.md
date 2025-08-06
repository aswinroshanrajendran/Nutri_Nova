# 🥦 NutriNova - Food Product Nutrition Analysis & Classification

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Data-Pandas-green?logo=pandas)
![Scikit-learn](https://img.shields.io/badge/ML-Scikit--learn-yellow?logo=scikitlearn)
![License](https://img.shields.io/badge/License-MIT-green)

**NutriNova** is a Data Science project that explores nutritional information from food products and performs analytical and predictive tasks such as **nutritional grade classification**, **data cleaning**, and **product insights discovery**. This project uses the **Open Food Facts** dataset and leverages key Python libraries to process, visualize, and model the data.

> 🍽️ Inspired by food tech, 🔍 driven by data, and 📊 powered by machine learning.

---

## 🌟 Project Highlights

- End-to-end data pipeline: ingestion → cleaning → analysis → modeling
- Comprehensive **Exploratory Data Analysis (EDA)** to uncover trends and correlations
- Handled missing data, outliers, and unknown labels effectively
- Classification of food products based on their **nutrition grade (a to e)**
- Normalized and balanced label distribution for fair modeling
- Trained and evaluated multiple ML models using cross-validation and visual tools

---

## 🛠 Tech Stack

- **Language**: Python 3.10+
- **Libraries**: 
  - `pandas`, `numpy`, `matplotlib`, `seaborn`
  - `scikit-learn`, `xgboost`, `lightgbm`
- **IDE**: Jupyter Notebook, VS Code
- **Version Control**: Git + GitHub

---

## 🧠 How It Works

1. **Dataset**:
   - Based on the [Open Food Facts](https://world.openfoodfacts.org/) dataset
   - Contains nutrition information of thousands of food products globally

2. **Data Cleaning & Preprocessing**:
   - Removed irrelevant and duplicate entries
   - Filtered to retain meaningful columns like `energy_100g`, `fat_100g`, `sugars_100g`, etc.
   - Removed entries with `"unknown"` nutrition grades
   - Scaled numerical features using `StandardScaler`
   - Label counts:
     ```
     Grade counts:
     a    39946
     b    38561
     c    52288
     d    71660
     e    49563
     ```

3. **EDA (Exploratory Data Analysis)**:
   - Visualized distribution of nutrition grades
   - Correlation heatmaps to identify feature impact on grades
   - Analyzed outliers and skewed nutrient values

4. **Feature Engineering**:
   - Selected features influencing nutritional quality: energy, fats, sugars, salt, etc.
   - Normalized input values for ML modeling

5. **Modeling**:
   - Trained multiple ML classifiers:
     - Logistic Regression
     - Random Forest
     - XGBoost
     - LightGBM
     - K-Nearest Neighbors
   - Evaluation:
     - Accuracy
     - Confusion Matrix
     - Precision, Recall, F1-score
     - Cross-validation

---

## 🚀 Getting Started

```bash
# 1. Clone the Repository
git clone https://github.com/yourusername/nutrinova.git
cd nutrinova

# 2. Create and Activate a Virtual Environment
python -m venv nutri-env
# On Windows
nutri-env\Scripts\activate
# On macOS/Linux
source nutri-env/bin/activate

# 3. Install Dependencies
pip install -r requirements.txt

# 4. Launch Notebooks
jupyter notebook
```

## 📊 Insights
Products with grades D and E had significantly higher sugar, salt, and saturated fat levels

Grade A products were generally low in processed ingredients and often plant-based

Feature scaling and class balancing helped reduce model bias

## 🔮 Future Enhancements
Add Streamlit dashboard for interactive model use

Incorporate product image data using CNNs

Real-time food label scanner using mobile interface + OCR

Nutrition-based health recommendation system

## 📜 License
This project is open-source and available under the MIT License.

## 🙋‍♂️ About Me
Aswin Roshan Rajendran
🎓 Master’s in Data Science & Analytics, EPITA Paris
📧 aswinroshan17@gmail.com
📍 Paris, France
🔗 LinkedIn | GitHub
