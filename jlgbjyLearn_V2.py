import sys
import os
from tqdm import tqdm
import time
import ddddocr
from selenium import webdriver
from selenium.webdriver.common.alert import Alert

def request_url(username, password, url, driver):
    driver.get(url)
    driver.maximize_window()
    driver.execute_script('window.scrollTo(0, 100);')
    driver.find_element_by_css_selector("#form1 > div > div:nth-child(1) > div > div:nth-child(3) > img").click()
    code = driver.find_element_by_css_selector("#imgcode")
    imgCode = driver.find_element_by_css_selector("#form1 > div > div:nth-child(1) > div > div:nth-child(3) > img")

    ocr = ddddocr.DdddOcr(show_ad=False)
    img_text = ocr.classification(imgCode.screenshot_as_png)
    code.send_keys(img_text)

    driver.find_element_by_css_selector("#name").send_keys(username)
    driver.find_element_by_css_selector("#password").send_keys(password)
    #driver.find_element_by_css_selector("#form1 > div > div:nth-child(1) > div > div:nth-child(4)").click()
    return driver

def login_url(username, password, url):
    options=webdriver.ChromeOptions()
    # options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('useAutomationExtension', False)

    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    options.add_argument('--start-maximized')
    options.add_argument('disable-infobars')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--ignore-certificate-errors-spki-list')
    options.add_argument('--ignore-certificate-errors')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrom_driver_path = "./bin/chromedriver.exe"
    driver = webdriver.Chrome(chrom_driver_path, chrome_options=options)
    driver.get(url)
    while driver.current_url==url:
        try:
            driver = request_url(username, password, url, driver)
        except:
            print("=======login error=======")
            driver.get(url)
            return driver
        try:
            alert = Alert(driver)
            time.sleep(3)
            alert.accept()
            
            alert = Alert(driver)
            time.sleep(3)
            alert.accept()
        except:
            pass
    return driver

def learn(driver):
    try:
        try:
            driver.find_element_by_css_selector("body > div.body-box > div.header > div.nav > ul > li:nth-child(2) > a").click()
        except:
            pass
        try:
            driver.find_element_by_css_selector("body > div.fen_wrap.fen_nav > ul > li:nth-child(2) > a").click()
        except:
            pass
        time.sleep(2)
        ttttt = int(driver.find_element_by_css_selector('#right > div.content > div > div:nth-child(6) > table > tbody > tr:nth-child(2) > td:nth-child(6)').text[:-2])
        learn_width = driver.find_element_by_css_selector("#right > div.content > div > div:nth-child(6) > table > tbody > tr:nth-child(2) > td:nth-child(3) > div > span").size["width"]
        learn_percent = driver.find_element_by_css_selector('#right > div.content > div > div:nth-child(6) > table > tbody > tr:nth-child(2) > td:nth-child(3) > span')
        if learn_percent.text == '100.00%':
            print("学习结束")
            return False
        ttttt = (1-learn_width//10*10/100)*ttttt
        ttttt = int(ttttt)+1
        nnnnn = driver.find_element_by_css_selector('#right > div.content > div > div:nth-child(6) > table > tbody > tr:nth-child(2) > td:nth-child(1)').text
        print(nnnnn+" 还需学习 "+str(ttttt)+" 分钟 ")
        driver.find_element_by_css_selector("#right > div.content > div > div:nth-child(6) > table > tbody > tr:nth-child(2) > td:nth-child(4) > a > img").click()
        handles = driver.window_handles
        driver.switch_to_window(handles[-1])
        time.sleep(2)
        
        frame_list = driver.find_elements_by_tag_name("iframe")
        driver.switch_to_frame(frame_list[0])
        frame_list = driver.find_elements_by_tag_name("iframe")
        driver.switch_to_frame(frame_list[0])
        try:
            driver.find_element_by_css_selector('#play').click()
        except:
            pass
        try:
            driver.find_element_by_css_selector('body > div > div.continue > div.user_choise').click()
        except:
            pass
        time.sleep(2)
        for i in tqdm(range(ttttt*60), dynamic_ncols=True):
            time.sleep(1)
        print("已学完："+nnnnn)
    except:
        pass
    return True

if __name__=="__main__":
    print("=====================================")
    print("# -*- coding: utf-8 -*-")
    print("Created on Sat Nov  3 2023")
    print("@author: Wythe")
    print("=====================================")
    url = r"https://www.jlgbjy.gov.cn/login.jsp"
    print("用户名：")
    username = sys.stdin.readline()
    print("密码：")
    password = sys.stdin.readline()

    os.system('cls')

    PATH_TEMP = os.path.join(os.getcwd(),"bin")

    sys.path.append(PATH_TEMP)

    res = True
    try:
        while res:
            try:
                driver = login_url(username, password, url)
            except:
                print("==========Login in Error==========")
            res = learn(driver)
            driver.quit()
    except:
        print("=============崩溃啦，重新来一遍吧！！！！！！！=============")
        print("=============崩溃啦，重新来一遍吧！！！！！！！=============")
        print("=============崩溃啦，重新来一遍吧！！！！！！！=============")
        print("=============崩溃啦，重新来一遍吧！！！！！！！=============")
        print("=============崩溃啦，重新来一遍吧！！！！！！！=============")
        print("=============崩溃啦，重新来一遍吧！！！！！！！=============")
        print("=============崩溃啦，重新来一遍吧！！！！！！！=============")
        pass

