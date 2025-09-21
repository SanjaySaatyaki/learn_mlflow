Centralized repository for storing metadata and artifacts
- Storage - store aritfacts, metadata during training process
    - backend stores
        - file store
        - DB Store
    - artifact stores
- Networking - 
    - Rest API
        Acess tracking server over HTTP
    - RPC
        Uses gRPC
    - Proxy access
        For artifacts

mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlflow-artifacts --host 127.0.0.1 --port 5000

