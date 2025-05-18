# Google Forms Auto Filler with Weighted Random Answers

Automates filling and submitting Google Forms using Selenium WebDriver.  
Supports configuring weighted probabilities for answer choices to simulate realistic response patterns.

---

## Features

- Automatically selects answers based on specified probability weights per question  
- Handles multiple choice questions with radio buttons  
- Waits for elements to load before interaction  
- Clicks the submit button and waits for confirmation  
- Configurable number of form submissions  

---

## Requirements

- Python 3.x  
- Selenium (`pip install selenium`)  
- Chrome WebDriver (compatible with your Chrome version)  

---

## Setup

1. Download the ChromeDriver executable from [https://sites.google.com/chromium.org/driver/](https://sites.google.com/chromium.org/driver/)  
2. Place the `chromedriver.exe` in a known path and update the `chromedriver_path` variable in the script accordingly  

---

## Usage

1. Modify the `form_url` variable in the script to your target Google Form URL  
2. Adjust the `probabilites` dictionary to reflect the weighted answer probabilities per question  
3. Run the script:

```bash
python your_script_name.py
