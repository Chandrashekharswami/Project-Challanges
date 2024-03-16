import boto3
import requests
import json

def get_instance_metadata():
    # Get the instance ID from the instance metadata
    instance_id = requests.get("http://IPaddress/latest/meta-data/instance-id").text

    # Initialize Boto3 client for EC2
    ec2_client = boto3.client('ec2')

    # Describe instance attributes to get metadata
    response = ec2_client.describe_instances(InstanceIds=[instance_id])

    # Extract instance metadata from the response
    instance_metadata = response['Reservations'][0]['Instances'][0]

    return instance_metadata

def main():
    # Get instance metadata
    instance_metadata = get_instance_metadata()

    # Convert metadata to JSON format
    json_metadata = json.dumps(instance_metadata, indent=4)

    # Print JSON formatted metadata
    print(json_metadata)

if __name__ == "__main__":
    main()