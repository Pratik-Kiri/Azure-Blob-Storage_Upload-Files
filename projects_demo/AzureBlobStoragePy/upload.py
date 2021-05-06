import os
import yaml
from azure.storage.blob import ContainerClient

# pyyaml
# azure-storage-blob

def load_config():
	dir_root = os.path.dirname(os.path.abspath(__file__))
	with open(dir_root + "/config.yaml", "r") as yamlfile:
		return yaml.load(yamlfile, Loader=yaml.FullLoader)


def get_files(dir):
	with os.scandir(dir) as entries:
		for entry in entries:
			if entry.is_file() and not entry.name.startswith('.'):
				yield entry


def upload(files, connection_string, container_name):
	container_client = ContainerClient.from_connection_string(connection_string, container_name)
	print("Uploading files to blob storage...")

	for file in files:
		blob_client = container_client.get_blob_client(file.name)
		with open(file.path, "rb") as data:
			blob_client.upload_blob(data, overwrite=True)
			print(f'{file.name} uploaded to blob storage')
			data.close()
			# os.remove(file)
			# print(f'{file.name} removed the folder')

config = load_config()
files = get_files(config["source_folder"]+"/files")
# pictures = get_files(config["source_folder"]+"/pictures")
# print(*pictures)
# print(*videos)
upload(files, config["azure_storage_connectionstring"], config["file_container_name"])
# upload(pictures, config["azure_storage_connectionstring"], config["pictures_container_name"])
