import os
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
from dotenv import load_dotenv

# Print current working directory
print(f"Current working directory: {os.getcwd()}")

# Try to read .env file directly
try:
    with open('.env', 'r') as f:
        print("Contents of .env file:")
        print(f.read())
except FileNotFoundError:
    print(".env file not found in the current directory")
except Exception as e:
    print(f"Error reading .env file: {e}")

# Load environment variables
load_dotenv()

# Set up authentication
subscription_key = os.getenv('AZURE_COMPUTER_VISION_KEY')
endpoint = os.getenv('AZURE_COMPUTER_VISION_ENDPOINT')

# Debug: Print out the values
print(f"Subscription Key: {subscription_key}")
print(f"Endpoint: {endpoint}")

# Check if the values are None
if subscription_key is None or endpoint is None:
    raise ValueError("Subscription key or endpoint is None. Please check your .env file.")

# Initialize the Computer Vision client
vision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

def analyze_image(image_url):
    """
    Analyze an image using Azure's Computer Vision API.
    """
    # Specify features to be retrieved
    features = [
        VisualFeatureTypes.description,
        VisualFeatureTypes.tags,
        VisualFeatureTypes.categories,
        VisualFeatureTypes.objects
    ]
    
    # Analyze the image
    results = vision_client.analyze_image(image_url, visual_features=features)
    
    # Get image description
    if results.description.captions:
        print(f"Description: {results.description.captions[0].text}")
    
    # Get image tags
    print("Tags:")
    for tag in results.tags:
        print(f"- {tag.name} (confidence: {tag.confidence:.2f})")
    
    # Get image categories
    print("Categories:")
    for category in results.categories:
        print(f"- {category.name} (confidence: {category.score:.2f})")
    
    # Get objects in the image
    print("Objects:")
    for obj in results.objects:
        print(f"- {obj.object_property} (confidence: {obj.confidence:.2f})")

# Main execution
if __name__ == "__main__":
    # Example usage
    image_url = "https://example.com/path/to/your/image.jpg"
    analyze_image(image_url)
