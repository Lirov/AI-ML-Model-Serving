from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from joblib import dump
from pathlib import Path

DATA = [
    ("I love this product, it’s amazing!", 1),
    ("Totally worth the price.", 1),
    ("Works great and super fast.", 1),
    ("This is awful, don’t buy it.", 0),
    ("Worst experience ever.", 0),
    ("It broke after two days.", 0),
    ("Fantastic quality and service!", 1),
    ("Terrible quality, very disappointed.", 0)
]

def train_and_save(model_path: str = "app/model/model.joblib"):
    texts, labels = zip(*DATA)
    pipe = Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1,2))),
        ("clf", LogisticRegression(max_iter=1000))
    ])
    pipe.fit(texts, labels)
    Path("app/model").mkdir(parents=True, exist_ok=True)
    dump(pipe, model_path)
    print(f"Saved model to {model_path}")

if __name__ == "__main__":
    train_and_save()
