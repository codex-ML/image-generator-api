

```markdown
<h1> AI Image Generator API </h1>

## Overview

This project implements an AI image generator API using the Diffusion Model 3. It allows users to generate images based on text prompts and negative prompts. The API is built with FastAPI and leverages Cloudinary for image storage and Pyngrok for public access during development.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features

- High-quality image generation using a diffusion model.
- User-friendly API with prompt input.
- Integration with Cloudinary for storing generated images.
- Public access via Ngrok for easy testing and demonstration.

## Requirements

To run this project, you will need:

```plaintext
transformers==4.28.0
safetensors==0.3.1
accelerate==0.27.2
diffusers==0.26.3
gradio==4.20.0
invisible-watermark==0.2.0
spaces==0.24.0
omegaconf==2.3.0
timm==0.9.10
fastapi==0.95.2
uvicorn==0.22.0
cloudinary==1.30.0
pyngrok==5.2.0
Pillow==9.5.0
nest_asyncio==1.5.6
torch==2.0.1+cu118  # Specify the appropriate CUDA version
```

You can install the necessary dependencies with:

```bash
pip install -r requirements.txt
```

## Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/ai-image-generator-api.git
   cd ai-image-generator-api
   ```

2. **Set Environment Variables:**
   Configure your Cloudinary and Ngrok credentials. You can set them in your environment or directly in the code (not recommended for production).

   ```python
   cloudinary_config(
       cloud_name="your_cloud_name",
       api_key="your_api_key",
       api_secret="your_api_secret"
   )
   ```

   Replace the values with your actual Cloudinary credentials.

3. **Run the API:**

   ```bash
   python main.py
   ```

   This will start the FastAPI server and provide a public URL via Ngrok.

## Usage

To generate an image, send a POST request to the `/generate` endpoint with the following JSON body:

```json
{
    "prompt": "A beautiful sunset over a mountain range.",
    "negative_prompt": "No people, no buildings."
}
```

### Example with `curl`

```bash
curl -X POST "http://localhost:8000/generate" -H "Content-Type: application/json" -d '{"prompt": "A beautiful sunset over a mountain range.", "negative_prompt": "No people, no buildings."}'
```

### Response

The API will return a JSON response containing the image URL, time taken for generation, and the prompts used:

```json
{
    "image_url": "https://your_cloudinary_url.png",
    "time_taken": 2.34,
    "prompt": "A beautiful sunset over a mountain range.",
    "negative_prompt": "No people, no buildings."
}
```

## API Endpoints

### POST /generate

- **Description:** Generates an image based on the provided prompt and negative prompt.
- **Request Body:**
  - `prompt`: The text prompt for image generation (string).
  - `negative_prompt`: The text prompt to avoid certain features (string).
  
- **Response:**
  - `image_url`: URL of the generated image.
  - `time_taken`: Time taken to generate the image (float).
  - `prompt`: The prompt used.
  - `negative_prompt`: The negative prompt used.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please fork the repository and create a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
```

### Instructions to Customize
- Fill in your actual Cloudinary credentials where indicated.
- Adjust any other project-specific details as necessary.
