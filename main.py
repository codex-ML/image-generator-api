import io
import time
import os
import torch
import uvicorn
import nest_asyncio
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from diffusers import DiffusionPipeline
from PIL import Image
from cloudinary import config as cloudinary_config
from cloudinary import uploader
from pyngrok import ngrok

# Configure Cloudinary with environment variables
cloudinary_config(
    cloud_name="dydcwsbps",
    api_key="453987143398927",
    api_secret="HOPrcHCwX4nMRoV5mWHR5YzMigo"
)


pipe = DiffusionPipeline.from_pretrained(
    "cagliostrolab/animagine-xl-3.1",
    torch_dtype=torch.float16,
    use_safetensors=True,
)
pipe.to('cuda')

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class GenerateRequest(BaseModel):
    prompt: str
    negative_prompt: str

@app.post("/generate")
async def generate_image(request: GenerateRequest):
    start_time = time.time()
    try:
       
        result = pipe(
            prompt=request.prompt,
            negative_prompt=request.negative_prompt,
            width=832,
            height=1216,
            guidance_scale=7,
            num_inference_steps=28  
        )
        image = result.images[0]

     
        buffer = io.BytesIO()
        image.save(buffer, format="PNG")
        buffer.seek(0)

        
        upload_response = uploader.upload(buffer, folder="generated_images")

        time_taken = time.time() - start_time

        return {
            "image_url": upload_response.get('secure_url'),
            "time_taken": time_taken,
            "prompt": request.prompt,
            "negative_prompt": request.negative_prompt
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    nest_asyncio.apply()

    # Get Ngrok auth token from environment variables
    ngrok_auth_token = ("2aCe8QZNv0fiTIwG6o5BhCgw5hM_77rSPax1bZPjruJrELAnL")
    if ngrok_auth_token:
        ngrok.set_auth_token(ngrok_auth_token)
    else:
        raise Exception("NGROK_AUTH_TOKEN is not set in environment variables.")

    # Start Ngrok tunnel
    public_url = ngrok.connect(8000).public_url
    print(f"Public URL: {public_url}")

    # Run Uvicorn server
    uvicorn.run(app, host="0.0.0.0", port=8000)
