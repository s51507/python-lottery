server = 'http://localhost:4723/wd/hub'
desired_caps = {
    'platformName': 'Android',
    'deviceName': 'HWRNE',
    'appPackage': 'com.qygame.lottery',
    'appActivity': '.ui.main.MainActivity'
}

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from time import sleep

driver = webdriver.Remote(server, desired_caps)

rb78 = 690
rb70 = 610
rb60 = 530
rb50 = 450
rb40 = 370
rb30 = 290
rb20 = 210
rb10 = 130
dollar = "com.qygame.lottery:id/rb_dollar"
dime = "com.qygame.lottery:id/rb_dime"
cent = "com.qygame.lottery:id/rb_cent"


def swipeUp():
    size = driver.get_window_size()
    x = size['width'] * 0.5
    driver.swipe(x, size['height'] * 0.75, x, size['height'] * 0.25, 500)
    return


def swipeRight(rebate):
    get_seekbar = driver.find_element_by_id("com.qygame.lottery:id/sb_ratio")
    start = get_seekbar.location.get('x')
    print(start)

    end = get_seekbar.size.get('width')
    print(end)

    ycd = get_seekbar.location.get('y')
    print(ycd)

    TouchAction(driver).press(get_seekbar).move_to(get_seekbar, rebate, 0).release().perform()
    # TouchAction(driver).press(get_seekbar).move_to(get_seekbar, end, ycd).release().perform()
    # TouchAction(driver).press(x=225, y=1580).move_to(x=rebate, y=1580).release().perform()
    return


def clickId(element):
    driver.find_element_by_id(element).click()
    return


def clickXpath(element):
    driver.find_element_by_xpath(element).click()
    return


def getText(element):
    return driver.find_element_by_id(element).text


# 選擇玩法 - 0層
def gameSelect0(num1):
    game1 = "/hierarchy/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[" + num1 + "]/android.widget.TextView"
    clickXpath(game1)
    return


# 選擇玩法 - 1層
def gameSelect1(num1, num2):
    game1 = "/hierarchy/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[" + num1 + "]/android.widget.TextView"
    game2 = "/hierarchy/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView[2]/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[" + num2 + "]/android.widget.TextView"
    clickXpath(game1)
    clickXpath(game2)
    return


# 選擇玩法 - 2層
def gameSelect2(num1, num2, num3):
    game1 = "/hierarchy/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[" + num1 + "]/android.widget.TextView"
    game2 = "/hierarchy/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView[2]/android.widget.RelativeLayout[" + num2 + "]/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[" + num3 + "]/android.widget.TextView"
    clickXpath(game1)
    clickXpath(game2)
    return


# 登入
def login():
    wait = WebDriverWait(driver, 30)
    clickId("com.qygame.lottery:id/ll_personal")
    account = driver.find_element_by_id("com.qygame.lottery:id/ed_account")
    account.clear()
    account.send_keys("ian003")
    password = driver.find_element_by_id("com.qygame.lottery:id/ed_password")
    password.clear()
    password.send_keys("qqq111")
    clickId("com.qygame.lottery:id/btn_login")
    return


def bet():
    # 購彩大廳
    clickId("com.qygame.lottery:id/ll_bet")
    # 重慶時時彩
    clickXpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.ImageView")
    # 選玩法
    clickId("com.qygame.lottery:id/imv_select")
    gameSelect1("1", "1")
    # 選號碼
    sleep(1)
    clickXpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView[2]/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView")
    clickXpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView[2]/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView")
    clickXpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView[2]/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView")
    swipeUp()
    clickXpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView[2]/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView")
    clickXpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[4]/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView[2]/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView")
    # 添加投注
    clickId("com.qygame.lottery:id/btn_betting")
    clickId(cent)
    swipeRight(rb40)
    print('返點：' + getText("com.qygame.lottery:id/tv_rebate") + '\n' +
          '賠率：' + getText("com.qygame.lottery:id/tv_odds") + '\n' +
          '注數：' + getText("com.qygame.lottery:id/tv_total_bet_slip") + '\n' +
          '總金額：' + getText("com.qygame.lottery:id/tv_total_bet_amount"))
    clickId("com.qygame.lottery:id/btn_betting")
    # 確認投注
    clickId("com.qygame.lottery:id/btn_betting")
    print(getText("com.qygame.lottery:id/tv_title") + '\n' +
          '================================================================================================')
    clickId("com.qygame.lottery:id/btn_enter")
    return


login()
bet()
