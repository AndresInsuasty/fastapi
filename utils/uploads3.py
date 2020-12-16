import boto3

s3 = boto3.resource('s3')

print('='*50)
print('List all the buckets created on your account')
for id, bucket in enumerate(s3.buckets.all()):
    print(id+1,bucket.name)