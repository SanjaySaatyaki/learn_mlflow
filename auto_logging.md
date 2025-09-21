this is a feature enables automatic logging of certain parameters, metrics, artifacts
Two ways:
- Generic Autologging method: mlflow.autolog()
- Library specific autolog : mlflow.<lib>.autolog()

mlflow.autolog()
- log_models: whether to log model or not
- log_input_examples: True to log the input examples - if log_models set to true
- log_model_signature: Boolean I/P and O/P of the model -if log_models set to true
- log_datasets: Boolean
- disable: Set to true to disable all the automatic loggin
- exclusive: 
- disable_for_unsupported_version
- silent: Suppress event logs

mlflow.sklearn.autolog()
- max_tuning_runs: Set maximum number of child mlflow runs default =5
- log_post_training_metrics: Set to True to log post training
- serialization_format: specify the serialization model artifact when the trained model is saved
- pos_label: positive label in binary classification
