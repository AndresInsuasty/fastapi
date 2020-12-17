from fastapi import FastAPI
from utils.uploads3 import create_presigned_post, list_elements, create_presigned_url
app = FastAPI()

@app.get("/upload/{bucket}/{filename}")
async def root(bucket: str, filename: str):
    return create_presigned_post(bucket,filename)

@app.get("/listfiles/{bucket}")
async def root(bucket: str):
    return {"files":list_elements(bucket)}

@app.get("/generatevoice/{text}/{bucket}/{voice_filename}")
async def root(text: str,bucket: str, voice_filename: str):
    #funcion para generar voz clonada
    voice = list_elements('clonedvoices')
    
    return {"url":create_presigned_url('clonedvoices',voice[0])}

@app.get("/generatevideo/{voice_filename}/{video_filename}")
async def root(voice_filename: str,video_filename: str):
    #funcion para generar voz clonada
    video = list_elements('videoscloned')
    return {"url":create_presigned_url('videoscloned',video[0])}