# Macroeconomic Stability & Well-Being Analytics
🔍 Project Overview

This project analyzes the relationship between macroeconomic indicators and population well-being, with the focus on identifying countries at risk of low happiness levels.

The core objective is to quantify and predict “Happiness Risk” using economic and social indicators such as inflation, freedom, and corruption perception.

🎯 Objectives
Analyze global trends in happiness and inflation
Identify key factors impacting well-being
Classify countries into High, Medium, and Low risk categories
Build a machine learning model to predict happiness risk
Develop an interactive app for real-time predictions and insights

📁 Dataset Description

The project uses a combined dataset derived from:

World Happiness Report data
Global inflation metrics
Key Features:
Country – Nation name
Happiness Score – Overall well-being indicator
Inflation Rate (CPI) – Economic stability proxy
Freedom to Make Life Choices – Social indicator
Perceptions of Corruption – Governance quality
Social Support, GDP, Life Expectancy – Supporting variables
⚙️ Methodology
1. Exploratory Data Analysis (EDA)
Distribution analysis of happiness scores and inflation
Correlation analysis between economic and social factors
Country-level comparisons and trend identification
2. Feature Engineering
Created Happiness Risk Categories:
High Risk
Medium Risk
Low Risk
Handled missing values and normalized key variables
Selected relevant predictors based on correlation and domain logic
3. Modeling
Implemented Random Forest classifier
Trained a model to predict categorical happiness risk
Split data into training and testing sets

🤖 Model Details & Evaluation
Model: Random Forest Classifier
Type: Multi-class classification
Evaluation Metrics:
Accuracy Score
Confusion Matrix
Classification Report (Precision, Recall, F1-score)
Outcome:
The model achieved strong classification performance in distinguishing risk categories
Feature importance analysis revealed key drivers of happiness risk

💻 Streamlit App Features

Built using Streamlit for interactive deployment.

Key Functionalities:
🔮 Prediction Tool
Input country-level indicators
Outputs predicted happiness risk
📊 Feature Importance Visualization
Highlights the most influential variables
🧠 Interpretation Layer

Explains why a prediction was made
🏛️ Policy Recommendations
Suggests actionable improvements based on inputs

📈 Key Insights & Findings
Higher inflation is generally associated with increased happiness risk
Freedom and social support strongly reduce risk levels
Perceived corruption negatively impacts well-being
Economic indicators alone are insufficient — social factors play a critical role

⚠️ Challenges & Limitations
Limited dataset size reduces generalization capability
Risk categorization is based on thresholds (subject to bias)
The model does not capture temporal (time-series) effects
External geopolitical factors are not included

🚀 Future Improvements
Incorporate time-series analysis for trend prediction
Experiment with advanced models (XGBoost, Gradient Boosting)
Expand the dataset with more countries and years
Deploy app on cloud (AWS / Streamlit Cloud)
Add explainability tools like SHAP for deeper insights

🛠️ Tech Stack
Programming: Python
Libraries: pandas, numpy, matplotlib, seaborn, scikit-learn
Visualization: Power BI / matplotlib / seaborn
App Framework: Streamlit
Modeling: Random Forest
