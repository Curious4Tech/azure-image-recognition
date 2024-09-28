# azure-computer-vision-app
A Python-based image recognition app using Azure's Computer Vision API. This project demonstrates how to analyze images by detecting objects, extracting tags, and generating descriptions through Azure Cognitive Services, offering hands-on AI-driven insights.

# Azure Image Recognition App

This Python application uses Azure's Computer Vision API to analyze images and provide descriptions, tags, categories, and detect objects within the image.

## Prerequisites

Before you begin, ensure you have met the following requirements:

* You have a Microsoft Azure account with an active subscription.
* You have created a Computer Vision resource in your Azure account.
* You have Python 3.6 or later installed on your system.

## Installation

1. Clone this repository to your local machine:
   ```
   git clone https://github.com/yourusername/azure-image-recognition.git
   cd azure-image-recognition
   ```

2. Install the required Python packages:
   ```
   pip install azure-cognitiveservices-vision-computervision msrest python-dotenv
   ```

3. Create a `.env` file in the root directory of the project with your Azure credentials:
   ```
   AZURE_COMPUTER_VISION_KEY=your_computer_vision_key_here
   AZURE_COMPUTER_VISION_ENDPOINT=your_computer_vision_endpoint_here
   ```
   Replace `your_computer_vision_key_here` and `your_computer_vision_endpoint_here` with your actual Azure Computer Vision key and endpoint.

## Usage

1. Open the `image_recognition.py` file.

2. Replace the `image_url` variable with the URL of the image you want to analyze:
   ```python
   image_url = "https://example.com/path/to/your/image.jpg"
   ```

3. Run the script:
   ```
   python image_recognition.py
   ```

4. The script will output the analysis results, including:
   - Image description
   - Tags
   - Categories
   - Detected objects

## File Structure

- `image_recognition.py`: The main Python script that performs image analysis.
- `.env`: Contains your Azure credentials (do not commit this file to version control).
- `README.md`: This file, containing project documentation.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- This project uses the [Azure Computer Vision API](https://azure.microsoft.com/en-us/services/cognitive-services/computer-vision/).
- Thanks to Microsoft Azure for providing the cognitive services used in this project.
