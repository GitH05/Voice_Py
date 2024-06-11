from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class infow:
    def __init__(self):
        # Use webdriver_manager to handle ChromeDriver
        chrome_service = Service(ChromeDriverManager().install())
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--start-maximized")  # Start Chrome maximized
        self.driver = webdriver.Chrome(options=chrome_options, service=chrome_service)

    def get_info(self,query):
        self.query=query
        self.driver.get(url="https://www.wikipedia.com")
        search = self.driver.find_element(By.ID, "searchInput")
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element(By.XPATH, '//*[@type="submit"]')
        enter.click()

