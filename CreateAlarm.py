import boto3

client = boto3.client('cloudwatch')
Metric=["CPUUtilization","NetworkIn","NetworkOut","StatusCheckFailed","MemoryUtilization","DiskSpaceUtilization"]
Measure=["Percent","Bytes","Bytes","Count","Percent","Percent"]
Trigger=[80,209715200,78643200,1,80,80]
Subject=["CPUUtilization is Greater than 80 %","NetworkIn is Greater than 200 MB","NetworkOut is Greater than 75 MB","Status Check-Failed-Any","DiskSpaceUtilization is Greater than 80%"]

def alarm(ServerName,Description,InstanceId,SnsTopic,i):
	client.put_metric_alarm(
	AlarmName= ServerName+' '+Subject[i],
    AlarmDescription=Description,
    ActionsEnabled=True,
    AlarmActions=SnsTopic,
    MetricName=Metric[i],
    Namespace='AWS/EC2',
    Statistic='Average',
    #ExtendedStatistic='string',
    Dimensions=[
        {
            'Name': 'InstanceId',
            'Value': InstanceId
        },
    ],
    Period=300,
    Unit=Measure[i],
    EvaluationPeriods=1,
    DatapointsToAlarm=1,
    Threshold=Trigger[i],
    ComparisonOperator='GreaterThanOrEqualToThreshold'
	)


