from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

class ChatGPTScraper:
    def __init__(self, headless: bool = True):
        """
        Initializes the ChatGPT web scraper.

        :param headless: Run in headless mode (no UI)
        """
        self.headless = headless
        self.driver = self._init_driver()

    def _init_driver(self):
        """Initializes the Selenium WebDriver."""
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        if self.headless:
            options.add_argument("--headless=new")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        service = Service(ChromeDriverManager().install())

        driver = webdriver.Chrome(service=service, options=options)
        driver.get("https://chatgpt.com/")

        return driver

    def send_prompt(self, prompt: str) -> str:
        """Sends a prompt to ChatGPT and returns the response."""
        try:
            # Find the input box and send the prompt
            p_element = self.driver.find_element(By.CSS_SELECTOR, 'p[data-placeholder="Ask anything"]')
            self.driver.execute_script("arguments[0].innerText = arguments[1];", p_element, prompt)

            button = self.driver.find_element("css selector", '[aria-label="Send prompt"]')
            button.click()

            # Wait for the response
            time.sleep(30)

            # Scrape the latest response
            messages = self.driver.find_elements(By.CSS_SELECTOR, "div[data-message-author-role='assistant']")
            if messages:
                return messages[-1].text
            else:
                return "No response found."

        except Exception as e:
            return f"Error: {e}"

    def close(self):
        """Closes the browser."""
        self.driver.quit()

# Usage Example
if __name__ == "__main__":
    chatgpt = ChatGPTScraper(headless=False)
    response = chatgpt.send_prompt("Hello, how are you?")
    print("ChatGPT Response:", response)
    chatgpt.close()
