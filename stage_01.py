import mlflow

text = "input 01"

with open("artifacts01.txt", "w") as f:
    f.write(text)
mlflow.log_artifact("artifacts01.txt", artifact_path="features")