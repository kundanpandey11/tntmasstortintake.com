import os

def list_html_files_in_parent_directory():
    # Get the parent directory of the current script
    parent_directory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    
    # List all HTML files in the parent directory
    html_files = [file for file in os.listdir(parent_directory) if file.endswith('.html')]
    
    if html_files:
        print("HTML files in the parent directory:")
        for html_file in html_files:
            print(html_file)
    else:
        print("No HTML files found in the parent directory.")

if __name__ == "__main__":
    list_html_files_in_parent_directory()
