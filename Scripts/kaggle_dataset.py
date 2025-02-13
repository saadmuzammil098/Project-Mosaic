import os
from kaggle.api.kaggle_api_extended import KaggleApi

#Authenticate Kaggle API
api = KaggleApi()
api.authenticate()

#Define dataset
DATASET_NAME = "prasad22/healthcare-dataset"

#Get the current script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

#Download the dataset to the same directory as this script
print("Downloading dataset...")
api.dataset_download_files(DATASET_NAME, path=script_dir, unzip=True)

print(f"Dataset '{DATASET_NAME}' downloaded successfully into '{script_dir}'!")
