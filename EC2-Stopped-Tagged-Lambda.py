import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

ec2 = boto3.resource('ec2')
def lambda_handler(event, context):
    filters = [{
            'Name': 'tag:AutOff',
            'Values': ['true']
        },
        {
            'Name': 'instance-state-name', 
            'Values': ['running']
        }
    ]
    #filter the instances
    instances = ec2.instances.filter(Filters=filters)
    #locate all running instances
    RunningInstances = [instance.id for instance in instances]
    print RunningInstances
    if len(RunningInstances) > 0:
        shuttingDown = ec2.instances.filter(InstanceIds=RunningInstances).stop()
        print shuttingDown
    else:
        print "Nothing to do"
