# AWS_Cost_Projections
Repository to store scripts that help you estimate AWS costs

## S3_Cost_Projections.py
### Usage:
`python3 S3_Cost_Projections <INITIAL_BUCKET_SIZE> <DAILY_INPUT> <DAYS_TO_RUN>`
where:
- INITIAL_BUCKET_SIZE : the initial size of the bucket contents (GB)
- DAILY_INPUT : estimated volume of data being added daily (GB)
- DAYS_TO_RUN : number of days to simulate 
