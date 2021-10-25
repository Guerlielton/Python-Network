import os
import boto3
from botocore import config
from botocore.retries.standard import RetryPolicy 
from settings import AWS_ACCESS_KEY,AWS_SECRET_KEY,CLUSTER 

aws_acces_secret = os.getenv("AWS_ACCESS_KEY")
aws_acces_secret_key = os.getenv("AWS_SECRET_KEY")

# Require information for start request 
client = boto3.client('ecs',region_name='us-east-1',aws_access_key_id=aws_acces_secret,aws_secret_access_key=aws_acces_secret_key)

def ecs_status():
    response = client.describe_clusters(
        clusters = [CLUSTER] 
    )
    print(response)
    clus = []
    for ecs in response['clusters']:
        namecluster = ecs['clusterName']
        stat = ecs['status']
        capacity = ecs ['capacityProviders']
        runtaskcount = ecs ['runningTasksCount']
        activeservcount = ecs ['activeServicesCount']
        temp_dict = {}
        temp_dict ['namecluster'] = namecluster
        temp_dict ['stat'] = stat
        temp_dict ['capacity'] = capacity
        temp_dict ['runtaskcount'] = runtaskcount
        temp_dict ['activeServCount'] = activeservcount
        
        clus.append(temp_dict)
    return clus
if __name__ == "__main__":
    ecs_status()