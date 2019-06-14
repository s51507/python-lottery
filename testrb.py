from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

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
    ActionChains(web).move_to_element(web.find_element_by_css_selector(element)).perform()
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
    web.get(host + '/#/lottery/jsk3?lotteryCategoryID=254')
    wait('#bet-area-component-renderer')
    wait(
        '#app > div.application--wrap > div > div.betting-bottom-bar_main_1nOle > div.betting-bottom-bar_container_v7kMX')
    click('#bet-area-component-renderer > div > div:nth-child(2) > div > button')
    click(
        '#app > div.application--wrap > div > div.betting-bottom-bar_main_1nOle > div.betting-bottom-bar_container_v7kMX > button.v-btn.theme--light.ig-btn_main_2mP9w.betting-bottom-bar_betting_1qX5B')
    wait('.bottom-bar--active')
    sleep(0.5)
    ActionChains(web).drag_and_drop_by_offset(web.find_element_by_css_selector(dot), rb78, 0).perform()
    return


print(input('RRRR:')+'aaa')
#login()
#bet()
