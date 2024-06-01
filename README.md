# Google Form Automation

This Python script automates the process of filling out a Google Form with survey responses from a CSV file using Selenium WebDriver.

## Prerequisites

Before running the script, ensure that you have the following:

- Python installed (version 3.6 or higher)
- Selenium WebDriver library installed (`pip install selenium`)
- Chrome web browser installed
- ChromeDriver executable matching your Chrome browser version

## Installation

1. Clone the repository or download the script file.

2. Install the required dependencies by running the following command (VERSION 4.21.0 Used in this script) :
   ```
   pip install selenium
   ```

3. Download the appropriate version of ChromeDriver from the official website: [ChromeDriver Downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads)

4. Place the downloaded ChromeDriver executable in the same directory as the script or update the `chrome_driver_path` variable in the script with the path to the ChromeDriver executable.

## Configuration

1. Update the `url` variable in the script with the URL of the Google Form you want to automate.

2. Prepare a CSV file with the survey responses. The CSV file should have the following structure:
   - The first row should contain the column names, which should match the question texts in the Google Form.
   - Each subsequent row should contain the survey responses for a single submission.
   - Ensure that the CSV file is saved with UTF-8 encoding.

3. Update the `./fijii.csv` file path in the script with the path to your CSV file.

## Usage

1. Open a terminal or command prompt and navigate to the directory where the script is located.

2. Run the script using the following command:
   ```
   python script_name.py
   ```
   Replace `script_name.py` with the actual name of your script file.

3. The script will launch a Chrome browser window and start automating the Google Form submission process.

4. The script will iterate over each row in the CSV file and fill out the form with the corresponding survey responses.

5. After each form submission, the script will clear the cookies and refresh the page to prepare for the next submission.

6. Once all the survey responses have been submitted, the script will automatically close the browser.

## Troubleshooting

- If the script fails to locate elements on the page, try adjusting the wait times by modifying the `time.sleep()` values in the script.

- If the script encounters an error related to the ChromeDriver version, ensure that you have downloaded the correct version of ChromeDriver matching your Chrome browser version.

- If the script fails to select the correct answer options, double-check the question texts and answer options in your CSV file and ensure they match exactly with the ones on the Google Form.

## Notes

- This script is intended for educational and demonstration purposes only. Make sure to comply with the terms of service and usage policies of Google Forms when using this script.

- The script may require modifications based on the specific structure and layout of your Google Form. Inspect the form elements and update the CSS selectors and XPath expressions accordingly.

- Exercise caution when automating form submissions and ensure that you have the necessary permissions and legal rights to do so.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to customize and enhance the script based on your specific requirements.
