from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_dir_features: Path
    source_dir_target: Path
    train_dir: Path
    test_dir: Path


@dataclass
class DataValidationConfig:
    root_dir: Path
    validation_status_file: Path
    train_dir: Path
    schema_file: Path


@dataclass
class DataPreprocessingConfig:
    root_dir: Path
    preprocessed_train_path: Path
    preprocessed_test_path: Path
    train_dir: Path
    test_dir: Path


@dataclass
class ModelTrainerConfig:
    root_dir: Path
    preprocessed_train_path: Path
    preprocessed_test_path: Path
    model_path: Path
    params_file: Path


@dataclass
class ModelEvaluationConfig:
    root_dir: Path
    preprocessed_test_path: Path
    model_path: Path
    metrics_file: Path
