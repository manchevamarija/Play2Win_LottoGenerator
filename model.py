from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import StandardScaler

def build_model():
    return Pipeline([
        ("scaler", StandardScaler()),
        ("clf", OneVsRestClassifier(
            LogisticRegression(max_iter=2000, solver="liblinear")
        ))
    ])
