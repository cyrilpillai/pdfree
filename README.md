# PDFree

[PDFree](https://pdfree.cyrilpillai.com/) is a simple web application built with Flask that allows users to upload password-protected PDF files and remove their passwords. It provides a user-friendly interface for securely handling sensitive documents without the need for additional software installations. The PDF files are persisted only temporarily and are deleted as soon as their purpose is served.

![Mockup](/assets/mockup.jpg)

## Features

- Upload password-protected PDF files
- Remove password protection from PDF files
- Securely handle sensitive documents
- User-friendly web interface

## Technologies Used

PDFree is built using the following technologies:

- **Flask**: A lightweight web framework for building Python applications.
- **venv**: A Python package that creates isolated environments for managing project dependencies.
- **gunicorn**: A Python WSGI HTTP server for running web applications.
- **fly.io**: A platform for deploying and hosting applications.

## Installation

To run PDFree locally, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/cyrilpillai/pdfree.git
   ```

2. Navigate to the project directory:

   ```
   cd pdfree
   ```

3. Create a virtual environment and activate it:

   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

5. Start the application using gunicorn:

   ```
   gunicorn app:app
   ```

7. Open your web browser and visit `http://localhost:8000` to access PDFree.

## Deployment

PDFree is hosted on fly.io. To deploy PDFree, follow these steps:

1. Create an account on [fly.io](https://fly.io) if you haven't already.

2. Install the Fly command-line tool by following the instructions on the [Fly documentation](https://fly.io/docs/hands-on/install-flyctl/).

3. Set up your Fly project by running:

   ```
   flyctl launch
   ```

4. Configure your Fly project using the generated `fly.toml` file. Update the configuration as needed.

5. Deploy the application to Fly:

   ```
   flyctl deploy
   ```

6. Once the deployment is complete, you will receive a URL where PDFree is accessible.

## Contributions

Contributions to PDFree are welcome! If you would like to contribute, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix:

   ```
   git checkout -b feature/your-feature-name
   ```

3. Make your changes and commit them:

   ```
   git commit -m "Add your commit message"
   ```

4. Push your changes to your forked repository:

   ```
   git push origin feature/your-feature-name
   ```

5. Open a pull request on the main repository.

Please ensure that your code adheres to the existing code style and includes appropriate tests.


## Acknowledgments

I am a Python novice & PDFree was built with the assistance of ChatGPT, an AI language model developed by OpenAI. Special thanks to the Python community and all the contributors of the libraries used in this project.

## License
```
Copyright 2023 Cyril Pillai
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
   http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.