from selenium import webdriver
import selenium.webdriver
from selenium import webdriver
from bs4 import BeautifulSoup
from nltk.tokenize import WhitespaceTokenizer 
import time

import csv
import pandas as pd

import tqdm

tk = WhitespaceTokenizer() 
comments = []
#stars = []
#date  =[]
def scroll(driver, timeout):
    scroll_pause_time = timeout

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        #WErWEJROIWERJOWIERjowierjiowej r_________________________we have to swap to newest
        #if "date" says not 2020, cut the peoram (break)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(scroll_pause_time)

        # Calculate new scroll height and compare with last scroll height

        new_height = driver.execute_script("return document.body.scrollHeight;")
        if new_height == last_height:
            # If heights are the same it will exit the function
            #for a in soup.findAll('div',attrs={'jscontroller':'LVJlx','class':'UD7Dzf'}):
            try:
                #clicks the find more button
                driver.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div/main/div/div[1]/div[2]/div[2]/div').click()
            except:
                if new_height == last_height:
                    break
        last_height = new_height
        
def deEmogize():
    pass


def main():

    driver = webdriver.Chrome("/Users/martintin/Downloads/chromedriver")
    driver.get("https://play.google.com/store/apps/details?id=com.instacart.client&showAllReviews=true")


    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div/main/div/div[1]/div[2]/c-wiz/div[1]/div/div[1]/div[2]/span').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div/main/div/div[1]/div[2]/c-wiz/div[1]/div/div[2]/div[1]/span').click()
    #gets to newest comments

    scroll(driver, 3)
    soup = BeautifulSoup(driver.page_source, features="html.parser")
    for i in soup.findAll('span',attrs={'jsname':'bN97Pc'}):
        entry = i.text
        if entry.endswith("...Full Review"):
            entry = entry[:-11]
        comments.append(entry)
    df = pd.DataFrame({"comments":comments})
    df.to_csv("instacart_ratings.csv",index=True,encoding="utf-8")
    print(len(comments))

#2720 --> 1 second
# 241 --> 2 secs
#5080 --> 3 seconds

main()






