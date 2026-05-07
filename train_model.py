import pandas as pd
import pickle
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report


# -----------------------------
# 1. Load data
# -----------------------------
df = pd.read_csv('data/WHI_Inflation.csv')


# -----------------------------
# 2. Create risk_level (IMPORTANT)
# -----------------------------
def assign_risk(score):
    if score < 4:
        return "High Risk"
    elif score < 6:
        return "Medium Risk"
    else:
        return "Low Risk"

df['risk_level'] = df['Score'].apply(assign_risk)


# -----------------------------
# 3. Select ONLY required features
# -----------------------------
FEATURES = [
    "Headline Consumer Price Inflation",
    "Freedom to make life choices",
    "Perceptions of corruption"
]

df = df.dropna(subset=FEATURES + ['risk_level'])

X = df[FEATURES]
y = df['risk_level']


# -----------------------------
# 4. Train-test split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# -----------------------------
# 5. Train model
# -----------------------------
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    class_weight='balanced'
)

model.fit(X_train, y_train)


# -----------------------------
# 6. Evaluate
# -----------------------------
print("\n📊 Model Performance:\n")
print(classification_report(y_test, model.predict(X_test)))


# -----------------------------
# 7. Save model
# -----------------------------
os.makedirs('model', exist_ok=True)

with open('model/model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("\n✅ Model trained and saved successfully!")