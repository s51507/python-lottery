from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from re import match

web = webdriver.Chrome()
host = 'http://www.lottery2.lianfa.co'
dot = '#app > div.v-dialog__content.v-dialog__content--active > div > div > div.pa-3.v-card.v-sheet.theme--light > div.ig-betting-slider_main_3k2wQ > div > div > div > div.vue-slider-dot > div.vue-slider-dot-handle'

rb78 = 330
rb70 = 296
rb60 = 253
rb50 = 210
rb40 = 167
rb30 = 125
rb20 = 83
rb10 = 40


# getText
def getText(element):
    return web.find_element_by_css_selector(element).text


# 等待元素出現
def wait(element):
    try:
        WebDriverWait(web, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, element))
        )
    except:
        print('error:' + element + 'not found')
        web.save_screenshot('.\\pic\\error.png')
    return


# 找到元素位置
def find(element):
    targetElem = web.find_element_by_css_selector(element)
    web.execute_script("arguments[0].scrollIntoView();", targetElem)
    return


def click2(element):
    targetElem = web.find_element_by_css_selector(element)
    web.execute_script("arguments[0].click();", targetElem)
    return


# click
def click(btn):
    # print(btn)
    wait(btn)
    newbtn = web.find_element_by_css_selector(btn)
    ActionChains(web).move_to_element(newbtn).click(newbtn).perform()
    # web.find_element_by_css_selector(btn).click()
    return


# 登入
def login():
    web.get(host)
    web.set_window_position(0, 0)
    web.set_window_size(450, 1045)
    click('button[value="info"]')
    sleep(0.5)
    web.find_element_by_css_selector('input[placeholder="请输入用户名"]').send_keys('ian001')
    web.find_element_by_css_selector('input[placeholder="请输入密码"').send_keys('qqq111')
    click('#login > div.flex-layout-column.login-panel > div.login-btn > button')
    wait('#app > div > div > div > div:nth-child(6)')
    wait(
        '#app > div.v-dialog__content.v-dialog__content--active > div > div.ig-dialog__content.v-card.v-sheet.theme--light > div.ig-dialog__title-container > i')
    click(
        '#app > div.v-dialog__content.v-dialog__content--active > div > div.ig-dialog__content.v-card.v-sheet.theme--light > div.ig-dialog__title-container > i')
    return


# 下注
def bet():
    web.get(host + '/#/lottery/bjkl8?lotteryCategoryID=300')
    wait('#bet-area-component-renderer')
    wait(
        '#app > div.application--wrap > div > div.betting-bottom-bar_main_1nOle > div.betting-bottom-bar_container_v7kMX')
    click2('#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(8) > button:nth-child(3)')
    return


login()
bet()
