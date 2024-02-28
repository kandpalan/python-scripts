#!/usr/bin/python3
import boto3,os

instance_id = input("Enter Instance id: ")

def instance_action(): 
  client = boto3.client('ec2')
  response = client.describe_instances()
  for r in response['Reservations']:
    for i in r['Instances']:
      e = i['InstanceId']
      if e == instance_id: 
        a = i['State']['Code']
        if a == 16:
          print("\n",instance_id, "is running")
          b = input("\nDo you want to stop this host ? (y/n)  ")
          if b == "y" or b == "Y" or b == "yes" or b == "Yes" or b == "YES":
            response = client.stop_instances(InstanceIds=[f'{instance_id}'])
            print("\n",response)
        elif a == 80:
          print("\n",instance_id, "Stopped")
          b = input("\nDo you want to start this host ? (y/n)  ")
          if b == "y" or b == "Y" or b == "yes" or b == "Yes" or b == "YES":
            response = client.start_instances(InstanceIds=[f'{instance_id}'])
            print("\n",response)
        elif a == 0:
          print("\n",f"{instance_id}","in pending state")
        elif a == 32:
          print("\n",f"{instance_id}","is shutting-down")
        elif a == 48:
          print("\n",f"{instance_id}","is Terminated")
        elif a == 64:
          print("\n",f"{instance_id}","is Stopping")
instance_action()
