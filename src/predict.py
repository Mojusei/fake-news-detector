import sys
import joblib
from pathlib import Path
from config.paths import MODEL_DIR

# Добавляем корень проекта в sys.path для запуска напрямую
PROJECT_ROOT = Path(__file__).parent.parent.resolve()
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

MODEL_PATH = MODEL_DIR / 'fake_news_model.pkl'
VEC_PATH = MODEL_DIR / 'tfidf_vectorizer.pkl'

if not MODEL_PATH.exists():
    raise FileNotFoundError(f"Модель по пути {MODEL_PATH} не найдена")
if not VEC_PATH.exists():
    raise FileNotFoundError(f"Векторизатор по пути {VEC_PATH} не найден")

_model = joblib.load(MODEL_PATH)
_vectorizer = joblib.load(VEC_PATH)


def predict_news(text: str) -> str:
    """Предсказывает, фейк или реальная новость."""
    vectorized = _vectorizer.transform([text])
    prediction = _model.predict(vectorized)[0]
    return "REAL" if prediction == 1 else "FAKE"


def main_cli():
    """Точка входа"""
    if len(sys.argv) != 2:
        print('Неверное количество аргументов')
        print('Используйте: fake-news-predict \"Текст новости\"')
        sys.exit(1)

    news_text = sys.argv[1]
    try:
        result = predict_news(news_text)
        print(f"Результат: {result}")
    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main_cli()
