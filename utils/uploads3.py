import boto3

def list_buckets():
    s3 = boto3.resource('s3')
    output=[]
    for bucket in s3.buckets.all():
        output.append(bucket.name)
    return output

def upload_file(filename,bucket_name):
    s3 = boto3.resource('s3')
    data = open(filename,'rb')
    s3.Bucket(bucket_name).put_object(Key=filename,Body=data)

def delete_file(filename,bucket_name):
    s3 = boto3.resource("s3")
    try:
        obj = s3.Object(bucket_name, filename)
        obj.delete()
        return True
    except:
        return False

def list_elements(bucket_name):
    conn = boto3.client('s3')  
    output=[]
    for key in conn.list_objects(Bucket=bucket_name)['Contents']:
        output.append(key['Key'])
    return output

bucket_name = 'udenar'
filename = 'requirements.txt'

#print(list_buckets())
#upload_file(filename,bucket_name)
#delete_file(filename,bucket_name)
# print(list_elements(bucket_name))
