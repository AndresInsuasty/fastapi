import logging
import boto3
from botocore.exceptions import ClientError

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

def create_presigned_url(BUCKET, OBJECT, expiration=3600):
    """Generate a presigned URL to share an S3 object

    :param bucket_name: string
    :param filename: string
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Presigned URL as string. If error, returns None.
    """

    # Generate a presigned URL for the S3 object
    s3_client = boto3.client('s3')
    url = s3_client.generate_presigned_url(
        'get_object',
        Params={'Bucket': BUCKET, 'Key': OBJECT},
        ExpiresIn=expiration)

    return url

def create_presigned_post(bucket_name, object_name,
                          fields=None, conditions=None, expiration=3600):
    """Generate a presigned URL S3 POST request to upload a file

    :param bucket_name: string
    :param object_name: string
    :param fields: Dictionary of prefilled form fields
    :param conditions: List of conditions to include in the policy
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Dictionary with the following keys:
        url: URL to post to
        fields: Dictionary of form fields and values to submit with the POST
    :return: None if error.
    """

    # Generate a presigned S3 POST URL
    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_post(bucket_name,
                                                     object_name,
                                                     Fields=fields,
                                                     Conditions=conditions,
                                                     ExpiresIn=expiration)
    except ClientError as e:
        logging.error(e)
        return None

    # The response contains the presigned URL and required fields
    return response


#bucket_name = 'fastapi2'
#filename = 'Readme.md'

# print(list_buckets())
# upload_file(filename,bucket_name)
# delete_file(filename,bucket_name)
# print(list_elements(bucket_name))
# print(create_presigned_url(bucket_name,filename,expiration=3600))
# print(create_presigned_post(bucket_name,filename,expiration=1000))