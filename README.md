# AzureDevOps-RecycleBin-Cleaner

Automate the management of your Azure DevOps repositories by efficiently emptying the Recycle Bin. This repository provides tools and scripts to help you identify and permanently delete repositories that are no longer needed, ensuring a clean and organized development environment.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [How to Use](#how-to-use)
  - [Step 1: Fetch Repositories in the Recycle Bin](#step-1-fetch-repositories-in-the-recycle-bin)
  - [Step 2: Run the Python Script](#step-2-run-the-python-script)
- [API Endpoint](#api-endpoint)
- [License](#license)

## Introduction

This repository contains a Python script that allows you to automate the permanent deletion of repositories from the Azure DevOps Recycle Bin. By leveraging Azure DevOps API, the script fetches repository details from a JSON file and deletes them in a batch process.

## Prerequisites

Before using this tool, make sure you have the following:

1. **Azure DevOps Personal Access Token (PAT):** A token with sufficient permissions to access and delete repositories.
2. **Python 3.6 or higher:** To run the provided script.
3. **Postman (optional):** For fetching repositories in the Recycle Bin.
4. **Permissions:** Ensure you have permissions to manage repositories in your Azure DevOps project.

## Setup

1. Clone the repository to your local machine:

   ```bash
   git clone git@github.com:username/azure-devops-repo-recycle-bin-cleaner.git
   cd azure-devops-repo-recycle-bin-cleaner
   ```

2. Install required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Save your repositories data into a JSON file (e.g., `deleted_repos.json`).

## How to Use

### Step 1: Fetch Repositories in the Recycle Bin

1. Open Postman or another API testing tool.
2. Use the following endpoint to fetch repositories in the Recycle Bin:

   ```
   GET https://dev.azure.com/{organization}/{project}/_apis/git/recycleBin/repositories?api-version=v7.1
   ```

3. Authenticate with **Basic Auth** and use your Azure DevOps PAT as the password (leave the username empty).
4. Save the response containing the repository details into a JSON file named `deleted_repos.json`.

### Step 2: Run the Python Script

1. Run the script:

   ```bash
   python empty_devops_recycle_bin.py
   ```

2. Follow the prompts to input the required details:
   - Azure DevOps Base URL
   - Organization Name
   - Project Name
   - API Version
   - Path to your JSON file
   - Personal Access Token (PAT)

3. The script will process the repositories listed in the JSON file and attempt to delete them permanently.

4. Review the summary of successfully deleted and failed deletions at the end.

## API Endpoint

The key API endpoint used in this tool is:

- **Fetch Recycle Bin Repositories:**

  ```
  GET https://dev.azure.com/{organization}/{project}/_apis/git/recycleBin/repositories?api-version=7.1
  ```

- **Delete Repository Permanently:**

  ```
  DELETE https://dev.azure.com/{organization}/{project}/_apis/git/recycleBin/repositories/{repositoryId}?api-version=7.1
  ```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
