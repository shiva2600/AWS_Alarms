import boto3

client = boto3.client('cloudwatch')
Metric=["CPUUtilization","NetworkIn","NetworkOut","StatusCheckFailed","MemoryUtilization","DiskSpaceUtilization","DiskSpaceUtilization"]
Measure=["Percent","Bytes","Bytes","Count","Percent","Percent","Percent"]
Trigger=[80,209715200,78643200,1,80,80,80]
Subject=["CPUUtilization is Greater than 80 %","NetworkIn is Greater than 200 MB","NetworkOut is Greater than 75 MB","Status Check-Failed-Any","MemoryUtilization is Greater than 80%", "root diskSpaceUtilization is Greater than 80%","/opt/commonconfig/ diskSpaceUtilization is Greater than 80%"]

def alarm(ServerName,Description,InstanceId,SnsTopic,i,Namespace):
	client.put_metric_alarm(
	AlarmName= ServerName+' '+Subject[i],
    AlarmDescription=Description,
    ActionsEnabled=True,
    AlarmActions=SnsTopic,
    MetricName=Metric[i],
    Namespace=Namespace[i],
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
	
def AlarmDisk(ServerName,Description,InstanceId,SnsTopic,i,Namespace,Filesystem,MountPath):
	client.put_metric_alarm(
	AlarmName= ServerName+' '+Subject[i],
    AlarmDescription=Description,
    ActionsEnabled=True,
    AlarmActions=SnsTopic,
    MetricName=Metric[i],
    Namespace=Namespace[i],
    Statistic='Average',
    #ExtendedStatistic='string',
    Dimensions=[
        {
            'Name': 'InstanceId',
            'Value': InstanceId
        },
		{
			'Name': 'Filesystem',
			'Value': Filesystem [i]
		},
		{
			'Name': 'MountPath',
			'Value' : MountPath[i]
		}
    ],
    Period=300,
    Unit=Measure[i],
    EvaluationPeriods=1,
    DatapointsToAlarm=1,
    Threshold=Trigger[i],
    ComparisonOperator='GreaterThanOrEqualToThreshold'
	)


