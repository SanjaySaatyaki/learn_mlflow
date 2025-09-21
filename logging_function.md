set_tracking_uri - set default tracking URI for current Run
    - uri - location where files can be stored
        - empty string - automatically creates mlrun folder and stores all your tracks
        - folder name - Folder name of your choice
        - file path - full path of your system in format
        - remote path - https://my-tracking-server:500
        - databricks workspace 

get_tracking_uri - Retrive tracking uri
    -  No inputs
    - Gives the tracking uri
    