

flask --app app.main run

flask --app app.main --debug run app.run


# My Voice Project

## Description

My Voice Project is a Flask-based web application that allows users to generate audio from text, record their voice, and upload MP3 audio files for processing. This project provides a simple, interactive platform where users can input text to generate speech, record their voice, and upload their voice recordings.

## Features

- **Text to Speech**: Users can enter text, and the system will convert it into audio.
- **Voice Recording**: Users can record their own voice through the web interface.
- **Audio File Upload**: Users can upload MP3 audio files for further processing.
- **Audio Playback**: Generated or uploaded audio files can be played directly in the browser.

## Requirements

- Python 3.x
- Flask
- werkzeug

You can install the required dependencies by running the following command:

## Configuration

1. **Environment Configuration**:  
   The `.flaskenv` file is used to configure the Flask application settings.

2. **Audio Uploads**:  
The application supports audio file uploads with the extension `.mp3`. Uploaded files are stored in the `uploads/` directory. If this directory does not exist, it will be automatically created upon the first file upload.

3. **Text to Speech and Audio Uploading**:  
- Users can enter text in a text area on the front-end interface, and the system will generate the corresponding audio.
- Users can also record their voice and upload it for processing.

## Usage

1. **Run the Flask Server**:  
To start the Flask development server, execute the following command:

This will start the application on `http://127.0.0.1:5000`.

2. **Interacting with the Application**:  
- Open `index.html` in a browser.
- Use the text area to generate speech from text.
- Record your voice using the voice recording feature.
- Upload MP3 audio files using the provided upload section.

## Future Enhancements

- Integrate more advanced voice processing techniques.
- Add support for multiple audio formats (e.g., WAV, OGG).
- Implement user authentication for saving and sharing audio files.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Flask documentation for setting up the web framework.
- JavaScript libraries for handling audio recording and playback.


## Running the Application

To run the Flask application, use one of the following commands in the terminal:

### 1. Run the Application (Basic)

To start the Flask development server, execute the following command:

This command will start the Flask app with the entry point defined in `app.main`. By default, it will run the app in development mode on `http://127.0.0.1:5000`.

### 2. Run the Application with Debug Mode

To run the application with debug mode enabled, which allows for automatic reloading and provides detailed error messages, use the following command:


Alternatively, if you prefer to directly call the `app.run()` method, use this command:


This will start the Flask app with debug mode enabled, which is useful during development for faster testing and debugging.




