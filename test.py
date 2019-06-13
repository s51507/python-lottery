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

def clickId(element):
    driver.find_element_by_id(element).click()
    return


def clickXpath(element):
    driver.find_element_by_xpath(element).click()
    return


def getText(element):
    return driver.find_element_by_id(element).text


def gameSelect0(num1):
    game1 = "/hierarchy/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[" + num1 + "]/android.widget.TextView"
    clickXpath(game1)
    return


def gameSelect1(num1, num2):
    game1 = "/hierarchy/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[" + num1 + "]/android.widget.TextView"
    game2 = "/hierarchy/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView[2]/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[" + num2 + "]/android.widget.TextView"
    clickXpath(game1)
    clickXpath(game2)
    return


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
