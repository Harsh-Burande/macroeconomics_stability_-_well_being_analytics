def load_knowledge_base():

    kb = []

    # 1. GDP vs Happiness
    kb.append({
        "title": "GDP vs Happiness",
        "content": """
        GDP strongly correlates with happiness (0.74) by improving living standards, healthcare, and economic security. However, happiness gains diminish at higher income levels, showing that social and institutional factors also influence well-being.
        """,
        "tags": ["gdp", "happiness", "economics"],
        "type": "insight"
    })

    # 2. Inflation vs Happiness
    kb.append({
        "title": "Inflation vs Happiness",
        "content": """
        Inflation has a weak overall relationship with happiness, although extreme inflation reduces well-being by increasing financial stress, uncertainty, and loss of purchasing power.
        """,
        "tags": ["inflation", "happiness", "economics"],
        "type": "insight"
    })

    # 3. Key Drivers of Happiness
    kb.append({
        "title": "Key Drivers of Happiness",
        "content": """
        Happiness is mainly influenced by GDP (0.74), health (0.70), social support (0.66), and freedom (0.57). Long-term structural and social factors contribute more to well-being than short-term economic fluctuations.
        """,
        "tags": ["happiness", "drivers", "gdp", "health", "freedom"],
        "type": "insight"
    })

    # 4. Corruption vs Happiness
    kb.append({
        "title": "Corruption vs Happiness",
        "content": """
        Corruption negatively impacts happiness by reducing institutional trust, increasing inequality, and limiting fair access to opportunities. Its correlation with happiness is moderate at approximately 0.44.
        """,
        "tags": ["corruption", "governance", "happiness"],
        "type": "insight"
    })

    # 5. Freedom vs Happiness
    kb.append({
        "title": "Freedom vs Happiness",
        "content": """
        Freedom positively affects happiness (0.57) by allowing individuals to make meaningful life choices, pursue goals, and maintain personal autonomy.
        """,
        "tags": ["freedom", "happiness"],
        "type": "insight"
    })

    # 6. Social Support vs Happiness
    kb.append({
        "title": "Social Support vs Happiness",
        "content": """
        Social support strongly improves happiness (0.66) by providing emotional stability, reducing stress, and strengthening community connections.
        """,
        "tags": ["social_support", "happiness"],
        "type": "insight"
    })

    # 7. Happiness Risk Classification
    kb.append({
        "title": "Happiness Risk Classification",
        "content": """
        Happiness scores were categorized into High, Medium, and Low risk groups. Most countries fall into medium and high-risk categories, indicating uneven global well-being distribution.
        """,
        "tags": ["risk", "classification", "model"],
        "type": "model_insight"
    })

    # 8. Global Summary
    kb.append({
        "title": "Macroeconomic Stability and Well-Being Summary",
        "content": """
        Happiness depends on economic, social, and institutional factors. GDP, health, freedom, and social support positively influence well-being, while corruption and extreme inflation reduce happiness.
        """,
        "tags": ["summary", "economics", "happiness"],
        "type": "summary"
    })

    return kb