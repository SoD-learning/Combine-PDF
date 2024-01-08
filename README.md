# Combine PDF

## Introduction

Combine PDF is a simple, user-friendly tool that allows you to combine multiple PDF files into a single PDF document. This document provides step-by-step instructions on how to install and use the application.

## Requirements

To use Combine PDF, you will need:

- a computer running Windows, macOS or Linux.
- Python installed on your computer.

## Installation

### Step 1: Install Python

If you do not have Python installed on your computer, follow these steps:

1. Visit the official [Python website](https://www.python.org/downloads/)
2. Download the latest version of Python for your operating system.
3. Run the installer and follow the on-screen instructions to install Python. Make sure to check the box that says "Add Python to PATH" during installation.

### Step 2: Download the Application

1. Download the PDF Merger Application files from the provided link or source.
2. Extract the files to a folder on your computer.

### Step 3: Install Required Libraries

1. Open a command prompt or terminal window.
2. Navigate to the folder where you extracted the application files.
3. Run the following command to install the required Python library:

```bash
pip install PyPDF2
```

## Usage

### Running the Application

1. Open the folder where you extracted the application files.
2. Double-click on the file named `combine_pdf.py` to run the application.

## Merging PDF Files

1. Once the application is open, click the "Select PDFs" button.
2. Navigate to and select the PDF files you wish to merge. You can select multiple files by holding down the `Ctrl` key (or `Command` key on macOS) while clicking on the files.
3. Should you need to re-order the files, you can click each one and drag it up and down in the list.
4. After selecting the files, click the "Merge PDFs" button.
5. Choose a location and file name for the merged PDF and click 'Save'.
6. The application will merge the selected PDF files into one and save it to the chosen location. A confirmation message will appear in the application window.

## Troubleshooting

If you encounter any issues while using the application, please ensure that:

- You have Python correctly installed on your computer.
- You have installed the PyPDF2 library as instructed.
- You are selecting valid PDF files.