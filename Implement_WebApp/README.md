# Image Analyzer  WebApp
 
## Overview

Image Analyzer is a web application built with Flask that allows users to upload images and analyze them using Azure's Computer Vision API. The application provides a simple and intuitive interface for users to get detailed information about their images, including descriptions, tags, categories, and detected objects.

## Features

- User-friendly web interface for image upload
- Integration with Azure Computer Vision API for image analysis
- Display of image analysis results including:
  - Image description
  - Tags
  - Categories
  - Detected objects
- Responsive design for both desktop and mobile devices

## Technologies Used

- Python
- Flask
- Azure Cognitive Services (Computer Vision API)
- HTML/CSS

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/Curious4Tech/azure-image-recognition.git
   
   cd azure-image-recognition/Implement_WebApp
   ```

 2.  Install the required dependencies (Optional for this demo):
  ```
   pip install -r requirements.txt
  ```

 3. Set up your Azure Computer Vision API credentials:
   - Create a `.env` file in the root directory of the project
   - Add your Azure credentials to the `.env` file:
     ```
     AZURE_COMPUTER_VISION_KEY=your_subscription_key
     AZURE_COMPUTER_VISION_ENDPOINT=your_endpoint_url
     ```

Refer to the [.env.example](.env.example) for a step-by-step guide on creating and configuring a `.env` file.

4. Run the Flask application:
   ```
   python app.py
   ```

5. Open a web browser and navigate to `http://127.0.0.1:5000/` to use the application.

## Usage

1. On the home page, click the "Choose File" button to select an image from your local machine.
2. Click the "Analyze Image" button to upload and analyze the image.
3. View the analysis results, including the image description, tags, categories, and detected objects.
4. To analyze another image, click the "Analyze Another Image" button at the bottom of the results page.

## Project Structure

```
image-analyzer/
├── app.py
├── .env
├── static/
│   ├── style.css
│   └── uploads/
└── templates/
    ├── index.html
    └── result.html
```

- `app.py`: The main Flask application file
- `.env`: Contains Azure API credentials (not tracked by git)
- `requirements.txt`: List of Python dependencies
- `static/`: Directory for static files (CSS and uploaded images)
- `templates/`: Directory for HTML templates

## Contributing

Contributions to the Image Analyzer project are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Azure Cognitive Services](https://azure.microsoft.com/en-us/services/cognitive-services/)
- [Flask](https://flask.palletsprojects.com/)
