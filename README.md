# AWS Cost Projections
Repository to store scripts that help estimate AWS costs

## S3_Cost_Projections
### Usage:
`python3 S3_Cost_Projections.py <INITIAL_BUCKET_SIZE> <DAILY_INPUT> <DAILY_OUTPUT> <DAYS_TO_RUN>`

where:
- INITIAL_BUCKET_SIZE : the initial size of the bucket contents (GB)
- DAILY_INPUT : estimated volume of data being added daily (GB)
- DAILY_OUTPUT : estimated volume of data being removed daily (GB)
- DAYS_TO_RUN : number of days to simulate 
