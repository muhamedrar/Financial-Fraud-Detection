import os
from kaggle.api.kaggle_api_extended import KaggleApi


def download_kaggle_dataset(dataset_name: str, dest_path: str):
    api = KaggleApi()
    api.authenticate()

    os.makedirs(dest_path, exist_ok=True)

    print(f"Downloading dataset '{dataset_name}' to '{dest_path}'...")
    api.dataset_download_files(dataset_name, path=dest_path, unzip=True)
    print(f"✅ Dataset downloaded and extracted to: {dest_path}")

if __name__ == "__main__":
    dataset_name = "sriharshaeedala/financial-fraud-detection-dataset"
    destination = "/usr/local/airflow/data"

    download_kaggle_dataset(dataset_name, destination)
