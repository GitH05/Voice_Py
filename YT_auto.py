from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class music():
    def __init__(self):
        
        chrome_service = Service(ChromeDriverManager().install())
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--start-maximized") 
        self.driver = webdriver.Chrome(options=chrome_options, service=chrome_service)


    def play(self,query):
        self.query=query
        self.driver.get(url="https://www.youtube.com/results?search_query="+ query)
        video = self.driver.find_element(By.ID, "video-title")
        video.click()

# assist=music()
# assist.play("tere bina")
