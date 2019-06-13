# python-lottery

## Install

```bash
git clone https://github.com/s51507/python-lottery.git
```

## Manual

```
1. 開啟lotteryMain.py

2. 最下面打上想要測的彩種代碼，時時彩要在括弧內打上玩法編號(1~3)
   例如：sqssc(1) -> 重慶時時彩，畫面上第一排的玩法

3. Shift + F10
```

## Games

```
時時彩　：重慶時時彩(cqssc)、極速時時彩(jsssc)、羅馬時時彩(lmssc)、騰訊分分彩(txffc)、新疆時時彩(xjssc)

PK10　 ：北京賽車(bjpk10)、88賽馬(horse88)、極速賽車(jssc)、威尼斯賽艇(wnsst)、幸運飛艇(xyft)

快三　　：江蘇快三(jsk3)、湖北快三(hbk3)、吉林快三(jlk3)

3D     ：福彩3D(fc3d)、體彩排列三(pl3)

快樂十分：廣東快樂十分(gdklsf)、重慶幸運農場(cqxync)

六合彩  ：香港六合彩(hksix)
```


## Update

```bash
v2.1.01 - fix
          rebate point

v2.1.00 - add
          香港六合彩
          配合六合彩更動下注方式
          
          fix
          修復按鈕有時會按不到的情形

v2.0.00 - add
          Android下注

v1.4.00 - add
          ffc0~7 - 分分彩間格太短，10個一組比較好
          
          fix
          lotteryGame - '37.' + gameName + '-後三-組選包膽：7_角_6.0%' 只能下一注
          lotteryBet - login按鈕改為 - button[value="info"]
          wait - 等待時間增加到20秒

v1.3.02 - add
          lotteryBet - 確認有無跳出下注錯誤訊息

v1.3.01 - fix
          重慶時時彩-龍虎-萬>百
          
          test
          lotteryBet - 確認有無跳出下注錯誤訊息

v1.3.00 - add
          快樂十分系列：廣東快樂十分、重慶幸運農場
          
          尚未實作
          lotteryBet - 確認有無跳出下注錯誤訊息
          lotteryBet - 確認有無跳出延期訊息

v1.2.00 - add
          3D系列：福彩3D、體彩排列三

v1.1.00 - add
          快三系列：江蘇快三、湖北快三、吉林快三

v1.0.00 - add
          時時彩系列：重慶時時彩、極速時時彩、羅馬時時彩、騰訊分分彩、新疆時時彩
          PK10系列：北京賽車、88賽馬、極速賽車、威尼斯賽艇、幸運飛艇

```


## License

The MIT License (MIT)

Copyright © 2019 s51507
