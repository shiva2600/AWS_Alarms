#calling alarm function
from CreateAlarm import alarm
import boto3

ServerName = "jollibee-poc-app01"
Description= "customer:jollibee private ip:172.17.108.197 ; server configuration:8 core 32 GiB RAM"
InstanceId="i-0e234c8c494609171"
SnsTopic="arn:aws:sns:us-east-1:386165448317:jlb-ec2-al"

for i in Metric:
 alarm(ServerName,Description,InstanceId,SnsTopic,i)





