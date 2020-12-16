import boto3

s3 = boto3.resource('s3')

# list files
print('='*50)
print('List all the buckets created on your account')
for id, bucket in enumerate(s3.buckets.all()):
    print(id+1,bucket.name)

# Upload a new file
bucket_name = 'pruebafastapi'
filename = 'requirements.txt'
data = open(filename,'rb')
s3.Bucket(bucket_name).put_object(Key=filename,Body=data)

