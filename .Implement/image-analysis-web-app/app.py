import os
from flask import Flask, render_template, request, url_for
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
from dotenv import load_dotenv
import uuid

load_dotenv()

app = Flask(__name__)

# Set up authentication
subscription_key = os.getenv('AZURE_COMPUTER_VISION_KEY')
endpoint = os.getenv('AZURE_COMPUTER_VISION_ENDPOINT')

# Initialize the Computer Vision client
vision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

def analyze_image(image_path):
    features = [
        VisualFeatureTypes.description,
        VisualFeatureTypes.tags,
        VisualFeatureTypes.categories,
        VisualFeatureTypes.objects
    ]
    
    with open(image_path, "rb") as image_file:
        results = vision_client.analyze_image_in_stream(image_file, visual_features=features)
    
    analysis = {
        "description": results.description.captions[0].text if results.description.captions else "",
        "tags": [{"name": tag.name, "confidence": f"{tag.confidence:.2f}"} for tag in results.tags],
        "categories": [{"name": category.name, "confidence": f"{category.score:.2f}"} for category in results.categories],
        "objects": [{"name": obj.object_property, "confidence": f"{obj.confidence:.2f}"} for obj in results.objects]
    }
    
    return analysis

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', error='No file part')
        
        file = request.files['file']
        
        if file.filename == '':
            return render_template('index.html', error='No selected file')
        
        if file:
            filename = str(uuid.uuid4()) + os.path.splitext(file.filename)[1]
            filepath = os.path.join('static', 'uploads', filename)
            file.save(filepath)
            
            analysis = analyze_image(filepath)
            
            return render_template('result.html', image_url=url_for('static', filename=f'uploads/{filename}'), analysis=analysis)
    
    return render_template('index.html')

if __name__ == '__main__':
    os.makedirs(os.path.join('static', 'uploads'), exist_ok=True)
    app.run(debug=True)