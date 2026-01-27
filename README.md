# End-to-End House Price Prediction ML Project

This is a complete machine learning pipeline designed to predict house prices using structured data. The project follows industry best practices with a modular architecture and organized workflow stages.

## Project Overview

The project implements a data science workflow with distinct phases: data ingestion, validation, preprocessing, model training, and evaluation. It uses MLflow for experiment tracking and scikit-learn for machine learning algorithms.

## Key Features

- **Modular Architecture**: Organized components for each ML pipeline stage
- **Configuration-Driven**: YAML-based configuration management for easy parameter tuning
- **Structured Data Flow**: Separate handling of features and target variables
- **End-to-End Pipeline**: Complete workflow from raw data to model evaluation
- **Experiment Tracking**: MLflow integration for tracking model performance and versioning

## Project Structure

```
End_to_end_House_price_predicton_MLproject/
├── config/
│   ├── config.yaml          # Main configuration file
│   ├── params.yaml          # Model parameters
│   └── schema.yaml          # Data schema definitions
├── data/
│   └── raw/
│       ├── data.csv         # Features dataset
│       └── output.csv       # Target variable dataset
├── src/
│   └── House_price_prediction/
│       ├── componants/      # Processing components
│       │   ├── data_ingestion.py
│       │   ├── data_validation.py
│       │   ├── data_preproccessing.py
│       │   ├── model_training.py
│       │   └── model_evaluation.py
│       ├── configurtion/    # Configuration management
│       │   └── config.py
│       ├── entity/          # Data entity definitions
│       │   └── config_entity.py
│       └── pipeline/        # Pipeline stages
│           ├── stage01_data_ingestion.py
│           ├── stage02_data_validation.py
│           ├── stage03_data_preproccessing.py
│           ├── stage04_model_training.py
│           └── stage05_model_evaluation.py
├── artifacts/               # Generated outputs
├── logs/                    # Logging directory
├── setup.py                 # Package setup
├── requierments.txt         # Project dependencies
└── template.py              # Template utilities
```

## Installation

1. **Clone the repository** or navigate to the project directory

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv house_env
   source house_env/Scripts/activate  # On Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requierments.txt
   ```

4. **Install the project package**:
   ```bash
   pip install -e .
   ```

## Usage

Run the complete pipeline:

```bash
python main.py
```

Or run individual pipeline stages:

```bash
python src/House_price_prediction/pipeline/stage01_data_ingestion.py
python src/House_price_prediction/pipeline/stage02_data_validation.py
python src/House_price_prediction/pipeline/stage03_data_preproccessing.py
python src/House_price_prediction/pipeline/stage04_model_training.py
python src/House_price_prediction/pipeline/stage05_model_evaluation.py
```

## Tech Stack

- **Python 3.x**: Core programming language
- **scikit-learn**: Machine learning algorithms
- **pandas**: Data manipulation and analysis
- **PyYAML**: Configuration management
- **MLflow**: Experiment tracking and model registry
- **joblib**: Model serialization

## Pipeline Stages

### Stage 1: Data Ingestion
- Loads features and target variables from raw data files
- Splits data into training and testing sets
- Saves processed data to artifacts directory

### Stage 2: Data Validation
- Validates data against schema definitions
- Checks for missing values and data types
- Ensures data quality before processing

### Stage 3: Data Preprocessing
- Handles missing values
- Performs feature scaling and normalization
- Encodes categorical variables
- Prepares data for model training

### Stage 4: Model Training
- Trains machine learning models
- Performs hyperparameter tuning
- Saves trained models using joblib
- Logs experiments with MLflow

### Stage 5: Model Evaluation
- Evaluates model performance on test set
- Calculates metrics (R², MSE, MAE, etc.)
- Generates evaluation reports
- Compares multiple models

## Configuration

All configurations are managed through YAML files in the `config/` directory:

- **config.yaml**: Data paths and directory configurations
- **params.yaml**: Model hyperparameters
- **schema.yaml**: Data schema and validation rules

## Logging

Comprehensive logging is implemented throughout the pipeline for:
- Debugging
- Monitoring pipeline execution
- Tracking data transformations
- Recording model training progress

Logs are stored in the `logs/` directory.

## Use Case

Ideal for building predictive models for real estate pricing with emphasis on:
- Reproducibility
- Maintainability
- Production-ready best practices
- Scalability

## Output Artifacts

The pipeline generates the following artifacts:

- Preprocessed training and test datasets
- Trained model files
- Model evaluation metrics and reports
- Experiment tracking data (MLflow)

## License

[Add your license information here]

## Contact

For questions or issues, please reach out to the project maintainer.

---

**Note**: Ensure all configuration files are properly set up before running the pipeline.
