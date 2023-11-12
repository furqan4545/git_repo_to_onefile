# git2json.py

## Overview

`git2json.py` is a Python script designed to clone a specified GitHub repository, extract text files (like `.py`, `.md`, `.js`, etc.), and convert these files into a single JSON file. This JSON file can then be used to feed data to ChatGPT AI models, aiding in understanding and analyzing the code context.

## Usage

To use `git2json.py`, you need to have Python and Git installed on your system. The script takes two command-line arguments: the URL of the GitHub repository to clone and the path where the repository should be cloned.

### Syntax

```bash
python git2json.py <github_url> <output_path>
```

### Parameters

- <github_url>: The URL of the GitHub repository you want to clone.
- <output_path>: The local path where the repository will be cloned and processed.

### Example

```bash
python git2json.py https://github.com/anshan-XR-ROB/HDES-Net.git repo
```

### How It Works

- Cloning the Repository: The script first clones the repository from the provided GitHub URL into the specified local path.
- Extracting Text Files: It then walks through the repository's directory structure, identifying text files such as Python scripts, Markdown files, HTML/CSS, JavaScript, etc.
- Creating JSON File: These files are read and their contents are stored in a JSON object, with each file's name as a key and its content as the value.
- Output: The JSON object is then written to a file named repo.json in the current working directory.
- Cleanup: After processing, the cloned repository folder is deleted to clean up the workspace.

### Purpose

- To take the json file and upload it to chatgpt for code analysis and furthermore you can ask any question regarding the code.
