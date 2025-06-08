from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
import streamlit as st

def train_model(X, y, model_name, test_size=0.2):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

    if model_name == "Logistic Regression":
        model = LogisticRegression(max_iter=1000)
    elif model_name == "Decision Tree":
        model = DecisionTreeClassifier()
    elif model_name == "Random Forest":
        model = RandomForestClassifier()
    elif model_name == "KNN":
        model = KNeighborsClassifier()
    else:
        st.error("Unsupported model selected")
        return None, None

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    metrics = {
        "Accuracy": accuracy_score(y_test, y_pred),
        "Precision": precision_score(y_test, y_pred, average="weighted", zero_division=0),
        "Recall": recall_score(y_test, y_pred, average="weighted", zero_division=0),
        "F1 Score": f1_score(y_test, y_pred, average="weighted", zero_division=0),
    }

    # Optional: ROC AUC for binary classification only
    if len(set(y)) == 2:
        y_proba = model.predict_proba(X_test)[:,1]
        metrics["ROC AUC"] = roc_auc_score(y_test, y_proba)

    return metrics, model

def evaluate_model(metrics):
    st.write("### Model Evaluation Metrics")
    for metric, value in metrics.items():
        st.write(f"{metric}: {value:.4f}")
