os module : provides a way to interact with the operating system, such as working with file paths and directories.

shutil module : offers a high-level interface for file operations, including copying files.

The copy_xml_testcase_files function takes two arguments: search_path and destination_directory. It copies XML files containing the string 'Testcase' from the search path to the destination directory.

The function uses os.walk() to traverse all directories and files within the search path. It captures the root path, directories, and files in each iteration.

For each file, it checks if the file has an '.xml' extension using file.endswith('.xml').

If the file has the desired extension, it constructs the full file path using os.path.join(root, file).

The function then opens the file in read mode and checks if it contains the string 'Testcase'. If it does, the file is copied to the destination directory using shutil.copy().

A message is printed indicating which file was copied to the destination directory.

Once all files are processed, a "Copying completed!" message is displayed.

The __name__ == '__main__' condition ensures that the code block under it is only executed when the script is run directly and not imported as a module.

The search_path variable is set to C:\PythonTask, representing the path where the XML files are located.

The home_directory variable is set to C:\Users\deeks, which should be replaced with the actual path to your home directory.

The copy_xml_testcase_files function is called with the specified search path and destination directory arguments.

The function will execute, searching for XML files containing 'Testcase' in the search path and copying them to the destination directory.

