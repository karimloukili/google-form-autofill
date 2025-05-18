# Google Form Auto Filler

Automate filling and submitting Google Forms multiple times using Selenium, with weighted random selection for each question's options.

---

## Features

- Automatically selects radio button options based on predefined probabilities per question.
- Handles dynamic loading of form elements reliably.
- Waits for submission confirmation before proceeding.
- Easily configurable number of form submissions.

---

## Requirements

- Python 3.x
- [Selenium](https://pypi.org/project/selenium/) (`pip install selenium`)
- Google Chrome browser
- ChromeDriver matching your Chrome version ([Download here](https://chromedriver.chromium.org/downloads))

---

## Setup

1. **Download and install ChromeDriver**  
   Make sure you download the ChromeDriver version that matches your installed Google Chrome browser version from the [official site](https://chromedriver.chromium.org/downloads).

2. **Configure the script**  
   - Set the path to your ChromeDriver executable in the script:

     ```python
     chromedriver_path = r"C:\path\to\your\chromedriver.exe"
     ```

   - Set your Google Form URL:

     ```python
     form_url = "https://docs.google.com/forms/d/e/your-form-id/viewform"
     ```

   - Adjust the number of form submissions as needed:

     ```python
     number_of_responses = 100
     ```

---

## Usage

Run the script using:

```bash
python your_script_name.py
