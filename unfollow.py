from selenium import webdriver
from time import sleep
from random import randint
from data import x
from data2 import y
from get-non-followers import z

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=User")
driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)
#tempo = randint(2, 6)


def unfollow(z):
    for c in z:
        driver.get("https://www.instagram.com/{}/".format(c))
        sleep(3)
        un_button1 = driver.find_element_by_class_name('_5f5mN.-fzfL._6VtSN.yZn4P').click()
        sleep(3)
        
        un_button2 = driver.find_element_by_class_name('aOOlW.-Cab_').click()
        sleep(3)
        break
        

unfollow(z)

