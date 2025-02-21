# GitHub Repository Classifier

This project classifies GitHub repositories to identify those containing unsafe code patterns. It utilizes the GitHub API to search for repositories based on specified keywords, such as Python and Django, and analyzes the code for potential vulnerabilities.

## Project Structure

```
github-repo-classifier
├── src
│   ├── main.py          # Entry point of the application
│   ├── github_api.py    # Functions to interact with the GitHub API
│   ├── classifier.py     # Logic for classifying unsafe code
│   └── utils.py         # Utility functions for the project
├── requirements.txt      # Project dependencies
├── .gitignore            # Files and directories to ignore in Git
└── README.md             # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/github-repo-classifier.git
   cd github-repo-classifier
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python src/main.py
   ```

2. Follow the prompts to enter keywords for searching GitHub repositories.

3. The application will fetch the repositories, analyze the code for unsafe patterns, and save the results in a JSON format.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.