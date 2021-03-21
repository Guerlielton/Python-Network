import boto3
from botocore.retries.standard import RetryPolicy 

# Require information for start request 

client = boto3.client('ec2',region_name='us-east-1')

def ec2_status():
    instances = []
    response = client.describe_instances()
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            instance_type = instance['InstanceType']
            instance_name = instance['Tags'][0]['Value']
            instance_status = instance['State']['Name']
            # privateip = instance['PrivateIpAddress']
            # subnetid = instance['SubnetId']
            # vpcid = instance['VpcId']
            ec2_dict = {}
            ec2_dict ['instance_id'] = instance_id
            ec2_dict ['instance_type'] = instance_type
            ec2_dict ['instance_name'] = instance_name
            ec2_dict ['instance_status'] = instance_status
            instances.append(ec2_dict)
    return instances
if __name__ == "__main__":
    ec2_status()


