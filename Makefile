deploy:
	gcloud run deploy "webhook" --source . --env-vars-file="./env_prod.json" --region="southamerica-east1"