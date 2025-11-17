import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_path = "project_all"

dif_lists = [
    ".github/workflows/.gitkeep",
    f"src/{project_path}/__init__.py",
    f"src/{project_path}/pipeline/__init__.py",
    f"src/{project_path}/pipeline/prediction_pipeline.py",
    f"src/{project_path}/pipeline/prediction_pipeline.py",
    f"src/{project_path}/componets/__init__.py",
    f"src/{project_path}/componets/ingestion.py",
    f"src/{project_path}/componets/transformation.py",
    f"src/{project_path}/componets/model_trainer.py",
    f"src/{project_path}/componets/monitoring.py",
    f"src/{project_path}/logger.py",
    f"src/{project_path}/utils.py",
    f"src/{project_path}/exception.py",
    f"Docker.py",
    f"requiremets.txt",
    f"setup.py",
    f"app.py",
]

for f in dif_lists:
    path = Path(f)
    dir, file = os.path.split(path)
    # print(f)

    if(dir != ""):
        os.makedirs(dir, exist_ok=True)
        logging.info(f"folder created: {dir}")

    if(not os.path.exists(file)):
        with open(f, "w") as f:
            pass
        logging.info(f"empty file created: {file}")