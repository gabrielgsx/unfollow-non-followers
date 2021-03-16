from selenium import webdriver
from time import sleep
from env import username, password
import os


options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=User")

driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)
driver.get("https://www.instagram.com")
sleep(3)

def get_unfollowers(username):
  driver.get('https://www.instagram.com/{}'.format(username))
  sleep(2)
  driver.find_element_by_xpath("//a[contains(@href, '{}/following')]".format(username)).click()
  _get_following()
  sleep(15)
  driver.get('https://www.instagram.com/{}'.format(username))
  driver.find_element_by_xpath("//a[contains(@href, '{}/followers')]".format(username)).click()
  _get_followers()
  

def _get_following():
  sleep(2)
  scroll_box = driver.find_element_by_class_name('isgrP')
  prev_height, height = 0, 1
  while prev_height != height:
      prev_height = height
      sleep(3)
      height = driver.execute_script("""
      arguments[0].scrollTo(0, arguments[0].scrollHeight);
      return arguments[0].scrollHeight;
      """, scroll_box)
  links = scroll_box.find_elements_by_tag_name('a')
  names = [name.text for name in links if name.text != '']
  file = open(r"C:\Users\gabri\Desktop\fol\app_notas\data\following.py", "w")  # CHANGE IT WITH YOUR DIRECTORY
  file.write(f"{names}") 
  file.close() 
  return

def _get_followers():
  sleep(2)
  scroll_box = driver.find_element_by_class_name('isgrP')
  prev_height, height = 0, 1
  while prev_height != height:
      prev_height = height
      sleep(3)
      height = driver.execute_script("""
      arguments[0].scrollTo(0, arguments[0].scrollHeight);
      return arguments[0].scrollHeight;
      """, scroll_box)
  links = scroll_box.find_elements_by_tag_name('a')
  names2 = [name.text for name in links if name.text != '']
  file = open(r"C:\Users\gabri\Desktop\fol\app_notas\data\followers.py", "w") # CHANGE IT WITH YOUR DIRECTORY
  file.write(f"{names2}") 
  file.close() 
  return



get_unfollowers(username)



