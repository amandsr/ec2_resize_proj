import os
import boto3
import json

with open('suggestion.json') as f:
    data = json.load(f)

instance_id = os.getenv('INSTANCE_ID')
region = os.getenv('REGION')
suggested_type = data['suggested_type']

ec2 = boto3.client('ec2', region_name=region)

print(f"Stopping instance {instance_id}...")
ec2.stop_instances(InstanceIds=[instance_id])
ec2.get_waiter('instance_stopped').wait(InstanceIds=[instance_id])

print(f"Modifying instance type to {suggested_type}...")
ec2.modify_instance_attribute(InstanceId=instance_id, Attribute='instanceType', Value=suggested_type)

print("Starting instance...")
ec2.start_instances(InstanceIds=[instance_id])
ec2.get_waiter('instance_running').wait(InstanceIds=[instance_id])

print("Instance type change applied successfully.")