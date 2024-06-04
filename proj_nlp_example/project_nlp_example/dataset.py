from pathlib import Path


from project_nlp_example.config import PROCESSED_DATA_DIR, RAW_DATA_DIR


def load_data(file_path):
    raise NotImplementedError


def get_latest_data(df_dynamic_frame):
    raise NotImplementedError


def get_dynamic_frame():
    raise NotImplementedError


def get_communications():
    raise NotImplementedError

