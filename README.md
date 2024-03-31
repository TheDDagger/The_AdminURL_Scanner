
# Web Admin URL Scanner

## Overview

This Python script is designed to scan a given URL for common administration paths commonly used in web applications. It utilizes multithreading for faster scanning and provides colored output to highlight any discovered admin paths.

## Features

- Scans a provided URL for common administration paths.
- Utilizes multithreading for faster scanning.
- Colored output to highlight discovered admin paths.
- Accepts user input for the URL to scan.

## Prerequisites

- Python 3.x
- Requests library (`pip install requests`)
- Termcolor library (`pip install termcolor`)

## Usage

1. Clone this repository to your local machine:

    ```
    git clone https://github.com/TheDDagger/The_AdminURL_Scanner.git
    ```

2. Navigate to the directory:

    ```
    cd The_AdminURL_Scanner
    ```

3. Run the script:

    ```
    python TheScanner.py
    ```

4. Enter the URL you want to scan when prompted.
## Example
python TheScanner.py 
Enter the URL you want to scan: http://example.com
Admin login found: http://example.com/admin
Admin login found: http://example.com/administrator
...
Total admin paths found: 10
Time taken: 5.32 seconds

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](MIT License) file for details.

---
