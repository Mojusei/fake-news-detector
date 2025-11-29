from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from config.globals import TFIDF_PARAMS, MODEL_PARAMS


class FakeNewsClassifier:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(**TFIDF_PARAMS)
        self.model = PassiveAggressiveClassifier(**MODEL_PARAMS)
        self.is_fitted = False

    def train(self, X_train, y_train):
        """Обучает векторизатор и модель."""
        X_train_vec = self.vectorizer.fit_transform(X_train)
        self.model.fit(X_train_vec, y_train)
        self.is_fitted = True

    def predict(self, X):
        """Предсказывает метки для списка текстов."""
        if not self.is_fitted:
            raise ValueError("Модель не обучена! Вызовите .train() сначала.")
        X_vec = self.vectorizer.transform(X)
        return self.model.predict(X_vec)

    def predict_proba_score(self, X):
        """Возвращает сырые оценки уверенности (для ROC и т.д.)."""
        X_vec = self.vectorizer.transform(X)
        return self.model.decision_function(X_vec)
