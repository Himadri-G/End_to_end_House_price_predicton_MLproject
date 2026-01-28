import os
import logging
from pathlib import Path

Project_name = "House_price_prediction"

log_dir = "logs"
log_file = "project_setup.log"

os.makedirs(log_dir , exist_ok=True)

logging.basicConfig(
    filename = os.path.join(log_dir , log_file ) , level = logging.INFO , format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)
logger = logging.getLogger(__name__)

list_of_files = [
    f"src/{Project_name}/__init__.py", 
    f"src/{Project_name}/entity/__init__.py", 
    f"src/{Project_name}/entity/config_entity.py", 
    f"src/{Project_name}/configurtion/__init__.py ", 
    f"src/{Project_name}/configurtion/config.py ", 
    f"src/{Project_name}/componants/__init__.py ", 
    f"src/{Project_name}/componants/data_ingestion.py ", 
    f"src/{Project_name}/componants/data_validation.py ", 
    f"src/{Project_name}/componants/data_preproccessing.py ", 
    f"src/{Project_name}/componants/model_training.py ", 
    f"src/{Project_name}/componants/model_evaluation.py ", 
    f"src/{Project_name}/pipeline/__init__.py ",
    f"src/{Project_name}/pipeline/stage01_data_ingestion.py ", 
    f"src/{Project_name}/pipeline/stage02_data_validation.py ",  
    f"src/{Project_name}/pipeline/stage03_data_preproccessing.py ",
    f"src/{Project_name}/pipeline/stage04_model_training.py ", 
    f"src/{Project_name}/pipeline/stage05_model_evaluation.py ",  
    "config/config.yaml",
    "config/params.yaml",
    "setup.py"
]

if __name__ == "__main__" :
    for file_name in list_of_files:
        file_name = Path(file_name)
        file_dir = file_name.parent
        
        if(file_dir and not file_dir.exists()):
            file_dir.mkdir(parents=True , exist_ok=True)
            
            logger.info(f"{file_dir} dir is created !!")
        
        if(not file_name.exists()):
            file_name.touch()
            logger.info(f"{file_dir} file is created !!")
                
