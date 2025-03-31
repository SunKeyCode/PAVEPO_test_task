from pathlib import Path

SRC_DIR = Path(__file__).parent.resolve()
PROJECT_DIR = Path(__file__).parents[2].resolve()
FILES_DIR = PROJECT_DIR / "files"

MAIN_PREFIX = "/api/v1"
