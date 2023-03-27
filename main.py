import time
import os
from fastapi import FastAPI, BackgroundTasks, HTTPException
from pydantic import BaseModel
from extract import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse




import os


SECRET = os.getenv("SECRET")

#
app = FastAPI()

class Msg(BaseModel):
    msg: str
    secret: str


resultado_lista=[]

@app.post('/')
def read_root(texto: str = Form(...)):

    urls = texto

    print(urls)

    url_list=urls.split(" ")

    print(url_list)

    i = -1
    for element in url_list:
        i+=1
        resultado_lista.append({"url": element, "resultado": "", "WRONG_PAGE": "", "IMAGE_HIGH_RESOLUTION": "",
             "INNER_PAGES_NOT_TRANSLATED": "False", "JAVASCRIPT_DROPDOWN": ""})
        '''PATH_TO_DRIVER = '/usr/bin/chromedriver'''''
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.headless = True

        chrome_options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver.get(element)

        time.sleep(2)



        try:

            wrong_page=driver.find_element(By.XPATH,'/html/body/div[1]/header/div[1]/nav/div[1]/button[2]')
            wrong_page.click()
            time.sleep(2)
            resultado_lista[i]={"url": element, "resultado": "", "WRONG_PAGE": "False", "IMAGE_BAD_RESOLUTION": "",
             "INNER_PAGES_NOT_TRANSLATED": "", "JAVASCRIPT_DROPDOWN_NOT_ENABLED": ""}

            image_element = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[1]/div[1]/img')


            try:
                javascript_list = driver.find_element(By.XPATH, '/html/body/div[1]/header/div[1]/nav/div[1]/button[2]')
                javascript_list.click()
                time.sleep(2)
                javascript_list_enabled = driver.find_element(By.XPATH,
                                                              '/html/body/div[1]/header/div[1]/nav/div[1]/nav/div[1]/section[1]/ul/li[2]/a/span[1]')
                javascript_list_enabled.click()

                resultado_lista[i] = {"url": element, "resultado": "", "IMAGE_BAD_RESOLUTION": "",
                                      "INNER_PAGES_NOT_TRANSLATED": "", "JAVASCRIPT_DROPDOWN_NOT_ENABLED": "False"}
                pass

            except:
                resultado_lista[i] = {"url": element, "resultado": "NOT_PASS", "IMAGE_BAD_RESOLUTION": "",
                                      "INNER_PAGES_NOT_TRANSLATED": "", "JAVASCRIPT_DROPDOWN_NOT_ENABLED": "True"}
                pass

            driver.quit()



            pass

        except:
            resultado_lista[i]={"url": element, "resultado": "NOT_PASS", "WRONG_PAGE": "True", "IMAGE_BAD_RESOLUTION": "",
             "INNER_PAGES_NOT_TRANSLATED": "", "JAVASCRIPT_DROPDOWN_NOT_ENABLED": ""}
            pass





    return resultado_lista






