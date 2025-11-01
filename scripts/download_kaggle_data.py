import os
from dotenv import load_dotenv

# Load .env BEFORE importing KaggleApi
dotenv_path = os.path.join(os.path.dirname(__file__), '../.env')
load_dotenv(dotenv_path)

# Now import Kaggle API
from kaggle.api.kaggle_api_extended import KaggleApi

# Authenticate (reads env vars automatically)
api = KaggleApi()
api.authenticate()

# Paths
dataset = 'sriharshaeedala/financial-fraud-detection-dataset'
download_path = os.path.join(os.path.dirname(__file__), '../data')
os.makedirs(download_path, exist_ok=True)

# Download and unzip
api.dataset_download_files(dataset, path=download_path, unzip=True)
print(f"Dataset downloaded to {download_path}")
