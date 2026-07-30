from pathlib import Path

# Project Root
BASE_DIR = Path(file).resolve().parent.parent

# Data folders
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
DATABASE_DIR = DATA_DIR / "database"

# Reports
REPORTS_DIR = BASE_DIR / "reports"

# Logs
LOGS_DIR = BASE_DIR / "logs"

# Database
DATABASE_NAME = "nse_alpha.db"

# Market Timings
MARKET_OPEN = "09:15"
MARKET_CLOSE = "15:30"

print("Configuration Loaded Successfully")
