## Models
    standard format to package machine learning model in reuseable format allowing models to be easily deployable to various environment

### Storage Format
    - how model is packaged and saved
    - models, metadata of model
    - support multiple formats
### Model Signature
    - Specifies input, outputs data types and shapes that the model expects
    - generates Rest API for model

### Model API
    - Rest API providing standardized Interface for interactive model
    - Can we deployed to various environments

### Falvor
    - specify way of serializing and storing machine learning model
    

## Model Signature
    Way to describe input, output data types and shpaes that are expected as input and produced by a
    machine learning model

    Input example a sample input representative type of data

    Column based
        - Each column input data is treated as seperate feature
    Tensor based
        - Organizing data as multi-dimensional array or tensor

    Model Signature Enforcement is process of defining and validating the input and output schema for machine learning model
    ### Signature Enforcement
    - Inputs provided to the model match the expected signature
    ### Name Ordering enforcement
    - input name provided to model expected input names
    ### Input type enforcement
    - inputs types provided to model match expected inputs

## Model API
    - save_model
        save a model to local file system, 2 flavors Mlflow.sklearn, mlflow.pyfunc
    - log_model
        save model to mlflow server
    - load_model
        loads model for execution