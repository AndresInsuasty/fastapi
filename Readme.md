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

## Como subir un archivo
vamos a suponer que tenemos el bucket llamado `fastapi2` y el archivo `readme.md`, entonces debemos hacer una peticion GET a la API como la siguiente estructura:

`[DIRECCION_IP]/uploadvoice/[NOMBRE_BUCKET]/[NOMBRE_ARCHIVO]`

Observa el siguiente ejemplo:

`http://localhost:8000/uploadvoice/fastapi2/readme.md`

La respuesta de esta petición es la siguiente:


```
{
    "url": "https://fastapi2.s3.amazonaws.com/",
    "fields": {
        "key": "readme.md",
        "AWSAccessKeyId": "AKIAJX5RO26LV35IZV3Q",
        "policy": "eyJleHBpcmF0aW9uIjogIjIwMjAtMTItMTdUMTY6MDM6NDlaIiwgImNvbmRpdGlvbnMiOiBbeyJidWNrZXQiOiAiZmFzdGFwaTIifSwgeyJrZXkiOiAicmVhZG1lLm1kIn1dfQ==",
        "signature": "3lyTBfUNWxsNd/Dr+EIUqMhoopk="
    }
}
```

esta respuesta nos entrega los datos para hacer un POST a la url del bucket y guardar ahi el archivo. Desde un HTML esta es una sugerencia como realizar este POST

```
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  </head>
  <body>
    <!-- Copy the 'url' value returned by S3Client.generate_presigned_post() -->
    <form action="URL_VALUE" method="post" enctype="multipart/form-data">
      <!-- Copy the 'fields' key:values returned by S3Client.generate_presigned_post() -->
      <input type="hidden" name="key" value="VALUE" />
      <input type="hidden" name="AWSAccessKeyId" value="VALUE" />
      <input type="hidden" name="policy" value="VALUE" />
      <input type="hidden" name="signature" value="VALUE" />
    File:
      <input type="file"   name="file" /> <br />
      <input type="submit" name="submit" value="Upload to Amazon S3" />
    </form>
  </body>
</html>
```

## Saber que archivos hay

para saber que archivos hay dentro de un bucket hacemos una peticion GET con la siguiente estructura:

`[DIRECCION_IP]/listfiles/[NOMBRE_BUCKET]` 

ejemplo:

`http://localhost:8000/listfiles/udenar`

la respuesta de este ejemplo es:
```
{
    "files": [
        "Advertising.csv",
        "Curso Matlab/",
        "Curso Matlab/clase 2.7 Livescript en Matlab/",
        "Curso Matlab/clase 2.7 Livescript en Matlab/ExplorandoDatos.mlx",
        "Curso Matlab/clase 2.7 Livescript en Matlab/data.csv",
        "catb_saved_DF.pkl",
        "catb_saved_Fanduel.pkl"
    ]
}
```

## Generar una voz clonada

para generar un clonado de voz debemos hacer una peticion GET a la siguiente ruta
`[DIRECCION_IP]/generatevoice/[TEXT]/[NOMBRE BUCKET]/[AUDIO ORIGINAL]`

ejemplo:

`http://localhost:8000/generatevoice/hola/originalvoices/TRUMP.wav`

el resultado tiene la url del archivo .wav con la voz clonada:
```
{
    "url": "https://clonedvoices.s3.amazonaws.com/duque.wav?AWSAccessKeyId=AKIAJX5RO26LV35IZV3Q&Signature=ouitJ1pM90Ra5zkentuCfabOk24%3D&Expires=1608227098"
}
```


