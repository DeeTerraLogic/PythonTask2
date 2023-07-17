import os
import shutil

def copy_xml_testcase_files(search_path, destination_directory):
    # Walk through all directories and files in the search path
    for root, dirs, files in os.walk(search_path):
        for file in files:
            if file.endswith('.xml'):
                file_path = os.path.join(root, file)
                
                # Check if the file contains 'Testcase' string
                with open(file_path, 'r') as f:
                    if 'Testcase' in f.read():
                        # Copy the file to the destination directory
                        shutil.copy(file_path, destination_directory)
                        print(f"Copied {file} to {destination_directory}")
    
    print("Copying completed!")

if __name__ == '__main__':
    # Specify the search path and destination directory
    search_path = r'C:\PythonTask'
    home_directory = r'C:\Users\deeks' 
    
    # Call the function to copy XML Testcase files
    copy_xml_testcase_files(search_path, home_directory)

