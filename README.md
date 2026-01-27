**End-to-End House Price Prediction ML Project**
This is a complete machine learning pipeline designed to predict house prices using structured data. The project follows industry best practices with a modular architecture and organized workflow stages.

**Project Overview**
The project implements a data science workflow with distinct phases: data ingestion, validation, preprocessing, model training, and evaluation. It uses MLflow for experiment tracking and scikit-learn for machine learning algorithms.

**Key Features**
  Modular Architecture: Organized components for each ML pipeline stage
  Configuration-Driven: YAML-based configuration management for easy parameter tuning
  Structured Data Flow: Separate handling of features and target variables
  End-to-End Pipeline: Complete workflow from raw data to model evaluation
  Experiment Tracking: MLflow integration for tracking model performance and versioning
**Project Structure**
  Data Layer: Raw features and target outputs stored in the raw directory
  Configuration: Centralized configs for data paths, model parameters, and schemas
**Source Code:**
  Components for each processing step (ingestion, preprocessing, validation, training, evaluation)
  Configuration management entity definitions
  Multi-stage pipeline orchestration
  Artifacts: Generated outputs including processed datasets and trained models
  Logging: Comprehensive logging for debugging and monitoring
**Tech Stack**
  Python 3.x with scikit-learn for machine learning
  pandas for data manipulation
  PyYAML for configuration management
  MLflow for experiment tracking and model registry
  joblib for model serialization
**Use Cases**
  Ideal for building predictive models for real estate pricing with emphasis on reproducibility, maintainability, and production-ready best practices.
