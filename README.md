# Macroeconomic Stability & Well-Being Analytics

🔍 Project Overview

- This project analyzes the relationship between macroeconomic indicators and population well-being, with the focus on identifying countries at risk of low happiness levels.
- The core objective is to quantify and predict “Happiness Risk” using economic and social indicators such as inflation, freedom, and corruption perception.
- The project also integrates a Generative AI-powered chatbot capable of answering questions related to happiness scores, inflation trends, macroeconomic indicators, and model insights using a custom knowledge base.

🎯 Objectives

- Analyze global trends in happiness and inflation
- Identify key factors impacting well-being
- Classify countries into High, Medium, and Low risk categories
- Build a machine learning model to predict happiness risk
- Develop an interactive app for real-time predictions and insights
- Implement a GenAI chatbot for intelligent question-answering on macroeconomic and well-being analytics

📁 Dataset Description

The project uses a combined dataset derived from:

- World Happiness Report data
- Global inflation metrics

Key Features:

- Country – Nation name
- Happiness Score – Overall well-being indicator
- Inflation Rate (CPI) – Economic stability proxy
- Freedom to Make Life Choices – Social indicator
- Perceptions of Corruption – Governance quality
- Social Support, GDP, Life Expectancy – Supporting variables

⚙️ Methodology

- Exploratory Data Analysis (EDA)
- Distribution analysis of happiness scores and inflation
- Correlation analysis between economic and social factors
- Country-level comparisons and trend identification
- Feature Engineering
- Created Happiness Risk Categories:
- High Risk
- Medium Risk
- Low Risk
- Handled missing values and normalized key variables
- Selected relevant predictors based on correlation and domain logic
- Modeling
- Implemented Random Forest classifier.
- Trained a model to predict categorical happiness risk.
- Split data into training and testing sets.
- Generative AI Integration
- Developed a GenAI chatbot using a custom knowledge base
- Enabled natural language question-answering related to macroeconomic and well-being indicators
- Integrated Retrieval-Augmented Generation (RAG)-based workflow for contextual responses
- Connected chatbot interface within the Streamlit application

🤖 Model Details & Evaluation

Model: Random Forest Classifier
- Type: Multi-class classification

Evaluation Metrics:

- Accuracy Score,
- Confusion Matrix,
- Classification Report (Precision, Recall, F1-score)

Outcome:

- The model achieved strong classification performance in distinguishing risk categories
- Feature importance analysis revealed key drivers of happiness risk
- The GenAI chatbot improved accessibility of insights through conversational interaction

💻 Streamlit App Features

- Built using Streamlit for interactive deployment.

Key Functionalities:

🔮 Prediction Tool

- Input country-level indicators
- Outputs predicted happiness risk

📊 Feature Importance Visualization

- Highlights the most influential variables

🧠 Interpretation Layer

- Explains why a prediction was made

🏛️ Policy Recommendations

- Suggests actionable improvements based on inputs

🤖 GenAI Chatbot

- Answers user queries related to happiness scores, inflation, and macroeconomic indicators
- Provides contextual responses using project knowledge base
- Enables conversational exploration of economic insights

📈 Key Insights & Findings

- Higher inflation is generally associated with increased happiness risk
- Freedom and social support strongly reduce risk levels
- Perceived corruption negatively impacts well-being
- Economic indicators alone are insufficient — social factors play a critical role
- Conversational AI improves accessibility and interpretability of analytical insights

⚠️ Challenges & Limitations

- Limited dataset size reduces generalization capability
- Risk categorization is based on thresholds (subject to bias)
- The model does not capture temporal (time-series) effects
- External geopolitical factors are not included
- GenAI responses depend on the quality and scope of the knowledge base

🚀 Future Improvements

- Incorporate time-series analysis for trend prediction
- Experiment with advanced models (XGBoost, Gradient Boosting)
- Expand the dataset with more countries and years
- Deploy app on cloud (AWS / Streamlit Cloud)
- Add explainability tools like SHAP for deeper insights
- Enhance chatbot with advanced LLMs and real-time economic data integration

🛠️ Tech Stack

Programming: Python
- Libraries: pandas, numpy, matplotlib, seaborn, scikit-learn
- Visualization: Power BI / matplotlib / seaborn
- App Framework: Streamlit
- Modeling: Random Forest
- Generative AI: Ollama, Phi LLM, Retrieval-Augmented Generation (RAG)
- NLP Components: Custom Knowledge Base, Prompt Engineering

📌 Conclusion

- This project combines data analytics, machine learning, and Generative AI to analyze the relationship between macroeconomic stability and human well-being. By integrating predictive modeling with a conversational AI interface, the solution enables users to explore economic insights, understand happiness risk factors, and interact with data in a more accessible and intelligent way.

The project demonstrates practical skills in:

- Exploratory Data Analysis (EDA)
- Machine Learning Classification
- Feature Engineering
- Streamlit Application Development
- Retrieval-Augmented Generation (RAG)
- AI-powered Insight Delivery
