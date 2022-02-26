# simple-mlflow-multistep-workflow

## commands -

* simple workflow execution `with` new conda env
    ```bash
    mlflow run .
    ```

* simple workflow execution `without` new conda env
    ```bash
    mlflow run . --no-conda
    ```

* simple workflow execution `without` new conda env with parameters
    ```bash
    mlflow run . -P param=value --no-conda
    ```

* run only entry point 
    ```bash
    mlflow run . -e entry_point_name
    ```