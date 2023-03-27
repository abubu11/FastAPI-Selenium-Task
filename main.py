import time

from fastapi import FastAPI, BackgroundTasks, HTTPException
from pydantic import BaseModel
from extract import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By




import os


SECRET = os.getenv("SECRET")

#
app = FastAPI()

class Msg(BaseModel):
    msg: str
    secret: str

urls='''https://datta07.github.io/classcentralclone/ 
     https://heartfelt-lollipop-736861.netlify.app/ 
     https://muhammederenaslan.github.io/codingallstars/
     https://exosmotic-bay.000webhostapp.com/
     https://www.facebook.com/'''
expected_language="hi"
resultado_lista=[]

@app.post('/')
def read_root():
    url_list=urls.split("\n")
    i = -1
    for element in url_list:
        i+=1
        print(element)
        resultado_lista.append({"url": element, "resultado": "", "WRONG_PAGE": "", "IMAGE_HIGH_RESOLUTION": "",
             "INNER_PAGES_NOT_TRANSLATED": "False", "JAVASCRIPT_DROPDOWN": ""})
        PATH_TO_DRIVER = "/Users/diegofeslava/Documents/Documentos - MacBook de Abubu/PersonalProjects/FastAPI-Selenium-Task/chromedriver"
        driver= webdriver.Chrome(PATH_TO_DRIVER)
        driver.get(element)

        time.sleep(1)



        try:
            wrong_page=driver.find_element(By.XPATH,'/html/body/div[1]/header/div[1]/nav/div[1]/button[2]')
            wrong_page.click()
            resultado_lista[i]={"url": element, "resultado": "", "WRONG_PAGE": "False", "IMAGE_BAD_RESOLUTION": "",
             "INNER_PAGES_NOT_TRANSLATED": "", "JAVASCRIPT_DROPDOWN_NOT_ENABLED": ""}

            image_element = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[1]/div[1]/img')

            print(image_element.rect)

            try:
                javascript_list = driver.find_element(By.XPATH, '/html/body/div[1]/header/div[1]/nav/div[1]/button[2]')
                javascript_list.click()
                javascript_list_enabled = driver.find_element(By.XPATH,
                                                              '/html/body/div[1]/header/div[1]/nav/div[1]/nav/div[1]/section[1]/ul/li[2]/a/span[1]')
                javascript_list_enabled.click()
                resultado_lista[i] = {"url": element, "resultado": "", "IMAGE_BAD_RESOLUTION": "",
                                      "INNER_PAGES_NOT_TRANSLATED": "", "JAVASCRIPT_DROPDOWN_NOT_ENABLED": "True"}
                pass

            except:
                resultado_lista[i] = {"url": element, "resultado": "", "IMAGE_BAD_RESOLUTION": "",
                                      "INNER_PAGES_NOT_TRANSLATED": "", "JAVASCRIPT_DROPDOWN_NOT_ENABLED": "False"}
                pass

            '''  inner_page=driver.find_element(By.XPATH,'/html/body/div[1]/main/section[1]/div[2]/ul/li[2]/a/span')
            inner_page.click()

            time.sleep(1)

            html_element=driver.find_element(By.TAG_NAME,'html')
            lang_attribute = html_element.get_attribute('lang')

            print(html_element)
            print(lang_attribute)

               driver.quit()

            if lang_attribute == expected_language:
                {"url": element, "resultado": "", "WRONG_PAGE": "", "IMAGE_HIGH_RESOLUTION": "",
                 "INNER_PAGES_NOT_TRANSLATED": "False", "JAVASCRIPT_DROPDOWN": ""}
    '''

            pass

        except:
            resultado_lista[i]={"url": element, "resultado": "NOT_PASS", "WRONG_PAGE": "True", "IMAGE_BAD_RESOLUTION": "",
             "INNER_PAGES_NOT_TRANSLATED": "", "JAVASCRIPT_DROPDOWN_NOT_ENABLED": ""}
            pass





    return resultado_lista






