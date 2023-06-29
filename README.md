# Web Screenshot App

This command-line application allows you to capture full-page screenshots of websites. The app will continue capturing screenshots until you enter an empty request.

## Installation

To install the Web Screenshot App, follow these steps:

1. Download the latest release from the [GitHub repository](https://github.com/lixelv/web_screenshot/archive/refs/heads/main.zip).
2. Extract the downloaded file to your preferred location.
3. Open the terminal and navigate to the extracted directory.


## Usage

To use the Web Screenshot App, follow these steps:

1. Open the terminal and navigate to the application directory.
2. Run the following command to start the app: `python parse.py`
3. Enter the URL of the website you want to capture a screenshot of.
4. The app will process the request and save the screenshot as an image file in the designated directory.
5. Repeat steps 3 and 4 for additional screenshots.
6. To stop the app and exit, simply enter an empty request by pressing Enter without providing a URL.

If you want to use html file, just write in url link something like this:
`file:///D:/Download/ChatGPT.html`
> **Note:** The Web Screenshot App supports capturing full-page screenshots of websites. Ensure that you have a stable internet connection and sufficient storage space to store the captured screenshots.

## Configuration

To change config, just open file config.txt and 
change it, you can change only one thing, this is width of your 
screenshot, default value is **1920px**.