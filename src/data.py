import pandas as pd
from sklearn.model_selection import train_test_split
from src.config import DATA_URL


def load_data():
    """Загружает датасет"""
    print('Загрузка датасета...')
    try:
        df = pd.read_csv(DATA_URL)
        print('Датасет успешно загружен')
        return df
    except Exception as e:
        raise ValueError('Ошибка: {e}')
    

def clean_data(df):
    """Обрабатывает данные"""
    df = df.dropna(subset=['text', 'label'])
    df['label'] = df['label'].map({'FAKE': 0, 'REAL': 1})
    return df


def get_train_test_split(df, test_size=0.2, random_state=42):
    """Разделяет данные на train/test с сохранением баланса."""
    X, y = df['text'], df['label']
    return train_test_split(X, y, test_size=test_size, random_state=random_state, stratify=y)