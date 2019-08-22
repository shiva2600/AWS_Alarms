#calling alarm function
from CreateAlarm import *
import boto3

ServerName = "fg-ma-r-server"
Description= "customer:Future group, Private ip: 172.31.40.83 ; server configuration:  4 core 30 GiB RAM"
InstanceId="i-0446578ba34454170"
SnsTopic=['arn:aws:sns:us-west-2:770678546179:fg-ec2-al']
Namespace=['AWS/EC2','AWS/EC2','AWS/EC2','AWS/EC2','System/Linux','System/Linux','System/Linux']
Filesystem=['Nil','Nil','Nil','Nil','Nil','/dev/xvda1','/dev/xvdf']
MountPath=['Nil','Nil','Nil','Nil','Nil','/','/opt/commonconfig']


for i in range(5):
 alarm(ServerName,Description,InstanceId,SnsTopic,i,Namespace)
 

for i in range(5,6):
 AlarmDisk(ServerName,Description,InstanceId,SnsTopic,i,Namespace,Filesystem,MountPath)

#Filesystem = /prod/xvda1, InstanceId = i-0853686bc726a04a7 (apoteket-vlc-prod-app01), MountPath = /


