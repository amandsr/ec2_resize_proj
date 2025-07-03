import boto3
import sys
import json
from datetime import datetime, timedelta

instance_id = sys.argv[1]
region = sys.argv[2]

cloudwatch = boto3.client('cloudwatch', region_name=region)

end = datetime.utcnow()
start = end - timedelta(days=7)

def get_metric(metric_name):
    response = cloudwatch.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName=metric_name,
        Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
        StartTime=start,
        EndTime=end,
        Period=3600,
        Statistics=['Average']
    )
    datapoints = response.get('Datapoints', [])
    if not datapoints:
        return 0.0
    return sum(dp['Average'] for dp in datapoints) / len(datapoints)

cpu = get_metric('CPUUtilization')
mem = get_metric('MemoryUtilization')

with open('metrics.json', 'w') as f:
    json.dump({'cpu_avg': cpu, 'memory_avg': mem}, f)

print(f"CPU avg: {cpu:.2f}%, Memory avg: {mem:.2f}%")