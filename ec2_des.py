import boto3
from botocore import config
from botocore.retries.standard import RetryPolicy 
from settings import AWS_SECRET_KEY,AWS_ACCESS_KEY

# Require information for start request 

client = boto3.client('ec2',region_name='us-east-1',aws_access_key_id=AWS_ACCESS_KEY,aws_secret_access_key=AWS_SECRET_KEY)

def ec2_status():
    instances = []
    response = client.describe_instances()
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            instance_type = instance['InstanceType']
            instance_name = instance['Tags'][0]['Value']
            instance_status = instance['State']['Name']
            #privateip = instance['PrivateIpAddress']
            #subnetid = instance['SubnetId']
            #vpcid = instance['VpcId']
            ec2 = {}
            ec2 ['instance_id'] = instance_id
            ec2 ['instance_type'] = instance_type
            ec2 ['instance_name'] = instance_name
            ec2 ['instance_status'] = instance_status
            instances.append(ec2)
    return instances
if __name__ == "__main__":
    ec2_status()


