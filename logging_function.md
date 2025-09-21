### set_tracking_uri()
    set default tracking URI for current Run
    - uri - location where files can be stored
        - empty string - automatically creates mlrun folder and stores all your tracks
        - folder name - Folder name of your choice
        - file path - full path of your system in format
        - remote path - https://my-tracking-server:500
        - databricks workspace 

### get_tracking_uri 
    Retrive tracking uri
    -  No inputs
    - Gives the tracking uri

### create_experiment 
    Creates Fresh new experiment
    Returns experiment id
    Parameters
    - name - custom name must be unique and case sensitive
    - artifact_location - location to store artifact folder in a specific location
    - tags -  specify tags on experiments


### set_experiment 
    set already created experiment if not avialable it will try to create.
    Parameters:
    - experiment_name: already exisiting name
    - experiment_id: If not avialble it will return error
    Returns:
        Instance of mlflow.entities.Experiments

### start_run
    starts a new mlflow run with all entities will be logged
    Parameters:
    - run_id : used for utitlizing exisiting run
    - experiment_id: specifies id of experiment where it should execute in run, cant be used if run_id is defined
    - run_name: name of a new run. cant be used if run_id is defined
    - nested: runs as nested run. specify argument as True
    - tags: key and values
    - description: Populates description
    Returns:
    - mlFlow.ActiveRun

### active_run()
    gives current active run

### last_active_run()
    returns recently active run

### log_param and log_params
    - single and multiple parameters
        - key - Alphanumeric string
        - value - Value of parameter which is used in model
    - params -> Dict <key,value>

### log_metric and log_metrics
    - Single and multiple metrics
        - key, value, step

### log_artifact and log_artifacts
    - Output like model, dataset, etc
    Parameters:
        - local_path: - Path of the file to be stored
        - artifact_path: - Path to store the artifacts
    

### get_artifact_uri
    - get absolute URI specified artifact