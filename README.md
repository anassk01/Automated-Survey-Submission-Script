# Automated Survey Submission Script

This Python script automates the submission of survey responses to a Google Form using Selenium WebDriver.

## Requirements
- Python 3
- Selenium WebDriver
- Google Chrome

## Installation
1. Clone this repository: `git clone https://github.com/your_username/automated-survey-script.git`
2. Install the required packages: `pip install -r requirements.txt`
3. Download [chromedriver](https://chromedriver.chromium.org/downloads) and place it in the project directory.

## Usage
1. Prepare your survey responses in a CSV file (`responses.csv`).
2. Run the script: `python automated_survey_script.py`

## Configuration
- Adjust sleep durations (`time.sleep()`) for page loading and form submission as needed.
- Modify `chrome_driver_path` variable to point to your chromedriver executable.
- Customize the Google Form URL (`url`) and CSV file path (`./responses.csv`).

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
