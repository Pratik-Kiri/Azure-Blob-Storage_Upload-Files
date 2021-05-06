# Azure Blob Storage - Upload Files
 
To upload files on your Azure BlobStorage using Python code follow below steps.

Install these two libraries in your local
# 1. pip install pyyaml
# 2. pip install azure-storage-blob

Create one container with any name inside your Storage Account.
Give that container name inside config.yaml
# file_container_name: "<container_name>"

Get your Storage Account Connection String and paste it into config.yaml
# azure_storage_connectionstring: "<enter your storage account connection string>"
 
Paste the local path of the folder where files are stored, into config.yaml
# source_folder: "<path to the folder of your files to be uploaded>
