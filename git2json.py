import os
import json
import shutil
import subprocess
import sys

def main():

    if len(sys.argv) != 3:
        print("Usage: python git2json.py <github_url> <output_path>")
        sys.exit(1)
        
    url = sys.argv[1]
    out_path = sys.argv[2]

    def clone_repo(url, path):
        if not os.path.exists(path):
            os.makedirs(path)
        subprocess.run(['git', 'clone', url, path])
        
    def get_text_files(path):
        """Return list of paths for all text files in path"""
        text_files = []
        for root, _, files in os.walk(path):
            for f in files:
                _, ext = os.path.splitext(f)
                if ext in ['.txt', '.py', '.md', '.json', '.yml', '.yaml', '.cfg', '.html', '.css', '.js', '.ts', '.sh', '.bat', '.c', '.cpp', '.java', '.xml', '.csv', '.tsv', '.jsonl', '.ipynb', 'jsx', '.tsx']:
                    text_files.append(os.path.join(root, f))
        return text_files

    def text_to_json(text_files, out_file):
        """Convert text files to JSON format in out_file"""
        data = {}
        for f in text_files:
            key = os.path.basename(f)
            data[key] = open(f).read()

        with open(out_file, 'w') as outfile:
            json.dump(data, outfile)

    if __name__ == '__main__':
        # url = 'https://github.com/anshan-XR-ROB/HDES-Net.git'
        # path = 'repo'

        # Clone the repository
        clone_repo(url, out_path)

        # Get list of text files
        text_files = get_text_files(out_path)

        # Convert text files to JSON format
        text_to_json(text_files, 'repo.json')
        
        # Delete repo folder
        shutil.rmtree(out_path)
    
main()