#!/bin/bash
DATA_DIR=$1

# dvc init

dvc remote add -d $DATA_DIR gdrive://$ROOT_KEY/$DATA_DIR
dvc remote modify $DATA_DIR gdrive_acknowledge_abuse true

dvc remote modify $DATA_DIR gdrive_client_id 'client-id'
dvc remote modify $DATA_DIR gdrive_user_credentials_file $SECRET_PATH/gdrive-client-key.json

dvc config core.hardlink_lock true

dvc remote modify $DATA_DIR gdrive_use_service_account true
dvc remote modify $DATA_DIR gdrive_service_account_json_file_path $SECRET_PATH/gdrive-service-key.json

dvc config core.autostage true
dvc fetch
dvc pull

dvc add $DATA_DIR/*

dvc push

dvc status -c
