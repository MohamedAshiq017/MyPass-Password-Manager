# MyPass - Password Manager

MyPass is a simple and efficient password manager built using Python and Tkinter. It allows you to store, generate, and search passwords securely for your various accounts and websites.

## Features

- **Password Generation**: Generate strong, random passwords with a mix of letters, numbers, and symbols.
- **Save Passwords**: Store website credentials (email/username and password) securely in a local JSON file.
- **Search Functionality**: Quickly search for stored credentials using the website name.
- **Copy Passwords**: Automatically copies the generated password to your clipboard for convenience.

## Preview

### Application UI
![password_manager_UI](https://github.com/user-attachments/assets/acf96d0a-8156-45cf-b15e-4dfbe5596c8f)

## Requirements

To use this project, ensure the following are installed:

- Python 3.6 or above
- Required Python modules:
  - `tkinter` (comes pre-installed with Python)
  - `pyperclip` (can be installed via pip)


### Use the application to:
1. Enter website, email/username, and password details.
2. Click **Generate Password** to create a strong password automatically.
3. Save the credentials using the **Add** button.
4. Search for existing credentials using the **Search** button.

### File Structure
- **main.py**: Main script for the application.
- **data.json**: File to store the saved passwords securely. (Auto-created if not present)
- **logo.png**: Logo used in the application's UI.
- **password_manager.PNG**: Screenshot of the application for preview purposes.
- **requirements.txt**: List of dependencies for the project.

### Notes
- All credentials are stored locally in a `data.json` file in the same directory as the script. **Make sure this file is kept secure.**
- If `data.json` is not present, the script creates it automatically during the first save operation.
- You can pre-fill the email/username field by uncommenting the relevant line in the script.

### Install the required dependencies:
```bash
pip install -r requirements.txt

