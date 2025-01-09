import requests
import json
import os
from urllib.parse import urljoin
from getpass import getpass

def load_json(file_path):
    """
    Load JSON data from a file.
    """
    with open(file_path, 'r') as f:
        return json.load(f)

def delete_repository(base_url, organization, project, repository_id, api_version, headers, auth):
    """
    Permanently delete a repository from the Azure DevOps Recycle Bin.
    """
    # Construct the URL
    url = f"{base_url}/{organization}/{project}/_apis/git/recycleBin/repositories/{repository_id}?api-version={api_version}"
    
    try:
        response = requests.delete(url, headers=headers, auth=auth)
        if response.status_code == 204:
            print(f"✅ Successfully deleted repository ID: {repository_id}")
            return True
        else:
            print(f"❌ Failed to delete repository ID: {repository_id}. Status Code: {response.status_code}. Response: {response.text}")
            return False
    except Exception as e:
        print(f"⚠️ Error deleting repository ID: {repository_id}. Error: {str(e)}")
        return False

def main():
    # Configuration - You can modify these variables as needed
    # Example base_url: "https://dev.azure.com"
    base_url = input("🔗 Enter Azure DevOps Base URL (e.g., https://dev.azure.com): ").strip()
    organization = input("🏢 Enter your Organization Name: ").strip()
    project = input("📁 Enter your Project Name: ").strip()
    api_version = input("🔍 Enter API Version (e.g., 7.1-preview.1): ").strip()
    json_file_path = input("📄 Enter the path to your JSON file (e.g., deleted_repos.json): ").strip()

    # Personal Access Token (PAT)
    print("\n🔐 Enter your Azure DevOps Personal Access Token (PAT).")
    print("   Note: Your PAT will not be displayed as you type.")
    pat = getpass("PAT: ").strip()

    if not all([base_url, organization, project, api_version, json_file_path, pat]):
        print("❗ All inputs are required. Please try again.")
        return

    # Load JSON data
    if not os.path.exists(json_file_path):
        print(f"❗ JSON file not found at path: {json_file_path}")
        return

    try:
        data = load_json(json_file_path)
    except json.JSONDecodeError as e:
        print(f"❗ Failed to parse JSON file. Error: {str(e)}")
        return

    if 'value' not in data:
        print("❗ Invalid JSON format: 'value' key not found.")
        return

    repositories = data['value']
    total_repos = data.get('count', len(repositories))
    print(f"\n🗃️ Total repositories to delete: {total_repos}\n")

    # Set up headers for authentication
    # Azure DevOps uses Basic Auth with PAT as the password and an empty username
    headers = {
        'Content-Type': 'application/json'
    }
    auth = ('', pat)  # Empty username

    # Iterate through each repository and delete
    success_count = 0
    failure_count = 0

    for repo in repositories:
        repo_id = repo.get('id')
        repo_name = repo.get('name')
        if not repo_id:
            print(f"⚠️ Repository name '{repo_name}' does not have an 'id'. Skipping.")
            failure_count += 1
            continue

        # Perform deletion
        success = delete_repository(base_url, organization, project, repo_id, api_version, headers=headers, auth=auth)
        if success:
            success_count += 1
        else:
            failure_count += 1

    # Summary
    print("\n📋 Deletion Process Completed.")
    print(f"✅ Successfully deleted: {success_count}")
    print(f"❌ Failed to delete: {failure_count}")

if __name__ == "__main__":
    main()
