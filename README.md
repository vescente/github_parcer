# GitHub Repository Classifier

This project classifies GitHub repositories to identify those containing unsafe code patterns. It utilizes the GitHub API to search for repositories based on specified keywords, such as Python and Django, and analyzes the code for potential vulnerabilities.

## Project Structure

```
github_parcer 
├── app.py # Entry point of the Flask application 
├── src 
│ ├── classifier.py # Logic for classifying unsafe code 
│ ├── config.py # Configuration file for the application 
│ ├── github_api.py # Functions to interact with the GitHub API 
├── templates # HTML templates for the Flask application 
│ ├── base.html 
│ ├── index.html 
│ ├── form.html 
│ └── contacts.html 
├── static # Static files (CSS, JS, images) 
│ ├── css 
│     └── styles.css 
│ └── js 
│     └── scripts.js 
├── requirements.txt # Project dependencies 
├── .gitignore # Files and directories to ignore in Git 
└── README.md # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/github-repo-classifier.git
   cd github-repo-classifier
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv source venv/bin/activate # On Windows use venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables for `SECRET_KEY` and `GITHUB_TOKEN`:
- On Windows (cmd):
  ```
  setx SECRET_KEY "your-secret-key"
  setx GITHUB_TOKEN "your-github-token"
  ```
- On Windows (PowerShell):
  ```
  $env:SECRET_KEY="your-secret-key"
  $env:G

## Usage

1. 1. Run the Flask application:
   ```
   flask run
   ```

2. Open your browser and go to `http://127.0.0.1:5000/` to access the application.

3. Use the web interface to enter the URL of a GitHub repository for analysis.

4. The application will fetch the repository, analyze the code for unsafe patterns, and display the results on the web page.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.