import boto3

client = boto3.client('s3')

#response = client.create_bucket(
#   Bucket='aravind-boto3-test-090',
#)

response = client.get_bucket_acl(
    Bucket='aravind-boto3-test-090',
)

grants = response['Grants']

print(grants)