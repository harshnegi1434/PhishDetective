# Commands (Azure CLI)

## To login into Azure CLI
```bash
az login --use-device-code
```

## To create a Resource Group
```bash
az group create --name <resource-group-name> --location <azure-region>
```
## To create a Azure Container Registry
```bash
az acr create --resource-group <resource-group-name> --name <registry-name> --sku <sku-name> --location <azure-region>
```

## To build a Docker image and tag inside the ACR
```bash
docker build -t <registry-name.azurecr.io>/<image-name:image-tag> . 
```

## To push an image into Azure Container Registry
```bash
docker push <registry-name.azurecr.io>/<image-name:image-tag>
```

## To create a Azure Container Instance (Single Container)
```bash
az container create \
  --resource-group <resource-group-name> \
  --name <container-instance-name> \
  --image <registry-name.azurecr.io>/<image-name:image-tag> \
  --ports <specify-port-number> \
  --dns-name-label <dns-name-label> \
  --location <location>
```

## To check the status of the Container Instance
```bash
az container show --resource-group <resource-group-name> --name <container-instance-name> --output table
```

## To check the logs of a particular containers
```bash
az container logs --resource-group <resource-group-name>  --name <container-instance-name> --container-name <container-name>
```

## To restart the containers
```
az container restart --resource-group <resource-group-name> --name <container-instance-name>
```

## To access the FQDN (Full Qualified Domain Name) of the container
```bash
az container show --resource-group <resource-group-name> --name <container-instance-name> --query ipAddress.fqdn
```