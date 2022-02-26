import mlflow
import argparse

def main(training=True):
    with mlflow.start_run() as run:
        if training:
            print("###### Training ######")
            mlflow.run(".", "stage_01", use_conda=False)
            mlflow.run(".", "stage_02", use_conda=False)
            mlflow.run(".", "stage_03", use_conda=False)
        else:
            print("###### Predicting ######")
            mlflow.run(".", "stage_01", use_conda=False)
            mlflow.run(".", "stage_03", use_conda=False)


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--training", "-t",type=int , default=1)
    parsed_args = args.parse_args()
    print(f">>>>>>> parsed_args.training {type(parsed_args.training)} {parsed_args.training}")
    main(training=bool(parsed_args.training))