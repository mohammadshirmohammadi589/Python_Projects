# Python Command-Line Interface (CLI) Tool

This Python project provides a command-line interface (CLI) tool for various file and directory operations. It supports commands for listing files, creating and deleting files and directories, navigating directories, copying, moving, finding files, and displaying file content.  It also includes logging of commands and a separate example of using `argparse` with subcommands.

## How to Run

1.  Clone the repository:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://www.google.com/search?q=https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git) # Replace with your repo URL
    ```
2.  Navigate to the project directory:
    ```bash
    cd PythonCLI
    ```
3.  Run the script:
    ```bash
    python cli_tool.py [command] [path] [arguments]
    ```

## Usage

The CLI tool takes a command as the first argument, an optional path as the second argument, and any command-specific arguments.

**File and Directory Operations:**

*   **`list [path]` or `ls [path]`:** Lists files and directories in the specified path (defaults to the current directory if no path is given).
*   **`create_file [path]`:** Creates a file named `new_file.txt` in the specified path.
*   **`create_dir [path]` or `mkdir [path]`:** Creates a directory named `new_directory` in the specified path.
*   **`delete_file [path]` or `rm [path]`:** Deletes the file `file_to_delete.txt` in the specified path.
*   **`delete_dir [path]` or `rmdir [path]`:** Deletes the directory `directory_to_delete` in the specified path.
*   **`rm -r [path]`:** Recursively deletes a directory and its contents.
*   **`cd [path]`:** Changes the current directory to the specified path.
*   **`cp [source] [destination]`:** Copies a file or directory from `source` to `destination`.
*   **`mv [source] [destination]`:** Moves a file or directory from `source` to `destination`.
*   **`find [path] [pattern]`:** Finds files in the specified path that match the given pattern.
*   **`cat [path]`:** Displays the contents of the file specified by `path`.

**Example:**

```bash
python cli_tool.py list .                # Lists files in the current directory
python cli_tool.py create_file my_folder  # Creates a file in the my_folder directory
python cli_tool.py delete_dir my_folder   # Deletes the my_folder directory
python cli_tool.py find . "txt"          # Finds all .txt files in the current directory and subdirectories
python cli_tool.py cat myfile.txt        # Displays the contents of myfile.txt
