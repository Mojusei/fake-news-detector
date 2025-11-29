from pathlib import Path


# Путь до проекта
PROJECT_ROOT = Path(__file__).parent.parent.resolve()

# Пути до важных папок
MODEL_DIR = PROJECT_ROOT / 'models'
REPORTS_DIR = PROJECT_ROOT / 'reports'


# Создание папок
MODEL_DIR.mkdir(exist_ok=True)
REPORTS_DIR.mkdir(exist_ok=True)
