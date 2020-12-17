Hi!
This repository is an exploration of fastapi library.

1. let's go to create an environment with conda

```conda create -n API python=3.7```

2. activate the environment

```conda activate API```

3. Install fastapi

`pip install fastapi` or `pip install fastapi==0.62.0`

4. Install uvicorn, an application server

`pip install uvicor` or `pip install uvicorn==0.13.1`

5. you can find a file called `example.py` to test this script, please type the following code into your terminal

```uvicorn example:app --reload```

the `--reload` is only for development, to refresh the changes made

=====
## Upload files to S3
you will find a function into the utils folder called `uploads3.py` to use it please have in mind the libraries required:

`pip install boto3`, moreover we need to have installed the AWS CLI in this case we use the version `2.1.11` and create credencials, `aws_access_key_id` and `aws_secret_access_key`. I created this into of IAM console.

So open a terminal and write `aws configure` after this enter your keys. In the section of region I wrote `us-east-1`
If you have issues with the functions of uploads3.py I recommend change the region of your bucket to `us-west-2`
