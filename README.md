# Client Environment Setup Script

This Python script sets up a user-specific environment in the terminal. It ensures that each client has a dedicated directory with a hidden profile file (`.profile.txt`) containing their name, phone, and email. The script validates the information, updates it if necessary, and provides access to the terminal after confirming or updating details.

## Features

- **Directory Setup**: Checks if the current working directory matches the client's username. If not, creates a new directory for the client.
- **Profile File Handling**: 
  - Checks if the hidden profile file (`.profile.txt`) exists within the client's directory.
  - Reads and displays profile information if the file exists, allowing the client to confirm if the details are up to date.
  - If the file doesn't exist or details are outdated, the script prompts the user for name, phone, and email, validates this data using regular expressions, and updates the file.
- **Input Validation**: Uses regex to ensure valid formats for:
  - **Name**: Only letters and spaces.
  - **Phone**: Only digits, with a length of 7-15.
  - **Email**: Must follow a basic email format (e.g., `user@example.com`).

## Prerequisites

- **Python 3.x**
- **OS**: Compatible with Unix-based systems (Linux, macOS). May require modifications for Windows.

## Installation

1. Clone or download this repository to your local machine.
2. Ensure Python 3.x is installed on your system.

## Usage

1. Open a terminal and navigate to the directory containing `client_environment.py`.
2. Run the script with:

   ```bash
   python client_environment.py
