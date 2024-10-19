
<h1>AI Image Generator API</h1>

<h2>Overview</h2>
<p>
    This project implements an AI image generator API using the Diffusion Model 3. It allows users to generate images based on text prompts and negative prompts. The API is built with FastAPI and leverages Cloudinary for image storage and Pyngrok for public access during development.
</p>

<h2>Table of Contents</h2>
<ul>
    <li><a href="#features">Features</a></li>
    <li><a href="#requirements">Requirements</a></li>
    <li><a href="#setup">Setup</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#api-endpoints">API Endpoints</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
</ul>

<h2 id="features">Features</h2>
<ul>
    <li>High-quality image generation using a diffusion model.</li>
    <li>User-friendly API with prompt input.</li>
    <li>Integration with Cloudinary for storing generated images.</li>
    <li>Public access via Ngrok for easy testing and demonstration.</li>
</ul>

<h2 id="requirements">Requirements</h2>
<p>To run this project, you will need:</p>
<pre>
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
</pre>
<p>You can install the necessary dependencies with:</p>
<pre>pip install -r requirements.txt</pre>

<h2 id="setup">Setup</h2>
<ol>
    <li><strong>Clone the Repository:</strong>
        <pre>git clone https://github.com/yourusername/ai-image-generator-api.git
cd ai-image-generator-api</pre>
    </li>
    <li><strong>Set Environment Variables:</strong>
        <p>Configure your Cloudinary and Ngrok credentials. You can set them in your environment or directly in the code (not recommended for production).</p>
        <pre>cloudinary_config(
    cloud_name="your_cloud_name",
    api_key="your_api_key",
    api_secret="your_api_secret"
)</pre>
        <p>Replace the values with your actual Cloudinary credentials.</p>
    </li>
    <li><strong>Run the API:</strong>
        <pre>python main.py</pre>
        <p>This will start the FastAPI server and provide a public URL via Ngrok.</p>
    </li>
</ol>

<h2 id="usage">Usage</h2>
<p>To generate an image, send a POST request to the <code>/generate</code> endpoint with the following JSON body:</p>
<pre>{
    "prompt": "A beautiful sunset over a mountain range.",
    "negative_prompt": "No people, no buildings."
}</pre>

<h3>Example with <code>curl</code></h3>
<pre>curl -X POST "http://localhost:8000/generate" -H "Content-Type: application/json" -d '{"prompt": "A beautiful sunset over a mountain range.", "negative_prompt": "No people, no buildings."}'</pre>

<h3>Response</h3>
<p>The API will return a JSON response containing the image URL, time taken for generation, and the prompts used:</p>
<pre>{
    "image_url": "https://your_cloudinary_url.png",
    "time_taken": 2.34,
    "prompt": "A beautiful sunset over a mountain range.",
    "negative_prompt": "No people, no buildings."
}</pre>

<h2 id="api-endpoints">API Endpoints</h2>

<h3>POST /generate</h3>
<ul>
    <li><strong>Description:</strong> Generates an image based on the provided prompt and negative prompt.</li>
    <li><strong>Request Body:</strong>
        <ul>
            <li><code>prompt</code>: The text prompt for image generation (string).</li>
            <li><code>negative_prompt</code>: The text prompt to avoid certain features (string).</li>
        </ul>
    </li>
    <li><strong>Response:</strong>
        <ul>
            <li><code>image_url</code>: URL of the generated image.</li>
            <li><code>time_taken</code>: Time taken to generate the image (float).</li>
            <li><code>prompt</code>: The prompt used.</li>
            <li><code>negative_prompt</code>: The negative prompt used.</li>
        </ul>
    </li>
</ul>

<h2 id="contributing">Contributing</h2>
<p>Contributions are welcome! If you have suggestions or improvements, please fork the repository and create a pull request.</p>

<h2 id="license">License</h2>
<p>This project is licensed under the MIT License. See the LICENSE file for more details.</p>

