
#!/bin/bash

# Define the virtual environment name
VENV_NAME="venv"

# Function to create and activate virtual environment
create_and_activate_venv() {
    echo "Creating virtual environment..."
    python3 -m venv $VENV_NAME
    source $VENV_NAME/bin/activate
}

# Function to install dependencies
install_dependencies() {
    echo "Installing dependencies..."
    pip install PyPDF2 python-docx openpyxl pandas requests beautifulsoup4 openai
}

# Check if .installed file exists
if [[ -f ".installed" ]]; then
    echo ".installed file exists. Activating virtual environment..."
    source $VENV_NAME/bin/activate
else
    create_and_activate_venv
    install_dependencies
    touch .installed
    echo "Dependencies installed and .installed file created."
fi
