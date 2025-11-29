DATA_URL = 'https://storage.yandexcloud.net/academy.ai/practica/fake_news.csv'

# Гиперпараметры
TFIDF_PARAMS = {
    'stop_words': 'english'
}

MODEL_PARAMS = {
    'max_iter': 1000,
    'random_state': 42
}


MIN_LENGTH_INPUT_NEWS = 10
MAX_LENGTH_INPUT_NEWS = 200
