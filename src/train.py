import joblib
from src.data import load_data, clean_data, get_train_test_split
from src.model import FakeNewsClassifier
from src.config import MODEL_DIR

def main():
    print("Загрузка данных...")
    df = clean_data(load_data())
    X_train, X_test, y_train, y_test = get_train_test_split(df)

    print("Обучение модели...")
    model = FakeNewsClassifier()
    model.train(X_train, y_train)

    joblib.dump(model.model, MODEL_DIR / "fake_news_model.pkl")
    joblib.dump(model.vectorizer, MODEL_DIR / "tfidf_vectorizer.pkl")

    print(f"Модель и векторизатор сохранены в: {MODEL_DIR}")

if __name__ == "__main__":
    main()