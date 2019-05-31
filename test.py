from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

web = webdriver.Chrome()
host = 'http://www.lottery2.lianfa.co'
dot = '#app > div.v-dialog__content.v-dialog__content--active > div > div > div.pa-3.v-card.v-sheet.theme--light > ' \
      'div.ig-betting-slider_main_3k2wQ > div > ' \
      'div.v-input.v-input--slider.v-input--slider--thumb-label.theme--light.my-0.mx-2 > div > div.v-input__slot > ' \
      'div > div.v-slider__thumb-container.v-slider__thumb-container--show-label > div.v-slider__thumb '

rb78 = 330
rb70 = 296
rb60 = 256
rb50 = 213
rb40 = 170
rb30 = 128
rb20 = 83
rb10 = 43
dollar = '#app > div.v-dialog__content.v-dialog__content--active > div > div > div.pa-3.v-card.v-sheet.theme--light > div.flex-space-between > div.button-group_main_1nnmi > div > button:nth-child(1)'
dime = '#app > div.v-dialog__content.v-dialog__content--active > div > div > div.pa-3.v-card.v-sheet.theme--light > div.flex-space-between > div.button-group_main_1nnmi > div > button:nth-child(2)'
cent = '#app > div.v-dialog__content.v-dialog__content--active > div > div > div.pa-3.v-card.v-sheet.theme--light > div.flex-space-between > div.button-group_main_1nnmi > div > button:nth-child(3)'

cqssc_1 = [
    '10.重慶時時彩-前三-特殊號：豹子、順子、對子_角_6.0%',
    '27',
    [
        '#bet-area-component-renderer > div > div:nth-child(2) > div > button:nth-child(3)'
    ],
    dime,
    rb60
]


# getText
def getText(element):
    return web.find_element_by_css_selector(element).text


# 等待元素出現
def wait(element):
    try:
        WebDriverWait(web, 5).until(
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
    newbtn = web.find_element_by_css_selector(btn)
    ActionChains(web).move_to_element(newbtn).click(newbtn).perform()
    # web.find_element_by_css_selector(btn).click()
    return


# 登入
def login():
    web.get(host)
    web.set_window_position(0, 0)
    web.set_window_size(450, 1045)
    click(
        '#app > div > div > div > div:nth-child(12) > div.bottom-nav_bottom-nav_2bggx.flex-layout-row > div > button:nth-child(4)')
    sleep(0.5)
    web.find_element_by_css_selector('input[placeholder="请输入用户名"]').send_keys('ian002')
    web.find_element_by_css_selector('input[placeholder="请输入密码"').send_keys('qqq111')
    click('#login > div.flex-layout-column.login-panel > div.login-btn > button')
    wait('#app > div > div > div > div:nth-child(6)')
    return


# 登出
def logout():
    web.get(host)
    click(
        '#app > div > div > div > div:nth-child(12) > div.bottom-nav_bottom-nav_2bggx.flex-layout-row > div > button:nth-child(4)')
    click(
        '#app > div > div > div.index_info-content_2RZOR > div.info-bar_bar_1AlVS > div.info-bar_right_3Zuz_ > img.info-bar_setting_W99Z_')
    click('#app > div > div > button')
    wait('#app > div > div > div > div:nth-child(6)')
    web.close()
    return


# 下注
def bet(lottery, game):
    name = game[0]
    Id = game[1]
    nums = game[2]
    money = game[3]
    rebate = game[4]
    print(name)
    web.get(host + '/#/lottery/' + lottery + '?lotteryCategoryID=' + Id)
    wait('#bet-area-component-renderer')
    wait(
        '#app > div.application--wrap > div > div.betting-bottom-bar_main_1nOle > div.betting-bottom-bar_container_v7kMX')
    try:
        web.find_element_by_css_selector('textarea').is_displayed()
        web.find_element_by_css_selector('textarea').send_keys(nums)
    except:
        for num in nums:
            click(num)
    click(
        '#app > div.application--wrap > div > div.betting-bottom-bar_main_1nOle > div.betting-bottom-bar_container_v7kMX > button.v-btn.theme--light.ig-btn_main_2mP9w.betting-bottom-bar_betting_1qX5B')
    wait('.bottom-bar--active')
    sleep(0.5)
    click(money)
    ActionChains(web).drag_and_drop_by_offset(web.find_element_by_css_selector(dot), rebate, 0).perform()
    print('返點：' + getText(
        '#app > div.v-dialog__content.v-dialog__content--active > div > div > div.pa-3.v-card.v-sheet.theme--light > div.ig-betting-slider_main_3k2wQ > span:nth-child(1)') + '\n' +
          '賠率：' + getText(
        '#app > div.v-dialog__content.v-dialog__content--active > div > div > div.pa-3.v-card.v-sheet.theme--light > div.ig-betting-slider_main_3k2wQ > span:nth-child(3)') + '\n' +
          '注數：' + getText(
        '#app > div.application--wrap > div > div.betting-bottom-bar_main_1nOle > div.betting-bottom-bar_container_v7kMX.bottom-bar--active > div > span.mx-2 > span') + '\n' +
          '總金額：' + getText(
        '#app > div.application--wrap > div > div.betting-bottom-bar_main_1nOle > div.betting-bottom-bar_container_v7kMX.bottom-bar--active > div > span.betting-bottom-bar_large_1gi64 > span.ig-primary'))
    click(
        '#app > div.application--wrap > div > div.betting-bottom-bar_main_1nOle > div.betting-bottom-bar_container_v7kMX.bottom-bar--active > button.v-btn.theme--light.ig-btn_main_2mP9w.betting-bottom-bar_betting_1qX5B')
    wait('#bet-list-view')
    wait('#bet-list-view > div.bottom-block > div.betting-bottom-bar_main_1nOle > div > button')
    web.save_screenshot('.\\pic\\' + name + '.png')
    click('#bet-list-view > div.bottom-block > div.betting-bottom-bar_main_1nOle > div > button')
    # 確認有無跳出下注錯誤訊息-未驗證 .alertToast
    try:
        sleep(1.5)
        web.find_element_by_css_selector('.alertToast').is_displayed()
        print('***********' + getText('.alertToast') + '***********')
    except:
        wait('#bet-dialog > div > div.title')
        print(getText('#bet-dialog > div > div.title') + '\n' +
              '================================================================================================')
        click('#bet-dialog > div > div.flex-layout-row.flex-center > button')

    # 確認有無跳出延期訊息　　-未實作 #app > div.v-dialog__content.v-dialog__content--active > div
    # 出現延期點確定　　     -未實作 #app > div.v-dialog__content.v-dialog__content--active > div > div > div.v-card__actions > div > button.ig-dialog__btn.v-btn.v-btn--outline.v-btn--depressed.theme--light.primary--text
    return


login()
bet('cqssc', cqssc_1)