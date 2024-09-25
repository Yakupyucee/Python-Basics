from githubUserInfo import username,password
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Github:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []

    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)

        self.browser.find_element(By.XPATH, "//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element(By.XPATH, "//*[@id='password']").send_keys(self.password)
        time.sleep(1)

        self.browser.find_element(By.XPATH, "//*[@id='login']/div[4]/form/div/input[13]").click()


    def getFollowers(self):
        self.browser.get(f"https://github.com/{self.username}?page=1&tab=followers")
        time.sleep(1)
        last_page = False

        while True:
            items = self.browser.find_elements(By.CSS_SELECTOR, ".d-table.table-fixed")


            try: #Single page control. Because if there is single page, there are no next and previous buttons.
                links = self.browser.find_element(By.CLASS_NAME, "pagination").find_elements(By.TAG_NAME, "a")
            except:
                for i in items:
                    self.followers.append(i.find_element(By.CSS_SELECTOR, ".Link--secondary").text)
                print(len(self.followers)) 
                break   
            

            if last_page:
                break           

            for i in items: # Usernames on the page are added to the followers list
                self.followers.append(i.find_element(By.CSS_SELECTOR, ".Link--secondary").text)
            print(len(self.followers))            

            last_page = True

            for link in links:# if next is active, it is goes next page
                if link.text == "Next":
                    link.click()
                    last_page = False
                   
                    
            
            time.sleep(1)
            




github = Github(username, password)

github.signIn()

github.getFollowers()

print(github.followers)

time.sleep(5)