from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

# Path to your ChromeDriver executable
chromedriver_path = r"C:\path\to\your\chromedriver.exe"
service = Service(executable_path=chromedriver_path)

# Probability distributions for selecting options per question index
# Each list corresponds to the weight of each option for that question
probabilities = {
    0: [0.05, 0.45, 0.45, 0.05],
    1: [0.1, 0.2, 0.3, 0.3, 0.1, 0.0],
    2: [0.3, 0.7, 0],
    3: [0.95, 0.05, 0.0],
    4: [0.05, 0.95],
    5: [0.1, 0.2, 0.3, 0.2, 0.1],
    6: [0.3, 0.2, 0.1, 0.2, 0.2],
    7: [0.3, 0.4, 0.1, 0.1, 0.1],
    8: [0.1, 0.2, 0.2, 0.4, 0.1],
    9: [0.5, 0.5, 0.0, 0.0, 0.0],
    10: [0.3, 0.4, 0.1, 0.1, 0.1],
    11: [0.5, 0.5, 0.0, 0.0, 0.0],
    12: [0.3, 0.4, 0.1, 0.1, 0.1],
    13: [0.3, 0.4, 0.1, 0.1, 0.1],
    14: [0.5, 0.3, 0.1, 0.1],
    15: [0.3, 0.3, 0.1, 0.15, 0.15],
    16: [0.2, 0.2, 0.2, 0.2, 0.2],
    17: [0.3, 0.4, 0.1, 0.1, 0.1],
    18: [0.5, 0.5, 0.0, 0.0, 0.0],
    19: [0.3, 0.4, 0.1, 0.1, 0.1],
    20: [0.3, 0.5, 0.1, 0.1, 0.0],
    21: [0.5, 0.5, 0.0, 0.0, 0.0],
    22: [0.5, 0.5, 0.0, 0.0, 0.0],
    23: [0.4, 0.5, 0.1, 0.0, 0.0],
    24: [0.3, 0.5, 0.1, 0.1, 0.0],
    25: [0.3, 0.4, 0.2, 0.1, 0.0],
    26: [0.5, 0.5, 0.0, 0.0, 0.0],
    27: [0.4, 0.4, 0.1, 0.1, 0.0],
}

def choose_option_with_probability(options, question_index):
    """
    Select an option element from a list of options based on predefined probabilities.
    If probabilities are not defined or don't match the number of options,
    selects a random option uniformly.
    """
    proba = probabilities.get(question_index, None)
    if proba and len(proba) == len(options):
        # weighted random choice based on probabilities for the question
        return random.choices(options, weights=proba, k=1)[0]
    # fallback: choose randomly if no probability distribution is defined
    return random.choice(options)

def fill_form(driver):
    """
    Finds all radio button groups (questions) on the Google Form page,
    selects an option for each question using weighted probabilities,
    and finally clicks the submit button and waits for confirmation.
    """
    wait = WebDriverWait(driver, 10)

    # Wait until all questions (radiogroups) are present on the page
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[role="radiogroup"]')))
    
    # Find all question containers
    questions = driver.find_elements(By.CSS_SELECTOR, 'div[role="radiogroup"]')

    for q_index, question in enumerate(questions):
        # Find all options for the current question
        options = question.find_elements(By.CSS_SELECTOR, 'div[role="radio"]')
        if not options:
            print(f"❌ Question {q_index + 1} has no options detected.")
            continue

        # Choose an option based on the probability distribution
        choice = choose_option_with_probability(options, q_index)
        
        # Scroll the chosen option into view for better reliability
        driver.execute_script("arguments[0].scrollIntoView(true);", choice)
        time.sleep(0.2)  # small delay for UI to update
        
        # Click the chosen option
        choice.click()
        print(f"✅ Question {q_index + 1}: option selected.")

    # Click the "Submit" button after all questions are answered
    try:
        submit_btn = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//div[@role='button' and (.//span[text()='Submit' or text()='Envoyer'])]"
        )))
        driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
        time.sleep(0.3)

        # Attempt to click normally, fallback to JS click if necessary
        try:
            submit_btn.click()
        except:
            driver.execute_script("arguments[0].click();", submit_btn)

        print("📤 'Submit' button clicked, waiting for confirmation...")

        # Wait until confirmation text appears indicating submission success
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((
            By.XPATH, "//div[contains(text(),'Your response has been recorded') or contains(text(),'Votre réponse a bien été enregistrée')]"
        )))

        print("🎉 Confirmation received: response recorded.")

    except Exception as e:
        print(f"⚠️ Error during submission: {e}")

def main():
    """
    Main function to launch the Chrome browser,
    submit the Google Form multiple times, then close the browser.
    """
    driver = webdriver.Chrome(service=service)
    # URL to your google from
    form_url = "https://docs.google.com/forms/d/e/your-form-id/viewform"
    number_of_responses = 100

    try:
        for i in range(number_of_responses):
            print(f"\n🔁 Submission #{i + 1}")
            driver.get(form_url)      # Load form page
            time.sleep(2)             # Wait for form to fully load
            fill_form(driver)         # Fill and submit the form
            time.sleep(3)             # Wait before next submission
    finally:
        driver.quit()                 # Close the browser when done

if __name__ == "__main__":
    main()
