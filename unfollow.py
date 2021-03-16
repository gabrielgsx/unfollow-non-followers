from selenium import webdriver
from time import sleep
from random import randint
from data/following import x
from data/followers import y

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=User")
driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)
tempo = randint(2, 6)

remover = list(set(x) - set(y))


def unfollow(remover):
    for c in remover:
        driver.get("https://www.instagram.com/{}/".format(c))
        sleep(3)
        un_button1 = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button').click()
        sleep(tempo)
        un_button2 = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[1]').click()
        sleep(tempo)
        remover.remove(c)
        

unfollow(remover)

