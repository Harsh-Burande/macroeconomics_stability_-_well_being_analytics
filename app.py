from rag.knowledge_base import load_knowledge_base
from rag.chatbot import chatbot
from rag.embedding import create_index

import streamlit as st
from utils.predict import predict_risk

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Macroeconomic Stability & Well-Being",
    layout="wide"
)

# -----------------------------
# Load RAG System (Cached)
# -----------------------------
@st.cache_resource
def load_rag_system():
    kb = load_knowledge_base()
    index = create_index(kb)
    return kb, index

kb, index = load_rag_system()

# -----------------------------
# Sidebar Navigation
# -----------------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Overview", "Insights", "Prediction Tool", "AI Chatbot"]
)

# -----------------------------
# 1. OVERVIEW
# -----------------------------
if page == "Overview":
    st.title("🌍 Macroeconomic Stability & Well-Being Analytics")

    st.write("""
    This project analyzes how economic and social factors influence a country's happiness and stability.

    Key objectives:
    - Understand impact of inflation on happiness
    - Analyze global well-being trends
    - Predict happiness risk levels
    """)

    st.subheader("📌 Key Factors")
    st.markdown("""
    - Inflation (Economic stability)
    - Freedom to make life choices
    - Perception of corruption
    """)

# -----------------------------
# 2. INSIGHTS
# -----------------------------
elif page == "Insights":
    st.title("📊 Key Insights")

    st.subheader("🔍 Findings from Analysis")

    st.markdown("""
    - Countries with high inflation volatility tend to have higher risk levels  
    - Freedom and corruption are stronger predictors than inflation alone  
    - Economic instability affects well-being, but social factors dominate  
    """)

    st.subheader("💡 Conclusion")

    st.info("""
    A hybrid approach combining economic and social indicators gives the best prediction performance.
    """)

# -----------------------------
# 3. PREDICTION TOOL
# -----------------------------
elif page == "Prediction Tool":

    st.title("🤖 Happiness Risk Prediction")

    country = st.text_input("Country Name (optional)", "Sample Country")

    col1, col2 = st.columns(2)

    with col1:
        inflation = st.slider("Headline Consumer Price Inflation", -2.0, 10.0, 3.0)
        freedom = st.slider("Freedom to make life choices", 0.0, 1.0, 0.5)

    with col2:
        corruption = st.slider("Perceptions of corruption", 0.0, 0.8, 0.3)

    if st.button("Predict Risk"):

        input_data = {
            "Country": country,
            "Headline Consumer Price Inflation": inflation,
            "Freedom to make life choices": freedom,
            "Perceptions of corruption": corruption
        }

        result, confidence, feature_importance = predict_risk(input_data)

        st.session_state["result"] = result
        st.session_state["confidence"] = confidence
        st.session_state["feature_importance"] = feature_importance
        st.session_state["input_data"] = input_data

    if "result" in st.session_state:

        result = st.session_state["result"]
        confidence = st.session_state["confidence"]
        feature_importance = st.session_state["feature_importance"]
        input_data = st.session_state["input_data"]

        inflation = input_data["Headline Consumer Price Inflation"]
        freedom = input_data["Freedom to make life choices"]
        corruption = input_data["Perceptions of corruption"]
        country = input_data["Country"]

        if inflation > 8 or corruption > 0.7:
            st.warning("⚠️ Extreme input values. Prediction may be less reliable.")

        st.subheader("Prediction Result")

        if result == "High Risk":
            st.error(f"⚠️ {result}")
        elif result == "Medium Risk":
            st.warning(f"⚠️ {result}")
        else:
            st.success(f"✅ {result}")

        st.write(f"🔍 Confidence Score: {confidence:.2f}")

        st.divider()

        st.markdown(f"### 📌 Interpretation for **{country}**")

        st.write(f"""
        - Inflation: **{inflation:.2f}%**
        - Freedom: **{freedom:.2f}**
        - Corruption: **{corruption:.2f}**
        """)

        st.divider()

        st.markdown("### 🔍 Feature Importance")

        sorted_features = sorted(feature_importance.items(), key=lambda x: x[1], reverse=True)

        for feature, importance in sorted_features:
            st.write(f"{feature}: {importance:.2f}")

# -----------------------------
# 4. AI CHATBOT
# -----------------------------
elif page == "AI Chatbot":

    st.title("🤖 Macroeconomic AI Chatbot")

    # Initialize chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # User input
    query = st.text_input("Ask a question")

    # Ask button
    if st.button("Ask"):

        if query:

            # Generate response
            answer = chatbot(query, kb, index)

            # Store conversation
            st.session_state.chat_history.append(
                {
                    "question": query,
                    "answer": answer
                }
            )

    # Display chat history
    for chat in st.session_state.chat_history:

        st.markdown(f"### 🧑 User:")
        st.write(chat["question"])

        st.markdown(f"### 🤖 AI:")
        st.write(chat["answer"])

        st.divider()

    # Clear chat button
    if st.button("Clear Chat"):
        st.session_state.chat_history = []
        st.rerun()