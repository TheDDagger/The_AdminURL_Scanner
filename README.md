# Admin Login Path Scanner

## Description
This Python script scans a given URL for common admin login paths and reports any findings. It utilizes asyncio and aiohttp for asynchronous HTTP requests, allowing for efficient scanning of multiple paths concurrently.

## Installation
1. Clone the repository to your local machine:
    ```
    git clone https://github.com/TheDDagger/The_AdminURL_Scanner.git
    ```
2. Navigate to the project directory:
    ```
    cd The_AdminURL_Scanner
    ```
3. Install the required dependencies using pip:
    ```
    pip install -r requirements.txt
    ```

## Usage
1. Run the script by executing the following command and follow the prompts:
    ```
    python3 TheScanner.py
    ```
2. Enter the URL you want to scan for admin login paths when prompted.
3. Wait for the script to complete the scanning process.
4. Review the output to see any admin login paths found, along with the total count and the time taken for the scan.

## Configuration
- The `MAX_CONCURRENT_REQUESTS` variable sets the maximum number of concurrent HTTP requests. Adjust this value based on your system resources and network capabilities.
- The `TIMEOUT` variable specifies the timeout duration for each HTTP request in seconds. Modify this value as needed to suit your requirements.

## Contributing
Contributions to this project are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request. Please adhere to the code formatting and style guidelines.

## License
Its project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
