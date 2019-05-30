from lotteryGame import getLottery as gl
from lottertBet import login
from lottertBet import bet


# 重慶時時彩
def cqssc(gameid):
    game = gl('重慶時時彩', 'ssc_' + gameid)
    for now in game:
        bet('cqssc', now)
    return


# 極速時時彩
def jsssc(gameid):
    game = gl('極速時時彩', 'ssc_' + gameid)
    for now in game:
        bet('jsssc', now)
    return


# 羅馬時時彩
def lmssc(gameid):
    game = gl('羅馬時時彩', 'ssc_' + gameid)
    for now in game:
        bet('lmssc', now)
    return


# 騰訊分分彩
def txffc(gameid):
    game = gl('騰訊分分彩', 'ssc_' + gameid)
    for now in game:
        bet('txffc', now)
    return


# 新疆時時彩
def xjssc(gameid):
    game = gl('新疆時時彩', 'ssc_' + gameid)
    for now in game:
        bet('xjssc', now)
    return


# 北京賽車
def bjpk10():
    game = gl('北京賽車', 'pk10')
    for now in game:
        bet('bjpk10', now)
    return


# 88賽馬
def horse88():
    game = gl('88賽馬', 'pk10')
    for now in game:
        bet('horse88', now)
    return


# 極速賽車
def jssc():
    game = gl('極速賽車', 'pk10')
    for now in game:
        bet('jssc', now)
    return


# 威尼斯賽艇
def wnsst():
    game = gl('威尼斯賽艇', 'pk10')
    for now in game:
        bet('wnsst', now)
    return


# 幸運飛艇
def xyft():
    game = gl('幸運飛艇', 'pk10')
    for now in game:
        bet('xyft', now)
    return


#江蘇快三
def jsk3():
    game = gl('江蘇快三', 'k3')
    for now in game:
        bet('jsk3', now)
    return


#湖北快三
def hbk3():
    game = gl('湖北快三', 'k3')
    for now in game:
        bet('hbk3', now)
    return


#吉林快三(還拿不到開獎號不能測)
def jlk3():
    game = gl('吉林快三', 'k3')
    for now in game:
        bet('jlk3', now)
    return


login()
cqssc('1')
#jsk3()