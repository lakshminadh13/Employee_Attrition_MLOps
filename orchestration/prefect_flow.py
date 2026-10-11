from prefect import flow, task
import subprocess
import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent


@task(name="Train Employee Attrition Model")
def train_model():
    print("Starting model training...")
    result = subprocess.run(
        [sys.executable, "src/train.py"],
        cwd=PROJECT_DIR,
        check=True
    )
    print("Model training completed successfully.")


@task(name="Verify Project Files")
def verify_files():
    required_files = [
        "Dockerfile",
        "compose.yaml",
        "requirements.txt",
        "src/train.py"
    ]

    for file in required_files:
        if not (PROJECT_DIR / file).exists():
            raise FileNotFoundError(f"Missing required file: {file}")
        print(f"Verified: {file}")

    print("Project file verification completed.")


@flow(name="Employee Attrition MLOps Workflow")
def employee_attrition_workflow():
    verify_files()
    train_model()
    print("Prefect workflow completed successfully!")


if __name__ == "__main__":
    employee_attrition_workflow()
