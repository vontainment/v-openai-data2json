
# GPT Content Processing Tool

This tool is designed to automate the process of extracting text from various file formats and web pages, converting them into a format suitable for training or fine-tuning GPT models. It supports a range of file types including PDFs, DOCX, Excel, and ASCII text files like TXT, MD, XML, HTML, CSV, RTF. Additionally, it can scrape and process text content from web URLs.

## Features

- **File Processing**: Handles PDFs, DOCX, Excel, and various text files. Converts PDF and DOCX to text, Excel to CSV.
- **URL Processing**: Extracts text from web pages, removing non-text elements like images, scripts, and styles.
- **GPT-4 API Interaction**: Converts the extracted content into JSON-formatted data, suitable for GPT model training.
- **Temporary Storage**: Utilizes a temporary directory for intermediate files.
- **Automated Environment Setup**: Includes a Bash script to set up a Python virtual environment and install dependencies.

## Project Structure

```
project_directory/
│
├── file_processor.py      # Main script
├── file_handling.py       # Handles file and URL processing
├── utils.py               # Utility functions
├── gpt_interaction.py     # GPT-4 API interactions
├── web_scraping.py        # Web scraping functionalities
└── setup_environment.sh   # Bash script for environment setup
```

## Getting Started

### Prerequisites

- Python 3
- Pip
- Bash (for setup script)

### Setup

1. Clone the repository or download the project files.
2. Run the `setup_environment.sh` script to create a virtual environment and install dependencies:
   ```bash
   chmod +x setup_environment.sh
   ./setup_environment.sh
   ```
3. Activate the virtual environment (if not already activated):
   ```bash
   source venv/bin/activate
   ```

### Usage

To process files in a directory:

```bash
python file_processor.py --files /path/to/input_directory
```

To process URLs from a text file:

```bash
python file_processor.py --links /path/to/text_file_with_urls
```

The output will be saved in the `./output` directory.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check issues page if you want to contribute.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OpenAI's GPT-4 API for content processing.
- Python libraries such as PyPDF2, python-docx, and BeautifulSoup for file handling and web scraping.
