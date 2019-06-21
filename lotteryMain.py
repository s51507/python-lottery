user = input('請輸入測試帳號：')
pwd = input('請輸入測試密碼：')
from src.lottertBet import login
from src.lotteryGame import *

tmp = 1
login(user, pwd)
print('目前所有彩種如下' + '\n' +
      '----------------------------' + '\n' +
      '時時彩：' + '\n' +
      '\t重慶時時彩 - cqssc 1~3' + '\n' +
      '\t極速時時彩 - jsssc 1~3' + '\n' +
      '\t羅馬時時彩 - lmssc 1~3' + '\n' +
      '\t騰訊分分彩 - txffc 0~7' + '\n' +
      '\t新疆時時彩 - xjssc 1~3' + '\n' +
      '----------------------------' + '\n' +
      'PK10：' + '\n' +
      '\t北京賽車 - bjpk10' + '\n' +
      '\t88賽馬 - horse88' + '\n' +
      '\t極速賽車 - jssc' + '\n' +
      '\t威尼斯賽艇 - wnsst' + '\n' +
      '\t幸運飛艇 - xyft' + '\n' +
      '----------------------------' + '\n' +
      '11選5：' + '\n' +
      '\t廣東11選5 - gdsyxw 1~2' + '\n' +
      '----------------------------' + '\n' +
      '快樂十分：' + '\n' +
      '\t廣東快樂十分 - gdklsf' + '\n' +
      '\t重慶幸運農場(已隱藏) - cqxync' + '\n' +
      '----------------------------' + '\n' +
      '快三：' + '\n' +
      '\t江蘇快三 - jsk3' + '\n' +
      '\t湖北快三 - hbk3' + '\n' +
      '\t吉林快三(已隱藏) - jlk3' + '\n' +
      '----------------------------' + '\n' +
      '3D：' + '\n' +
      '\t福彩3D - fc3d' + '\n' +
      '\t體彩排列三 - pl3' + '\n' +
      '----------------------------' + '\n' +
      '快樂8：' + '\n' +
      '\t北京快樂8 - bjkl8' + '\n' +
      '----------------------------' + '\n' +
      '六合彩：' + '\n' +
      '\t香港六合彩 - hksix 1~3' + '\n' +
      '----------------------------' + '\n')

while tmp > 0:
    game = input('請輸入要測試的彩種 例如:cqssc 1\n')
    if game == 'cqssc 1':
        cqssc('1')
    elif game == 'cqssc 2':
        cqssc('2')
    elif game == 'cqssc 3':
        cqssc('3')
    elif game == 'jsssc 1':
        jsssc('1')
    elif game == 'jsssc 2':
        jsssc('2')
    elif game == 'jsssc 3':
        jsssc('3')
    elif game == 'lmssc 1':
        lmssc('1')
    elif game == 'lmssc 2':
        lmssc('2')
    elif game == 'lmssc 3':
        lmssc('3')
    elif game == 'txffc 0':
        txffc('0')
    elif game == 'txffc 1':
        txffc('1')
    elif game == 'txffc 2':
        txffc('2')
    elif game == 'txffc 3':
        txffc('3')
    elif game == 'txffc 4':
        txffc('4')
    elif game == 'txffc 5':
        txffc('5')
    elif game == 'txffc 6':
        txffc('6')
    elif game == 'txffc 7':
        txffc('7')
    elif game == 'xjssc 1':
        xjssc('1')
    elif game == 'xjssc 2':
        xjssc('2')
    elif game == 'xjssc 3':
        xjssc('3')
    elif game == 'bjpk10':
        bjpk10()
    elif game == 'horse88':
        horse88()
    elif game == 'jssc':
        jssc()
    elif game == 'wnsst':
        wnsst()
    elif game == 'xyft':
        xyft()
    elif game == 'gdsyxw 1':
        gdsyxw('1')
    elif game == 'gdsyxw 2':
        gdsyxw('2')
    elif game == 'gdklsf':
        gdklsf()
    elif game == 'cqxync':
        cqxync()
    elif game == 'jsk3':
        jsk3()
    elif game == 'hbk3':
        hbk3()
    elif game == 'jlk3':
        jlk3()
    elif game == 'fc3d':
        fc3d()
    elif game == 'pl3':
        pl3()
    elif game == 'bjkl8':
        bjkl8()
    elif game == 'hksix 1':
        hksix('1')
    elif game == 'hksix 2':
        hksix('2')
    elif game == 'hksix 3':
        hksix('3')
    else:
        print('?????????????')
