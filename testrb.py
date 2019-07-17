from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

web = webdriver.Chrome(r".\\data\\chromedriver.exe")
host = 'http://www.lottery2.lianfa.co'
dot = '#app > div.v-dialog__content.v-dialog__content--active > div > div > div.pa-3.v-card.v-sheet.theme--light > div.ig-betting-slider_main_36re8 > div > div > div > div.vue-slider-dot > div'

rb78 = 345
rb70 = 310
rb60 = 265
rb50 = 220
rb40 = 175
rb30 = 130
rb20 = 85
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
    web.find_element_by_css_selector('input[placeholder="请输入用户名"]').send_keys('ian002')
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
        '#app > div.application--wrap > div > div.betting-bottom-bar_main_3OzhA > div.betting-bottom-bar_container_2FzNa')
    click('#bet-area-component-renderer > div > div:nth-child(2) > div > button')
    click(
        '#app > div.application--wrap > div > div.betting-bottom-bar_main_3OzhA > div.betting-bottom-bar_container_2FzNa > button.v-btn.theme--light.ig-btn_main_2mP9w.betting-bottom-bar_betting_3yJDP')
    wait('.bottom-bar--active')
    sleep(0.5)
    ActionChains(web).drag_and_drop_by_offset(web.find_element_by_css_selector(dot), rb70, 0).perform()
    print('返點：' + getText(
        '#app > div.v-dialog__content.v-dialog__content--active > div > div > div.pa-3.v-card.v-sheet.theme--light > div.ig-betting-slider_main_36re8 > span:nth-child(1)'))
    print('賠率：' + getText(
        '#app > div.v-dialog__content.v-dialog__content--active > div > div > div.pa-3.v-card.v-sheet.theme--light > div.ig-betting-slider_main_36re8 > span:nth-child(3)'))
    print('注數：' + getText(
        '#app > div.application--wrap > div > div.betting-bottom-bar_main_3OzhA > div.betting-bottom-bar_container_2FzNa.bottom-bar--active > div > span.mx-2 > span'))
    print('總金額：' + getText(
        '#app > div.application--wrap > div > div.betting-bottom-bar_main_3OzhA > div.betting-bottom-bar_container_2FzNa.bottom-bar--active > div > span.betting-bottom-bar_large_1PhrE > span.ig-primary'))
    return


login()
bet()
