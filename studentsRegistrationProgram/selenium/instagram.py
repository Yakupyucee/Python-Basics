from instagramUserInfo import username,password
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time


class Instagram:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []
        self.followed = []
    

    def singIn(self):
        self.browser.get("https://www.instagram.com/")
        time.sleep(1)

        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(self.username)
        self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(self.password)

        self.browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[3]/button").click()


    def getUserWithScroll(self,scroll_screen_id, users_id):
        user_count = 0
        new_count = 0
        while True:
            scrollable_element = self.browser.find_element(By.CSS_SELECTOR, scroll_screen_id)
            for i in range(1, 16): 
                self.browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_element)
                time.sleep(0.2) 
          
            users = self.browser.find_elements(By.CSS_SELECTOR, users_id)

            user_count = new_count
            new_count = len (users)
            if new_count == user_count :
                break
            print("Number of new user :" , new_count)
        return users


    def get_profilescreen(self):
        self.browser.get(f"https://www.instagram.com/{self.username}/")

        time.sleep(2)

        return self.browser.find_element(By.TAG_NAME, "ul").find_elements(By.TAG_NAME, "li")


    def getfollowers(self):
        
        items = self.get_profilescreen()
        
        items[1].click()

        time.sleep(2)

        users = self.getUserWithScroll('.xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6', '.x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3')

        for user in users:
            self.followers.append((user.find_element(By.CSS_SELECTOR, "a").get_attribute("href")).split('/')[-2])


    def getfollowed(self):
        items = self.get_profilescreen()
        
        items[2].click()

        time.sleep(2)

        users = self.getUserWithScroll('.xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6', '.x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3')

        for user in users:
            self.followed.append((user.find_element(By.CSS_SELECTOR, "a").get_attribute("href")).split('/')[-2])

      
    def non_Followers(self):
        return [item for item in self.followed if item not in self.followers]


    def unfollowed(self):
        return [item for item in self.followers if item not in self.followed]


    

def printList(list):
    count = 1 
    for i in list : 
        print(f"{count}. {i}") 
        count+=1
    print("\n\n\n")

instagram = Instagram(username, password)

instagram.singIn()

time.sleep(5)

instagram.getfollowers()
printList(instagram.followers)

instagram.getfollowed()
printList(instagram.followed)

printList(instagram.non_Followers())
printList(instagram.unfollowed())

time.sleep(15)