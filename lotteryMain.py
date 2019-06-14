user = input('請輸入測試帳號：')
pwd = input('請輸入測試密碼：')
from lottertBet import login
import lotteryGame

tmp = 1
login(user, pwd)
print('目前所有彩種如下' + '\n' +
      '時時彩：' + '\n' +
      '重慶時時彩 - cqssc 1~3' + '\n' +
      '極速時時彩 - jsssc 1~3' + '\n' +
      '羅馬時時彩 - lmssc 1~3' + '\n' +
      '騰訊分分彩 - txffc 0~7' + '\n' +
      '新疆時時彩 - xjssc 1~3' + '\n' +
      'PK10：' + '\n' +
      '北京賽車 - bjpk10' + '\n' +
      '88賽馬 - horse88' + '\n' +
      '極速賽車 - jssc' + '\n' +
      '威尼斯賽艇 - wnsst' + '\n' +
      '幸運飛艇 - xyft' + '\n' +
      '11選5：' + '\n' +
      '廣東11選5 - gdsyxw 1~2' + '\n' +
      '快樂十分：' + '\n' +
      '廣東快樂十分 - gdklsf' + '\n' +
      '重慶幸運農場 - cqxync' + '\n' +
      '快三：' + '\n' +
      '江蘇快三 - jsk3' + '\n' +
      '湖北快三 - hbk3' + '\n' +
      '吉林快三 - jlk3' + '\n' +
      '3D：' + '\n' +
      '福彩3D - fc3d' + '\n' +
      '體彩排列三 - pl3' + '\n' +
      '快樂8：' + '\n' +
      '北京快樂8 - bjkl8' + '\n' +
      '六合彩：' + '\n' +
      '香港六合彩 - hksix 1~3' + '\n' +
      '幸運28：' + '\n' +
      '還沒做 - none' + '\n')

while tmp > 0:
    game = input('請輸入要測試的彩種 例如:cqssc 1\n')
    if game == 'cqssc 1':
        lotteryGame.cqssc('1')
    elif game == 'cqssc 2':
        lotteryGame.cqssc('2')
    elif game == 'cqssc 3':
        lotteryGame.cqssc('3')
    elif game == 'jsssc 1':
        lotteryGame.jsssc('1')
    elif game == 'jsssc 2':
        lotteryGame.jsssc('2')
    elif game == 'jsssc 3':
        lotteryGame.jsssc('3')
    elif game == 'lmssc 1':
        lotteryGame.lmssc('1')
    elif game == 'lmssc 2':
        lotteryGame.lmssc('2')
    elif game == 'lmssc 3':
        lotteryGame.lmssc('3')
    elif game == 'txffc 0':
        lotteryGame.txffc('0')
    elif game == 'txffc 1':
        lotteryGame.txffc('1')
    elif game == 'txffc 2':
        lotteryGame.txffc('2')
    elif game == 'txffc 3':
        lotteryGame.txffc('3')
    elif game == 'txffc 4':
        lotteryGame.txffc('4')
    elif game == 'txffc 5':
        lotteryGame.txffc('5')
    elif game == 'txffc 6':
        lotteryGame.txffc('6')
    elif game == 'txffc 7':
        lotteryGame.txffc('7')
    elif game == 'xjssc 1':
        lotteryGame.xjssc('1')
    elif game == 'xjssc 2':
        lotteryGame.xjssc('2')
    elif game == 'xjssc 3':
        lotteryGame.xjssc('3')
    elif game == 'bjpk10':
        lotteryGame.bjpk10()
    elif game == 'horse88':
        lotteryGame.horse88()
    elif game == 'jssc':
        lotteryGame.jssc()
    elif game == 'wnsst':
        lotteryGame.wnsst()
    elif game == 'xyft':
        lotteryGame.xyft()
    elif game == 'gdsyxw 1':
        lotteryGame.gdsyxw('1')
    elif game == 'gdsyxw 2':
        lotteryGame.gdsyxw('2')
    elif game == 'gdklsf':
        lotteryGame.gdklsf()
    elif game == 'cqxync':
        lotteryGame.cqxync()
    elif game == 'jsk3':
        lotteryGame.jsk3()
    elif game == 'hbk3':
        lotteryGame.hbk3()
    elif game == 'jlk3':
        lotteryGame.jlk3()
    elif game == 'fc3d':
        lotteryGame.fc3d()
    elif game == 'pl3':
        lotteryGame.pl3()
    elif game == 'bjkl8':
        lotteryGame.bjkl8()
    elif game == 'hksix 1':
        lotteryGame.hksix('1')
    elif game == 'hksix 2':
        lotteryGame.hksix('2')
    elif game == 'hksix 3':
        lotteryGame.hksix('3')
    elif game == 'pcdd':
        lotteryGame.pcdd()
    else:
        print('?????????????')
