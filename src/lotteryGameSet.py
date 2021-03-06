rb78 = 345
rb70 = 310
rb60 = 265
rb50 = 220
rb40 = 175
rb30 = 130
rb20 = 85
rb10 = 40
dollar = '#app > div.v-dialog__content.v-dialog__content--active > div > div > div.pa-3.v-card.v-sheet.theme--light > div.flex-space-between > div.button-group_main_2m02p > div > button:nth-child(1)'
dime = '#app > div.v-dialog__content.v-dialog__content--active > div > div > div.pa-3.v-card.v-sheet.theme--light > div.flex-space-between > div.button-group_main_2m02p > div > button:nth-child(2)'
cent = '#app > div.v-dialog__content.v-dialog__content--active > div > div > div.pa-3.v-card.v-sheet.theme--light > div.flex-space-between > div.button-group_main_2m02p > div > button:nth-child(3)'


def ssc_1(gameName):
    return [
        [
            '01.' + gameName + '-五星直選複式：0,0,0,0,0_元_7.8%',
            '4',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div:nth-child(5) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)'
            ],
            dollar,
            rb78
        ],
        [
            '02.' + gameName + '-五星直選單式：5,5,5,5,5_角_7.8%',
            '5',
            '55555',
            dime,
            rb78
        ],
        [
            '03.' + gameName + '-龍虎：萬>百_分_7.8%',
            '6',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > span:nth-child(1)'
            ],
            cent,
            rb78
        ],
        [
            '04.' + gameName + '-前三-直選和值：14_元_7.8%',
            '9',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button:nth-child(5)'
            ],
            dollar,
            rb78
        ],
        [
            '05.' + gameName + '-前三-直選跨度：5_元_7.8%',
            '15',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)'
            ],
            dollar,
            rb78
        ],
        [
            '06.' + gameName + '-前三-直選複式：3,7,8_元_7.8%',
            '197',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(3)',
                '#bet-area-component-renderer > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(4)'
            ],
            dollar,
            rb78
        ],
        [
            '07.' + gameName + '-前三-直選單式：5,6,1_元_7.8%',
            '198',
            '561',
            dollar,
            rb78
        ],
        [
            '08.' + gameName + '-前三-前三組合：1,3,2_元_7.8%',
            '199',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)',
                '#bet-area-component-renderer > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)'
            ],
            dollar,
            rb78
        ],
        [
            '09.' + gameName + '-前三-和值尾數：0,1,2,3,4_角_6.0%',
            '26',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div.button-group_main_1nnmi > div > button:nth-child(3)'
            ],
            dime,
            rb60
        ],
        [
            '10.' + gameName + '-前三-特殊號：豹子、順子、對子_角_6.0%',
            '27',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div > button:nth-child(3)'
            ],
            dime,
            rb60
        ],
        [
            '11.' + gameName + '-前三-組三複式：1,7_分_4.0%',
            '38',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(3)'
            ],
            cent,
            rb40
        ],
        [
            '12.' + gameName + '-前三-組三單式：1,8,8_分_4.0%',
            '39',
            '188',
            cent,
            rb40
        ],
        [
            '13.' + gameName + '-前三-組六複式：2,5,8_分_4.0%',
            '40',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(4)'
            ],
            cent,
            rb40
        ],
        [
            '14.' + gameName + '-前三-組六單式：4,1,7_分_4.0%',
            '41',
            '417',
            cent,
            rb40
        ],
        [
            '15.' + gameName + '-前三-組選和值：13_分_4.0%',
            '43',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button:nth-child(3)'
            ],
            cent,
            rb40
        ],
        [
            '16.' + gameName + '-前三-組選包膽：9_分_4.0%',
            '44',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div > div:nth-child(2) > button:nth-child(5)'
            ],
            cent,
            rb40
        ],
        [
            '17.' + gameName + '-前三-混合組選：6,2,4_分_4.0%',
            '56',
            '624',
            cent,
            rb40
        ],
        [
            '18.' + gameName + '-任三-直選複式：6,8,5,1,_元_7.8%',
            '12',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(4)',
                '#bet-area-component-renderer > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)',
                '#bet-area-component-renderer > div:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)'
            ],
            dollar,
            rb78
        ],
        [
            '19.' + gameName + '-任三-直選單式：百十個 0,7,4_元_7.0%',
            '13',
            '074',
            dollar,
            rb70
        ],
        [
            '20.' + gameName + '-任三-直選和值：百十個 13,14_元_6.0%',
            '14',
            [
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button:nth-child(4)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button:nth-child(5)'
            ],
            dollar,
            rb60
        ],
        [
            '21.' + gameName + '-任三-組六複式：百十個 2,3,5_角_5.0%',
            '50',
            [
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)'
            ],
            dime,
            rb50
        ],
        [
            '22.' + gameName + '-任三-組六單式：百十個 0,6,1_角_4.0%',
            '51',
            '064',
            dime,
            rb40
        ],
        [
            '23.' + gameName + '-任三-組選和值：百十個 14,17_角_3.0%',
            '53',
            [
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button:nth-child(4)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(4) > button:nth-child(2)'
            ],
            dime,
            rb30
        ],
        [
            '24.' + gameName + '-任三-組三複式：百十個 1,2,3_分_2.0%',
            '54',
            [
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)'
            ],
            cent,
            rb20
        ],
        [
            '25.' + gameName + '-任三-組三單式：百十個 4,5,5_分_1.0%',
            '55',
            '455',
            cent,
            rb10
        ],
        [
            '26.' + gameName + '-任三-混合組選：百十個 7,8,9_分_1.0%',
            '57',
            '789',
            cent,
            rb10
        ]
    ]


def ssc_2(gameName):
    return [
        [
            '27.' + gameName + '-後三-後三組合：7,4,9_元_7.8%',
            '18',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(3)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(5)',
                '#bet-area-component-renderer > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(5)'
            ],
            dollar,
            rb78
        ],
        [
            '28.' + gameName + '-後三-直選複式：1,2,3_元_7.8%',
            '42',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)',
                '#bet-area-component-renderer > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)'
            ],
            dollar,
            rb78
        ],
        [
            '29.' + gameName + '-後三-直選單式：4,5,6_元_7.8%',
            '181',
            '456',
            dollar,
            rb78
        ],
        [
            '30.' + gameName + '-後三-直選和值：13,14_元_7.8%',
            '182',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button:nth-child(5)'
            ],
            dollar,
            rb78
        ],
        [
            '31.' + gameName + '-後三-直選跨度：5_元_7.8%',
            '183',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)'
            ],
            dollar,
            rb78
        ],
        [
            '32.' + gameName + '-後三-組三複式：2,5_角_6.0%',
            '185',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)'
            ],
            dime,
            rb60
        ],
        [
            '33.' + gameName + '-後三-組三單式：788_角_6.0%',
            '186',
            '788',
            dime,
            rb60
        ],
        [
            '34.' + gameName + '-後三-組六複式：1,5,9_角_6.0%',
            '187',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(5)'
            ],
            dime,
            rb60
        ],
        [
            '35.' + gameName + '-後三-組六單式：248_角_6.0%',
            '188',
            '248',
            dime,
            rb60
        ],
        [
            '36.' + gameName + '-後三-混合組選：258_角_6.0%',
            '189',
            '258',
            dime,
            rb60
        ],
        [
            '37.' + gameName + '-後三-組選包膽：7_角_6.0%',
            '190',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div > div:nth-child(2) > button:nth-child(3)'
            ],
            dime,
            rb60
        ],
        [
            '38.' + gameName + '-後三-組選和值：15,16_角_6.0%',
            '228',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button:nth-child(5)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(4) > button:nth-child(1)'
            ],
            dime,
            rb60
        ],
        [
            '39.' + gameName + '-後三-和值尾數：0,1,2,3,4_分_4.0%',
            '192',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div.button-group_main_1nnmi > div > button:nth-child(3)'
            ],
            cent,
            rb40
        ],
        [
            '40.' + gameName + '-後三-特殊號：豹子,順子,對子_分_4.0%',
            '193',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div > button:nth-child(3)'
            ],
            cent,
            rb40
        ],
        [
            '41.' + gameName + '-定位膽：百 0_分_2.0%',
            '19',
            [
                '#bet-area-component-renderer > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)'
            ],
            cent,
            rb20
        ],
        [
            '42.' + gameName + '-大小單雙-前三：大,單,小_元_7.8%',
            '21',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div > button:nth-child(1)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div > button:nth-child(3)',
                '#bet-area-component-renderer > div:nth-child(3) > div:nth-child(2) > div > button:nth-child(2)'
            ],
            dollar,
            rb78
        ],
        [
            '43.' + gameName + '-大小單雙-前二：單,雙_元_7.8%',
            '205',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div > button:nth-child(3)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div > button:nth-child(4)'
            ],
            dollar,
            rb78
        ],
        [
            '44.' + gameName + '-大小單雙-後二：小,大_元_7.8%',
            '206',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div > button:nth-child(2)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div > button:nth-child(1)'
            ],
            dollar,
            rb78
        ],
        [
            '45.' + gameName + '-大小單雙-後三：雙,小,單_元_7.8%',
            '207',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div > button:nth-child(4)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div > button:nth-child(2)',
                '#bet-area-component-renderer > div:nth-child(3) > div:nth-child(2) > div > button:nth-child(3)'
            ],
            dollar,
            rb78
        ],
        [
            '46.' + gameName + '-不定膽-前三二碼：0,1_元_7.8%',
            '24',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)'
            ],
            dollar,
            rb78
        ],
        [
            '47.' + gameName + '-不定膽-前三一碼：2_元_7.8%',
            '208',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)'
            ],
            dollar,
            rb78
        ],
        [
            '48.' + gameName + '-不定膽-後三一碼：3_元_7.8%',
            '209',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)'
            ],
            dollar,
            rb78
        ],
        [
            '49.' + gameName + '-不定膽-後三二碼：4,5_元_7.8%',
            '210',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(5)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)'
            ],
            dollar,
            rb78
        ],
        [
            '50.' + gameName + '-不定膽-前四一碼：6_角_7.8%',
            '212',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)'
            ],
            dime,
            rb78
        ],
        [
            '51.' + gameName + '-不定膽-前四二碼：7,8_角_7.8%',
            '213',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(4)'
            ],
            dime,
            rb78
        ],
        [
            '52.' + gameName + '-不定膽-後四一碼：9_角_7.8%',
            '214',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(5)'
            ],
            dime,
            rb78
        ],
        [
            '53.' + gameName + '-不定膽-後四二碼：0,1_角_7.8%',
            '215',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)'
            ],
            dime,
            rb78
        ],
        [
            '54.' + gameName + '-不定膽-五星一碼：2_分_7.8%',
            '217',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)'
            ],
            cent,
            rb78
        ],
        [
            '55.' + gameName + '-不定膽-五星二碼：3,4_分_7.8%',
            '218',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(5)'
            ],
            cent,
            rb78
        ],
        [
            '56.' + gameName + '-不定膽-五星三碼：5,6,7_分_7.8%',
            '219',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(3)'
            ],
            cent,
            rb78
        ]
    ]


def ssc_3(gameName):
    return [
        [
            '57.' + gameName + '-前二-組選複式：0,1,2_元_7.8%',
            '34',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)'
            ],
            dollar,
            rb78
        ],
        [
            '58.' + gameName + '-前二-組選單式：34_元_7.0%',
            '35',
            '34',
            dollar,
            rb70
        ],
        [
            '59.' + gameName + '-前二-組選和值：9,10_元_6.0%',
            '36',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(5)'
            ],
            dollar,
            rb60
        ],
        [
            '60.' + gameName + '-前二-組選包膽：2_元_5.0%',
            '37',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div > div:nth-child(1) > button:nth-child(3)'
            ],
            dollar,
            rb50
        ],
        [
            '61.' + gameName + '-前二-直選複式：2,9_元_4.0%',
            '201',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(5)'
            ],
            dollar,
            rb40
        ],
        [
            '62.' + gameName + '-前二-直選單式：57_元_3.0%',
            '202',
            '57',
            dollar,
            rb30
        ],
        [
            '63.' + gameName + '-前二-直選和值：8,9_元_2.0%',
            '203',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(5)'
            ],
            dollar,
            rb20
        ],
        [
            '64.' + gameName + '-前二-直選跨度：1_元_1.0%',
            '204',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)'
            ],
            dollar,
            rb10
        ],
        [
            '65.' + gameName + '-任選二-組選複式：十個 4,6_角_7.8%',
            '47',
            [
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(5)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)'
            ],
            dime,
            rb78
        ],
        [
            '66.' + gameName + '-任選二-組選單式：十個 23_角_7.8%',
            '48',
            '23',
            dime,
            rb78
        ],
        [
            '67.' + gameName + '-任選二-組選和值：十個 8,9,10_角_7.8%',
            '52',
            [
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(3)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(4)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(5)'
            ],
            dime,
            rb78
        ],
        [
            '68.' + gameName + '-任選二-直選複式：萬千 7,8_角_7.8%',
            '221',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(3)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(4)'
            ],
            dime,
            rb78
        ],
        [
            '69.' + gameName + '-任選二-直選單式：十個 09_角_7.8%',
            '222',
            '09',
            dime,
            rb78
        ],
        [
            '70.' + gameName + '-任選二-直選和值：十個 9,11_角_7.8%',
            '223',
            [
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(5)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button:nth-child(2)'
            ],
            dime,
            rb78
        ],
        [
            '71.' + gameName + '-任選四-組選24：千百十個 0,1,2,3_分_6.0%',
            '60',
            [
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)'
            ],
            cent,
            rb60
        ],
        [
            '72.' + gameName + '-任選四-組選12：千百十個 4,56_分_6.0%',
            '61',
            [
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(5)',
                '#bet-area-component-renderer > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)',
                '#bet-area-component-renderer > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)'
            ],
            cent,
            rb60
        ],
        [
            '73.' + gameName + '-任選四-組選6：千百十個 78_分_6.0%',
            '62',
            [
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(3)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(4)'
            ],
            cent,
            rb60
        ],
        [
            '74.' + gameName + '-任選四-組選4：千百十個 9,0_分_6.0%',
            '63',
            [
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(5)',
                '#bet-area-component-renderer > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)'
            ],
            cent,
            rb60
        ],
        [
            '75.' + gameName + '-任選四-直選複式：萬千百十 1,2,3,4_分_6.0%',
            '225',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)',
                '#bet-area-component-renderer > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)',
                '#bet-area-component-renderer > div:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(5)'
            ],
            cent,
            rb60
        ],
        [
            '76.' + gameName + '-任選四-直選單式：千百十個 5678_分_6.0%',
            '226',
            '5678',
            cent,
            rb60
        ],
        [
            '77.' + gameName + '-四星-直選複式：9,0,1,2_元_7.8%',
            '179',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(5)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)'
            ],
            dollar,
            rb78
        ],
        [
            '78.' + gameName + '-四星-直選單式：3456_元_7.8%',
            '180',
            '3456',
            dollar,
            rb78
        ]
    ]


def ffc_0(gameName):
    return [
        [
            '01.' + gameName + '-五星直選複式：0,0,0,0,0_元_7.8%',
            '4',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div:nth-child(5) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)'
            ],
            dollar,
            rb78
        ],
        [
            '02.' + gameName + '-五星直選單式：5,5,5,5,5_角_7.8%',
            '5',
            '55555',
            dime,
            rb78
        ],
        [
            '03.' + gameName + '-龍虎：萬>百_分_7.8%',
            '6',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > span:nth-child(1)'
            ],
            cent,
            rb78
        ],
        [
            '04.' + gameName + '-前三-直選和值：14_元_7.8%',
            '9',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button:nth-child(5)'
            ],
            dollar,
            rb78
        ],
        [
            '05.' + gameName + '-前三-直選跨度：5_元_7.8%',
            '15',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)'
            ],
            dollar,
            rb78
        ],
        [
            '06.' + gameName + '-前三-直選複式：3,7,8_元_7.8%',
            '197',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(3)',
                '#bet-area-component-renderer > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(4)'
            ],
            dollar,
            rb78
        ],
        [
            '07.' + gameName + '-前三-直選單式：5,6,1_元_7.8%',
            '198',
            '561',
            dollar,
            rb78
        ],
        [
            '08.' + gameName + '-前三-前三組合：1,3,2_元_7.8%',
            '199',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)',
                '#bet-area-component-renderer > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)'
            ],
            dollar,
            rb78
        ],
        [
            '09.' + gameName + '-前三-和值尾數：0,1,2,3,4_角_6.0%',
            '26',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div.button-group_main_1nnmi > div > button:nth-child(3)'
            ],
            dime,
            rb60
        ]
    ]


def ffc_1(gameName):
    return [
        [
            '10.' + gameName + '-前三-特殊號：豹子、順子、對子_角_6.0%',
            '27',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div > button:nth-child(3)'
            ],
            dime,
            rb60
        ],
        [
            '11.' + gameName + '-前三-組三複式：1,7_分_4.0%',
            '38',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(3)'
            ],
            cent,
            rb40
        ],
        [
            '12.' + gameName + '-前三-組三單式：1,8,8_分_4.0%',
            '39',
            '188',
            cent,
            rb40
        ],
        [
            '13.' + gameName + '-前三-組六複式：2,5,8_分_4.0%',
            '40',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(4)'
            ],
            cent,
            rb40
        ],
        [
            '14.' + gameName + '-前三-組六單式：4,1,7_分_4.0%',
            '41',
            '417',
            cent,
            rb40
        ],
        [
            '15.' + gameName + '-前三-組選和值：13_分_4.0%',
            '43',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button:nth-child(3)'
            ],
            cent,
            rb40
        ],
        [
            '16.' + gameName + '-前三-組選包膽：9_分_4.0%',
            '44',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div > div:nth-child(2) > button:nth-child(5)'
            ],
            cent,
            rb40
        ],
        [
            '17.' + gameName + '-前三-混合組選：6,2,4_分_4.0%',
            '56',
            '624',
            cent,
            rb40
        ],
        [
            '18.' + gameName + '-任三-直選複式：6,8,5,1,_元_7.8%',
            '12',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(4)',
                '#bet-area-component-renderer > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)',
                '#bet-area-component-renderer > div:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)'
            ],
            dollar,
            rb78
        ],
        [
            '19.' + gameName + '-任三-直選單式：百十個 0,7,4_元_7.0%',
            '13',
            '074',
            dollar,
            rb70
        ]
    ]


def ffc_2(gameName):
    return [
        [
            '20.' + gameName + '-任三-直選和值：百十個 13,14_元_6.0%',
            '14',
            [
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button:nth-child(4)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button:nth-child(5)'
            ],
            dollar,
            rb60
        ],
        [
            '21.' + gameName + '-任三-組六複式：百十個 2,3,5_角_5.0%',
            '50',
            [
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)'
            ],
            dime,
            rb50
        ],
        [
            '22.' + gameName + '-任三-組六單式：百十個 0,6,1_角_4.0%',
            '51',
            '064',
            dime,
            rb40
        ],
        [
            '23.' + gameName + '-任三-組選和值：百十個 14,17_角_3.0%',
            '53',
            [
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button:nth-child(4)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(4) > button:nth-child(2)'
            ],
            dime,
            rb30
        ],
        [
            '24.' + gameName + '-任三-組三複式：百十個 1,2,3_分_2.0%',
            '54',
            [
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)'
            ],
            cent,
            rb20
        ],
        [
            '25.' + gameName + '-任三-組三單式：百十個 4,5,5_分_1.0%',
            '55',
            '455',
            cent,
            rb10
        ],
        [
            '26.' + gameName + '-任三-混合組選：百十個 7,8,9_分_1.0%',
            '57',
            '789',
            cent,
            rb10
        ],
        [
            '27.' + gameName + '-後三-後三組合：7,4,9_元_7.8%',
            '18',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(3)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(5)',
                '#bet-area-component-renderer > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(5)'
            ],
            dollar,
            rb78
        ],
        [
            '28.' + gameName + '-後三-直選複式：1,2,3_元_7.8%',
            '42',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)',
                '#bet-area-component-renderer > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)'
            ],
            dollar,
            rb78
        ],
        [
            '29.' + gameName + '-後三-直選單式：4,5,6_元_7.8%',
            '181',
            '456',
            dollar,
            rb78
        ]
    ]


def ffc_3(gameName):
    return [
        [
            '30.' + gameName + '-後三-直選和值：13,14_元_7.8%',
            '182',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button:nth-child(5)'
            ],
            dollar,
            rb78
        ],
        [
            '31.' + gameName + '-後三-直選跨度：5_元_7.8%',
            '183',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)'
            ],
            dollar,
            rb78
        ],
        [
            '32.' + gameName + '-後三-組三複式：2,5_角_6.0%',
            '185',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)'
            ],
            dime,
            rb60
        ],
        [
            '33.' + gameName + '-後三-組三單式：788_角_6.0%',
            '186',
            '788',
            dime,
            rb60
        ],
        [
            '34.' + gameName + '-後三-組六複式：1,5,9_角_6.0%',
            '187',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(5)'
            ],
            dime,
            rb60
        ],
        [
            '35.' + gameName + '-後三-組六單式：248_角_6.0%',
            '188',
            '248',
            dime,
            rb60
        ],
        [
            '36.' + gameName + '-後三-混合組選：258_角_6.0%',
            '189',
            '258',
            dime,
            rb60
        ],
        [
            '37.' + gameName + '-後三-組選包膽：7_角_6.0%',
            '190',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div > div:nth-child(2) > button:nth-child(3)'
            ],
            dime,
            rb60
        ],
        [
            '38.' + gameName + '-後三-組選和值：15,16_角_6.0%',
            '228',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button:nth-child(5)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(4) > button:nth-child(1)'
            ],
            dime,
            rb60
        ],
        [
            '39.' + gameName + '-後三-和值尾數：0,1,2,3,4_分_4.0%',
            '192',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div.button-group_main_1nnmi > div > button:nth-child(3)'
            ],
            cent,
            rb40
        ]
    ]


def ffc_4(gameName):
    return [
        [
            '40.' + gameName + '-後三-特殊號：豹子,順子,對子_分_4.0%',
            '193',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div > button:nth-child(3)'
            ],
            cent,
            rb40
        ],
        [
            '41.' + gameName + '-定位膽：百 0_分_2.0%',
            '19',
            [
                '#bet-area-component-renderer > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)'
            ],
            cent,
            rb20
        ],
        [
            '42.' + gameName + '-大小單雙-前三：大,單,小_元_7.8%',
            '21',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div > button:nth-child(1)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div > button:nth-child(3)',
                '#bet-area-component-renderer > div:nth-child(3) > div:nth-child(2) > div > button:nth-child(2)'
            ],
            dollar,
            rb78
        ],
        [
            '43.' + gameName + '-大小單雙-前二：單,雙_元_7.8%',
            '205',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div > button:nth-child(3)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div > button:nth-child(4)'
            ],
            dollar,
            rb78
        ],
        [
            '44.' + gameName + '-大小單雙-後二：小,大_元_7.8%',
            '206',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div > button:nth-child(2)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div > button:nth-child(1)'
            ],
            dollar,
            rb78
        ],
        [
            '45.' + gameName + '-大小單雙-後三：雙,小,單_元_7.8%',
            '207',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div > button:nth-child(4)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div > button:nth-child(2)',
                '#bet-area-component-renderer > div:nth-child(3) > div:nth-child(2) > div > button:nth-child(3)'
            ],
            dollar,
            rb78
        ],
        [
            '46.' + gameName + '-不定膽-前三二碼：0,1_元_7.8%',
            '24',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)'
            ],
            dollar,
            rb78
        ],
        [
            '47.' + gameName + '-不定膽-前三一碼：2_元_7.8%',
            '208',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)'
            ],
            dollar,
            rb78
        ],
        [
            '48.' + gameName + '-不定膽-後三一碼：3_元_7.8%',
            '209',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)'
            ],
            dollar,
            rb78
        ],
        [
            '49.' + gameName + '-不定膽-後三二碼：4,5_元_7.8%',
            '210',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(5)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)'
            ],
            dollar,
            rb78
        ]
    ]


def ffc_5(gameName):
    return [
        [
            '50.' + gameName + '-不定膽-前四一碼：6_角_7.8%',
            '212',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)'
            ],
            dime,
            rb78
        ],
        [
            '51.' + gameName + '-不定膽-前四二碼：7,8_角_7.8%',
            '213',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(4)'
            ],
            dime,
            rb78
        ],
        [
            '52.' + gameName + '-不定膽-後四一碼：9_角_7.8%',
            '214',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(5)'
            ],
            dime,
            rb78
        ],
        [
            '53.' + gameName + '-不定膽-後四二碼：0,1_角_7.8%',
            '215',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)'
            ],
            dime,
            rb78
        ],
        [
            '54.' + gameName + '-不定膽-五星一碼：2_分_7.8%',
            '217',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)'
            ],
            cent,
            rb78
        ],
        [
            '55.' + gameName + '-不定膽-五星二碼：3,4_分_7.8%',
            '218',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(5)'
            ],
            cent,
            rb78
        ],
        [
            '56.' + gameName + '-不定膽-五星三碼：5,6,7_分_7.8%',
            '219',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(3)'
            ],
            cent,
            rb78
        ],
        [
            '57.' + gameName + '-前二-組選複式：0,1,2_元_7.8%',
            '34',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)'
            ],
            dollar,
            rb78
        ],
        [
            '58.' + gameName + '-前二-組選單式：34_元_7.0%',
            '35',
            '34',
            dollar,
            rb70
        ],
        [
            '59.' + gameName + '-前二-組選和值：9,10_元_6.0%',
            '36',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(5)'
            ],
            dollar,
            rb60
        ]
    ]


def ffc_6(gameName):
    return [
        [
            '60.' + gameName + '-前二-組選包膽：2_元_5.0%',
            '37',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div > div:nth-child(1) > button:nth-child(3)'
            ],
            dollar,
            rb50
        ],
        [
            '61.' + gameName + '-前二-直選複式：2,9_元_4.0%',
            '201',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(5)'
            ],
            dollar,
            rb40
        ],
        [
            '62.' + gameName + '-前二-直選單式：57_元_3.0%',
            '202',
            '57',
            dollar,
            rb30
        ],
        [
            '63.' + gameName + '-前二-直選和值：8,9_元_2.0%',
            '203',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(5)'
            ],
            dollar,
            rb20
        ],
        [
            '64.' + gameName + '-前二-直選跨度：1_元_1.0%',
            '204',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)'
            ],
            dollar,
            rb10
        ],
        [
            '65.' + gameName + '-任選二-組選複式：十個 4,6_角_7.8%',
            '47',
            [
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(5)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)'
            ],
            dime,
            rb78
        ],
        [
            '66.' + gameName + '-任選二-組選單式：十個 23_角_7.8%',
            '48',
            '23',
            dime,
            rb78
        ],
        [
            '67.' + gameName + '-任選二-組選和值：十個 8,9,10_角_7.8%',
            '52',
            [
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(3)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(4)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(5)'
            ],
            dime,
            rb78
        ],
        [
            '68.' + gameName + '-任選二-直選複式：萬千 7,8_角_7.8%',
            '221',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(3)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(4)'
            ],
            dime,
            rb78
        ],
        [
            '69.' + gameName + '-任選二-直選單式：十個 09_角_7.8%',
            '222',
            '09',
            dime,
            rb78
        ]
    ]


def ffc_7(gameName):
    return [
        [
            '70.' + gameName + '-任選二-直選和值：十個 9,11_角_7.8%',
            '223',
            [
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(5)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button:nth-child(2)'
            ],
            dime,
            rb78
        ],
        [
            '71.' + gameName + '-任選四-組選24：千百十個 0,1,2,3_分_6.0%',
            '60',
            [
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)'
            ],
            cent,
            rb60
        ],
        [
            '72.' + gameName + '-任選四-組選12：千百十個 4,56_分_6.0%',
            '61',
            [
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(5)',
                '#bet-area-component-renderer > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)',
                '#bet-area-component-renderer > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)'
            ],
            cent,
            rb60
        ],
        [
            '73.' + gameName + '-任選四-組選6：千百十個 78_分_6.0%',
            '62',
            [
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(3)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(4)'
            ],
            cent,
            rb60
        ],
        [
            '74.' + gameName + '-任選四-組選4：千百十個 9,0_分_6.0%',
            '63',
            [
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(5)',
                '#bet-area-component-renderer > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)'
            ],
            cent,
            rb60
        ],
        [
            '75.' + gameName + '-任選四-直選複式：萬千百十 1,2,3,4_分_6.0%',
            '225',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)',
                '#bet-area-component-renderer > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)',
                '#bet-area-component-renderer > div:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(5)'
            ],
            cent,
            rb60
        ],
        [
            '76.' + gameName + '-任選四-直選單式：千百十個 5678_分_6.0%',
            '226',
            '5678',
            cent,
            rb60
        ],
        [
            '77.' + gameName + '-四星-直選複式：9,0,1,2_元_7.8%',
            '179',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(5)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)'
            ],
            dollar,
            rb78
        ],
        [
            '78.' + gameName + '-四星-直選單式：3456_元_7.8%',
            '180',
            '3456',
            dollar,
            rb78
        ]
    ]


def pk10(gameName):
    return [
        [
            '01.' + gameName + '-龍虎-冠軍：龍_元_7.0%',
            '68',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div > button:nth-child(1)'
            ],
            dollar,
            rb70
        ],
        [
            '02.' + gameName + '-龍虎-亞軍：龍_元_6.0%',
            '69',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div > button:nth-child(1)'
            ],
            dollar,
            rb60
        ],
        [
            '03.' + gameName + '-龍虎-季軍：龍_元_5.0%',
            '70',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div > button:nth-child(1)'
            ],
            dollar,
            rb50
        ],
        [
            '04.' + gameName + '-龍虎-第四名：龍_角_4.0%',
            '71',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div > button:nth-child(1)'
            ],
            dime,
            rb40
        ],
        [
            '05.' + gameName + '-龍虎-第五名：虎_角_3.0%',
            '72',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div > button:nth-child(2)'
            ],
            dime,
            rb30
        ],
        [
            '06.' + gameName + '-龍虎-冠亞軍：虎_分_2.0%',
            '73',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div > button:nth-child(2)'
            ],
            cent,
            rb20
        ],
        [
            '07.' + gameName + '-龍虎-冠亞季軍：虎_分_1.0%',
            '74',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div > button:nth-child(2)'
            ],
            cent,
            rb10
        ],
        [
            '08.' + gameName + '-大小單雙-冠軍：大_元_7.8%',
            '77',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div > button:nth-child(1)'
            ],
            dollar,
            rb78
        ],
        [
            '09.' + gameName + '-大小單雙-亞軍：大_元_7.8%',
            '78',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div > button:nth-child(1)'
            ],
            dollar,
            rb78
        ],
        [
            '10.' + gameName + '-大小單雙-季軍：大_元_7.8%',
            '79',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div > button:nth-child(1)'
            ],
            dollar,
            rb78
        ],
        [
            '11.' + gameName + '-大小單雙-第四名：小_元_7.8%',
            '80',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div > button:nth-child(2)'
            ],
            dollar,
            rb78
        ],
        [
            '12.' + gameName + '-大小單雙-第五名：小_角_6.0%',
            '81',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div > button:nth-child(2)'
            ],
            dime,
            rb60
        ],
        [
            '13.' + gameName + '-大小單雙-第六名：小_角_6.0%',
            '82',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div > button:nth-child(2)'
            ],
            dime,
            rb60
        ],
        [
            '14.' + gameName + '-大小單雙-第七名：單_角_6.0%',
            '83',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div > button:nth-child(3)'
            ],
            dime,
            rb60
        ],
        [
            '15.' + gameName + '-大小單雙-第八名：單_角_6.0%',
            '84',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div > button:nth-child(3)'
            ],
            dime,
            rb60
        ],
        [
            '16.' + gameName + '-大小單雙-第九名：單_分_4.0%',
            '85',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div > button:nth-child(3)'
            ],
            cent,
            rb40
        ],
        [
            '17.' + gameName + '-大小單雙-第十名：雙_分_4.0%',
            '86',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div > button:nth-child(4)'
            ],
            cent,
            rb40
        ],
        [
            '18.' + gameName + '-大小單雙-冠亞：雙_分_4.0%',
            '87',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div > button:nth-child(4)'
            ],
            cent,
            rb40
        ],
        [
            '19.' + gameName + '-大小單雙-冠亞季：雙_分_4.0%',
            '88',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div > button:nth-child(4)'
            ],
            cent,
            rb40
        ],
        [
            '20.' + gameName + '-不定膽-冠亞季選一：1,2_元_2.0%',
            '91',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)'
            ],
            dollar,
            rb20
        ],
        [
            '21.' + gameName + '-不定膽-冠亞季選二：1,2,3,4,5_元_1.0%',
            '92',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div.button-group_main_1nnmi > div > button:nth-child(3)'
            ],
            dollar,
            rb10
        ],
        [
            '22.' + gameName + '-定位膽：冠軍 1,2,3,4,5_元_7.8%',
            '93',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div.button-group_main_1nnmi > div > button:nth-child(3)'
            ],
            dollar,
            rb78
        ],
        [
            '23.' + gameName + '-猜冠軍：6,7,8,9,10_元_7.0%',
            '94',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div.button-group_main_1nnmi > div > button:nth-child(2)'
            ],
            dollar,
            rb70
        ],
        [
            '24.' + gameName + '-猜冠亞軍-直選複式：7,10_元_6.0%',
            '97',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(5)'
            ],
            dollar,
            rb60
        ],
        [
            '25.' + gameName + '-猜冠亞軍-直選單式：87_角_5.0%',
            '98',
            '0807',
            dime,
            rb50
        ],
        [
            '26.' + gameName + '-猜冠亞軍-直選和值：11_分_4.0%',
            '111',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(4)'
            ],
            cent,
            rb40
        ],
        [
            '27.' + gameName + '-猜冠亞季軍-直選複式：5,7,4_元_3.0%',
            '101',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(5)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)',
                '#bet-area-component-renderer > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)'
            ],
            dollar,
            rb30
        ],
        [
            '28.' + gameName + '-猜冠亞季軍-直選單式：652_角_2.0%',
            '102',
            '060502',
            dime,
            rb20
        ],
        [
            '29.' + gameName + '-猜冠亞季軍-直選和值：15,16,17,18_分_1.0%',
            '112',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(5)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button:nth-child(3)',
            ],
            cent,
            rb10
        ]
    ]


def k3(gameName):
    return [
        [
            '01.' + gameName + '-三同號-通選：三同號通選_元_7.8%',
            '254',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div > button'
            ],
            dollar,
            rb78
        ],
        [
            '02.' + gameName + '-三同號-單選：111,333,555_元_7.8%',
            '255',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(5)'
            ],
            dollar,
            rb78
        ],
        [
            '03.' + gameName + '-二同號-複選：22,44,66_元_7.8%',
            '258',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button'
            ],
            dollar,
            rb78
        ],
        [
            '04.' + gameName + '-二同號-單選：33,2_元_7.8%',
            '259',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div > div:nth-child(1) > button:nth-child(2)'
            ],
            dollar,
            rb78
        ],
        [
            '05.' + gameName + '-三不同號-標準：1,2,3,4,5,6_角_6.0%',
            '262',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div.button-group_main_1nnmi > div > button:nth-child(1)'
            ],
            dime,
            rb60
        ],
        [
            '06.' + gameName + '-三不同號-膽拖：24,5_角_6.0%',
            '263',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(1) > button:nth-child(4)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(5)'
            ],
            dime,
            rb60
        ],
        [
            '07.' + gameName + '-二不同號-標準：1,3,4_角_6.0%',
            '266',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)'
            ],
            dime,
            rb60
        ],
        [
            '08.' + gameName + '-二不同號-膽拖：2,45_角_6.0%',
            '267',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(5)'
            ],
            dime,
            rb60
        ],
        [
            '09.' + gameName + '-三連號：三連號通選_分_4.0%',
            '268',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div > button'
            ],
            cent,
            rb40
        ],
        [
            '10.' + gameName + '-和值-大小單雙：小_分_4.0%',
            '269',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div > button:nth-child(2)'
            ],
            cent,
            rb40
        ],
        [
            '11.' + gameName + '-和值-直選和值：10,11_分_4.0%',
            '270',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(4)'
            ],
            cent,
            rb40
        ]
    ]


def td(gameName):
    return [
        [
            '01.' + gameName + '-三星-直選複式：0,6,1_元_7.8%',
            '275',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)',
                '#bet-area-component-renderer > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)'
            ],
            dollar,
            rb78
        ],
        [
            '02.' + gameName + '-三星-直選單式：873_元_7.8%',
            '276',
            '873',
            dollar,
            rb78
        ],
        [
            '03.' + gameName + '-三星-直選和值：13,14_元_7.8%',
            '277',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button:nth-child(5)'
            ],
            dollar,
            rb78
        ],
        [
            '04.' + gameName + '-三星-組三複式：1,2,8_元_6.0%',
            '278',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(4)'
            ],
            dollar,
            rb60
        ],
        [
            '05.' + gameName + '-三星-組六複式：3,6,8,9_元_6.0%',
            '279',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(5)'
            ],
            dollar,
            rb60
        ],
        [
            '06.' + gameName + '-三星-組三和值：12,15_元_6.0%',
            '280',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button:nth-child(5)'
            ],
            dollar,
            rb60
        ],
        [
            '07.' + gameName + '-三星-組六和值：11,21_元_6.0%',
            '281',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(4) > button:nth-child(4)'
            ],
            dollar,
            rb60
        ],
        [
            '08.' + gameName + '-二星-前二直選複式：8,7_角_4.0%',
            '285',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(4)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(3)'
            ],
            dime,
            rb40
        ],
        [
            '09.' + gameName + '-二星-後二直選複式：6,3_角_4.0%',
            '286',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)'
            ],
            dime,
            rb40
        ],
        [
            '10.' + gameName + '-二星-前二組選複式：5,6_角_4.0%',
            '287',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)'
            ],
            dime,
            rb40
        ],
        [
            '11.' + gameName + '-二星-後二組選複式：0,9_角_4.0%',
            '288',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(5)'
            ],
            dime,
            rb40
        ],
        [
            '12.' + gameName + '-定位膽：9,7,8_角_2.0%',
            '289',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(5)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(3)',
                '#bet-area-component-renderer > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(4)'
            ],
            dime,
            rb20
        ],
        [
            '13.' + gameName + '-不定膽-一碼：2_分_2.0%',
            '292',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)'
            ],
            cent,
            rb20
        ],
        [
            '14.' + gameName + '-不定膽-二碼：3,5_分_2.0%',
            '293',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)'
            ],
            cent,
            rb20
        ],
        [
            '15.' + gameName + '-大小單雙-前二大小單雙：大,小_分_2.0%',
            '296',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div > button:nth-child(1)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div > button:nth-child(2)'
            ],
            cent,
            rb20
        ],
        [
            '16.' + gameName + '-大小單雙-後二大小單雙：單,雙_分_2.0%',
            '297',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div > button:nth-child(3)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div > button:nth-child(4)'
            ],
            cent,
            rb20
        ]
    ]


def klsf(gameName):
    return [
        [
            '01.' + gameName + '-選一-數投：1~18_元_7.8%',
            '231',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div.button-group_main_1nnmi > div > button:nth-child(1)'
            ],
            dollar,
            rb78
        ],
        [
            '02.' + gameName + '-選一-紅投：19_元_7.8%',
            '232',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div > div > button:nth-child(1)'
            ],
            dollar,
            rb78
        ],
        [
            '03.' + gameName + '-選二-任選二：4,6,19_元_7.8%',
            '234',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(4) > button:nth-child(4)'
            ],
            dollar,
            rb78
        ],
        [
            '04.' + gameName + '-選二-任選膽拖：8|9,12_元_7.8%',
            '235',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(2) > button:nth-child(3)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(4)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button:nth-child(2)'
            ],
            dollar,
            rb78
        ],
        [
            '05.' + gameName + '-選二-連組：8,15,19_元_7.8%',
            '236',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button:nth-child(5)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(4) > button:nth-child(4)'
            ],
            dollar,
            rb78
        ],
        [
            '06.' + gameName + '-選二-連組膽拖：11|4,18_元_7.8%',
            '237',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(3) > button:nth-child(1)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(4) > button:nth-child(3)'
            ],
            dollar,
            rb78
        ],
        [
            '07.' + gameName + '-選二-連直：1|6,10_元_7.8%',
            '238',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(5)'
            ],
            dollar,
            rb78
        ],
        [
            '08.' + gameName + '-選三-任選：16,17,18,19,20_角_6.0%',
            '240',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(4) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(4) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(4) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(4) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(4) > button:nth-child(5)'
            ],
            dime,
            rb60
        ],
        [
            '09.' + gameName + '-選三-任選膽拖：19|2,7,12_角_6.0%',
            '241',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(4) > button:nth-child(4)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button:nth-child(2)'
            ],
            dime,
            rb60
        ],
        [
            '10.' + gameName + '-選三-前組：9,12,15_角_6.0%',
            '242',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button:nth-child(5)'
            ],
            dime,
            rb60
        ],
        [
            '11.' + gameName + '-選三-前組膽拖：1|8,13,18_角_6.0%',
            '243',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(3)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button:nth-child(3)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(4) > button:nth-child(3)'
            ],
            dime,
            rb60
        ],
        [
            '12.' + gameName + '-選三-前直：14,7,2_角_6.0%',
            '244',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button:nth-child(4)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)',
                '#bet-area-component-renderer > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)'
            ],
            dime,
            rb60
        ],
        [
            '13.' + gameName + '-選四-任選：1,7,13,19_分_4.0%',
            '246',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(4) > button:nth-child(4)'
            ],
            cent,
            rb40
        ],
        [
            '14.' + gameName + '-選四-任選膽拖：5,9,13|1_分_4.0%',
            '247',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(1) > button:nth-child(5)',
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(2) > button:nth-child(4)',
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(3) > button:nth-child(3)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)'
            ],
            cent,
            rb40
        ],
        [
            '15.' + gameName + '-選五-任選：3,8,12,14,16,20_分_4.0%',
            '249',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(4) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(4) > button:nth-child(5)'
            ],
            cent,
            rb40
        ],
        [
            '16.' + gameName + '-選五-任選膽拖：1,7,13,19|5_分_4.0%',
            '250',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(2) > button:nth-child(2)',
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(3) > button:nth-child(3)',
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(4) > button:nth-child(4)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(5)'
            ],
            cent,
            rb40
        ]
    ]


def six_1(gameName):
    return [
        [
            '01.' + gameName + '-特碼-A：1_元',
            '336',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)'
            ],
            dollar
        ],
        [
            '02.' + gameName + '-特碼-B：2_元',
            '337',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)'
            ],
            dollar
        ],
        [
            '03.' + gameName + '-正碼-A：3_元',
            '339',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)'
            ],
            dollar
        ],
        [
            '04.' + gameName + '-正碼-B：4_元',
            '340',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)'
            ],
            dollar
        ],
        [
            '05.' + gameName + '-正特碼-正一特：5_元',
            '342',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(5)'
            ],
            dollar
        ],
        [
            '06.' + gameName + '-正特碼-正二特：6_元',
            '343',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)'
            ],
            dollar
        ],
        [
            '07.' + gameName + '-正特碼-正三特：7_元',
            '344',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)'
            ],
            dollar
        ],
        [
            '08.' + gameName + '-正特碼-正四特：8_元',
            '345',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(3)'
            ],
            dollar
        ],
        [
            '09.' + gameName + '-正特碼-正五特：9_元',
            '346',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(4)'
            ],
            dollar
        ],
        [
            '10.' + gameName + '-正特碼-正六特：10_元',
            '347',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(5)'
            ],
            dollar
        ],
        [
            '11.' + gameName + '-正碼1至6-正一碼：大_元',
            '349',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)'
            ],
            dollar
        ],
        [
            '12.' + gameName + '-正碼1至6-正二碼：小_元',
            '350',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)'
            ],
            dollar
        ],
        [
            '13.' + gameName + '-正碼1至6-正三碼：單_元',
            '351',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)'
            ],
            dollar
        ],
        [
            '14.' + gameName + '-正碼1至6-正四碼：雙_元',
            '352',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)'
            ],
            dollar
        ],
        [
            '15.' + gameName + '-正碼1至6-正五碼：紅波_元',
            '353',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(5)'
            ],
            dollar
        ],
        [
            '16.' + gameName + '-正碼1至6-正六碼：藍波_元',
            '354',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)'
            ],
            dollar
        ]
    ]


def six_2(gameName):
    return [
        [
            '17.' + gameName + '-連碼-三全中：7,13,19_元',
            '356',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(3) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(4) > button:nth-child(4)'
            ],
            dollar
        ],
        [
            '18.' + gameName + '-連碼-三中二：2,8,14_元',
            '357',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div > div:nth-child(2) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div > div:nth-child(3) > button:nth-child(4)'
            ],
            dollar
        ],
        [
            '19.' + gameName + '-連碼-二全中：27,33_元',
            '358',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(6) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(7) > button:nth-child(3)'
            ],
            dollar
        ],
        [
            '20.' + gameName + '-連碼-二中特：39,43_元',
            '359',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div > div:nth-child(8) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div > div:nth-child(9) > button:nth-child(3)'
            ],
            dollar
        ],
        [
            '21.' + gameName + '-連碼-特串：15,30_元',
            '360',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(3) > button:nth-child(5)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(6) > button:nth-child(5)'
            ],
            dollar
        ],
        [
            '22.' + gameName + '-連碼-四中一：7,19,28,40_元',
            '361',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(4) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(6) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(8) > button:nth-child(5)'
            ],
            dollar
        ],
        [
            '23.' + gameName + '-半波：藍雙_元',
            '362',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(5)'
            ],
            dollar
        ],
        [
            '24.' + gameName + '-一肖/尾數：猴_元',
            '363',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(4)'
            ],
            dollar
        ],
        [
            '25.' + gameName + '-特肖：豬_元',
            '364',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(3) > button:nth-child(4)'
            ],
            dollar
        ]
    ]


def six_3(gameName):
    return [
        [
            '26.' + gameName + '-合肖-二肖：鼠牛_元',
            '366',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)'
            ],
            dollar
        ],
        [
            '27.' + gameName + '-合肖-三肖：鼠牛虎_元',
            '367',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)'
            ],
            dollar
        ],
        [
            '28.' + gameName + '-合肖-四肖：鼠牛虎兔_元',
            '368',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)'
            ],
            dollar
        ],
        [
            '29.' + gameName + '-合肖-五肖：鼠牛虎兔龍_元',
            '369',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)'
            ],
            dollar
        ],
        [
            '30.' + gameName + '-合肖-六肖：鼠牛虎兔龍蛇_元',
            '370',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)'
            ],
            dollar
        ],
        [
            '31.' + gameName + '-合肖-七肖：鼠牛虎兔龍蛇馬_元',
            '371',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(3)'
            ],
            dollar
        ],
        [
            '32.' + gameName + '-合肖-八肖：鼠牛虎兔龍蛇馬羊_元',
            '372',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(4)'
            ],
            dollar
        ],
        [
            '33.' + gameName + '-合肖-九肖：鼠牛虎兔龍蛇馬羊猴_元',
            '373',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(3) > button:nth-child(1)'
            ],
            dollar
        ],
        [
            '34.' + gameName + '-合肖-十肖：鼠牛虎兔龍蛇馬羊猴雞_元',
            '374',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(3) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(3) > button:nth-child(2)'
            ],
            dollar
        ],
        [
            '35.' + gameName + '-合肖-十一肖：鼠牛虎兔龍蛇馬羊猴雞狗_元',
            '375',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(3) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(3) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(3) > button:nth-child(3)'
            ],
            dollar
        ],
        [
            '36.' + gameName + '-連肖-二肖連中：鼠牛_元',
            '377',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)'
            ],
            dollar
        ],
        [
            '37.' + gameName + '-連肖-三肖連中：鼠牛虎_元',
            '378',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)'
            ],
            dollar
        ],
        [
            '38.' + gameName + '-連肖-四肖連中：鼠牛虎兔_元',
            '379',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)'
            ],
            dollar
        ],
        [
            '39.' + gameName + '-連肖-五肖連中：鼠牛虎兔龍_元',
            '380',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)'
            ],
            dollar
        ],
        [
            '40.' + gameName + '-連肖-二肖連不中：鼠牛_元',
            '381',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)'
            ],
            dollar
        ],
        [
            '41.' + gameName + '-連肖-三肖連不中：鼠牛虎_元',
            '382',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)'
            ],
            dollar
        ],
        [
            '42.' + gameName + '-連肖-四肖連不中：鼠牛虎兔_元',
            '383',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)'
            ],
            dollar
        ],
        [
            '43.' + gameName + '-尾數連-二尾連中：0,1_元',
            '385',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)'
            ],
            dollar
        ],
        [
            '44.' + gameName + '-尾數連-三尾連中：2,3,4_元',
            '386',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(5)'
            ],
            dollar
        ],
        [
            '45.' + gameName + '-尾數連-四尾連中：5,6,7,8_元',
            '387',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(4)'
            ],
            dollar
        ],
        [
            '46.' + gameName + '-尾數連-二尾連不中：0,9_元',
            '388',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(5)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)'
            ],
            dollar
        ],
        [
            '47.' + gameName + '-尾數連-三尾連不中：1,2,3_元',
            '389',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)'
            ],
            dollar
        ],
        [
            '48.' + gameName + '-尾數連-四尾連不中：4,5,6,7_元',
            '390',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(5)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(3)'
            ],
            dollar
        ],
        [
            '49.' + gameName + '-全不中-五不中：1,2,3,4,5_元',
            '392',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(5)'
            ],
            dollar
        ],
        [
            '50.' + gameName + '-全不中-六不中：6,7,8,9,10,11_元',
            '393',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(5)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(3) > button:nth-child(1)'
            ],
            dollar
        ],
        [
            '51.' + gameName + '-全不中-七不中：12~18_元',
            '394',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(3) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(3) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(3) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(3) > button:nth-child(5)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(4) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(4) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(4) > button:nth-child(3)'
            ],
            dollar
        ],
        [
            '52.' + gameName + '-全不中-八不中：19~26_元',
            '395',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(4) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(4) > button:nth-child(5)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(5) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(5) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(5) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(5) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(5) > button:nth-child(5)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(6) > button:nth-child(1)'
            ],
            dollar
        ],
        [
            '53.' + gameName + '-全不中-九不中：27~35_元',
            '396',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(6) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(6) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(6) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(6) > button:nth-child(5)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(7) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(7) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(7) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(7) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(7) > button:nth-child(5)'
            ],
            dollar
        ],
        [
            '54.' + gameName + '-全不中-十不中：36~45_元',
            '397',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(8) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(8) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(8) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(8) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(8) > button:nth-child(5)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(9) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(9) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(9) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(9) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(9) > button:nth-child(5)'
            ],
            dollar
        ],
        [
            '55.' + gameName + '-全不中-十一不中：1,6,11,16,21,26,31,36,41,46,49_元',
            '398',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(3) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(4) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(5) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(6) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(7) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(8) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(9) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(10) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(10) > button:nth-child(4)'
            ],
            dollar
        ],
        [
            '56.' + gameName + '-全不中-十二不中：3,4,8,9,13,18,23,28,33,38,43,48_元',
            '399',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(3) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(4) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(5) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(6) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(7) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(8) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(9) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(10) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(4)'
            ],
            dollar
        ]
    ]


def syxw_1(gameName):
    return [
        [
            '01.' + gameName + '-三碼-前三-直選複式：1,2,3_元_7.8%',
            '118',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)'
            ],
            dollar,
            rb78
        ],
        [
            '02.' + gameName + '-三碼-前三-直選單式：4,5,6_元_7.8%',
            '119',
            '040506',
            dollar,
            rb78
        ],
        [
            '03.' + gameName + '-三碼-前三-組選複式：7,8,9_元_7.8%',
            '120',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)',
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(3)',
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(4)'
            ],
            dollar,
            rb78
        ],
        [
            '04.' + gameName + '-三碼-前三-組選單式：10,11,01_元_7.8%',
            '121',
            '101101',
            dollar,
            rb78
        ],
        [
            '05.' + gameName + '-三碼-前三-組選膽拖：2|3,4_元_7.8%',
            '122',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)'
            ],
            dollar,
            rb78
        ],
        [
            '06.' + gameName + '-三碼-中三-直選複式：5,6,7_角_7.8%',
            '123',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(5)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)',
                '#bet-area-component-renderer > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)'
            ],
            dime,
            rb78
        ],
        [
            '07.' + gameName + '-三碼-中三-直選單式：8,9,10_角_7.8%',
            '124',
            '080910',
            dime,
            rb78
        ],
        [
            '08.' + gameName + '-三碼-中三-組選複式：11,1,2_角_7.8%',
            '125',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)'
            ],
            dime,
            rb78
        ],
        [
            '09.' + gameName + '-三碼-中三-組選單式：3,4,5_角_7.8%',
            '126',
            '030405',
            dime,
            rb78
        ],
        [
            '10.' + gameName + '-三碼-中三-組選膽拖：6|7,8_角_7.8%',
            '127',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(2) > button:nth-child(1)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(3)'
            ],
            dime,
            rb78
        ],
        [
            '11.' + gameName + '-三碼-後三-直選複式：9,10,11_分_7.0%',
            '128',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(4)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(5)',
                '#bet-area-component-renderer > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button'
            ],
            cent,
            rb70
        ],
        [
            '12.' + gameName + '-三碼-後三-直選單式：1,2,3_分_7.0%',
            '129',
            '010203',
            cent,
            rb70
        ],
        [
            '13.' + gameName + '-三碼-後三-組選複式：4,5,6_分_7.0%',
            '130',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(5)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)'
            ],
            cent,
            rb70
        ],
        [
            '14.' + gameName + '-三碼-後三-組選單式：7,8,9_分_7.0%',
            '131',
            '070809',
            cent,
            rb70
        ],
        [
            '15.' + gameName + '-三碼-後三-組選膽拖：10|11,1_分_7.0%',
            '132',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(2) > button:nth-child(5)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)'
            ],
            cent,
            rb70
        ],
        [
            '16.' + gameName + '-二碼-前二-直選複式：2,3_元_6.0%',
            '135',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)'
            ],
            dollar,
            rb60
        ],
        [
            '17.' + gameName + '-二碼-前二-直選單式：4,5_元_6.0%',
            '136',
            '0405',
            dollar,
            rb60
        ],
        [
            '18.' + gameName + '-二碼-前二-組選複式：6,7_元_6.0%',
            '137',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)'
            ],
            dollar,
            rb60
        ],
        [
            '19.' + gameName + '-二碼-前二-組選單式：8,9_元_6.0%',
            '138',
            '0809',
            dollar,
            rb60
        ],
        [
            '20.' + gameName + '-二碼-前二-組選膽拖：10|11_元_6.0%',
            '139',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(2) > button:nth-child(5)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button'
            ],
            dollar,
            rb60
        ],
        [
            '21.' + gameName + '-二碼-後二-直選複式：1.2_角_5.0%',
            '141',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)'
            ],
            dime,
            rb50
        ],
        [
            '22.' + gameName + '-二碼-後二-直選單式：3.4_角_5.0%',
            '142',
            '0304',
            dime,
            rb50
        ],
        [
            '23.' + gameName + '-二碼-後二-組選複式：5.6_角_5.0%',
            '143',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(5)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)'
            ],
            dime,
            rb50
        ],
        [
            '24.' + gameName + '-二碼-後二-組選單式：7.8_角_5.0%',
            '144',
            '0708',
            dime,
            rb50
        ],
        [
            '25.' + gameName + '-二碼-後二-組選膽拖：9|10_角_5.0%',
            '145',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(2) > button:nth-child(4)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(5)'
            ],
            dime,
            rb50
        ],
        [
            '26.' + gameName + '-定位膽：11,,,,_分_4.0%',
            '146',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button'
            ],
            cent,
            rb40
        ],
        [
            '27.' + gameName + '-不定膽-前三位：1_分_4.0%',
            '149',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)'
            ],
            cent,
            rb40
        ],
        [
            '28.' + gameName + '-不定膽-中三位：2_分_4.0%',
            '150',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)'
            ],
            cent,
            rb40
        ],
        [
            '29.' + gameName + '-不定膽-後三位：3_分_4.0%',
            '151',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)'
            ],
            cent,
            rb40
        ]
    ]


def syxw_2(gameName):
    return [
        [
            '30.' + gameName + '-任選單式-任選一中一：4_元_3.0%',
            '161',
            '04',
            dollar,
            rb30
        ],
        [
            '31.' + gameName + '-任選單式-任選二中二：5,6_元_3.0%',
            '162',
            '0506',
            dollar,
            rb30
        ],
        [
            '32.' + gameName + '-任選單式-任選三中三：7,8,9_元_3.0%',
            '163',
            '070809',
            dollar,
            rb30
        ],
        [
            '33.' + gameName + '-任選單式-任選四中四：10,11,1,2_元_3.0%',
            '164',
            '10110102',
            dollar,
            rb30
        ],
        [
            '34.' + gameName + '-任選單式-任選五中五：3,4,5,6,7_元_3.0%',
            '165',
            '0304050607',
            dollar,
            rb30
        ],
        [
            '35.' + gameName + '-任選單式-任選六中五：8,9,10,11,1,2_元_3.0%',
            '166',
            '080910110102',
            dollar,
            rb30
        ],
        [
            '36.' + gameName + '-任選單式-任選七中五：3,4,5,6,7,8,9_元_3.0%',
            '167',
            '03040506070809',
            dollar,
            rb30
        ],
        [
            '37.' + gameName + '-任選單式-任選八中五：10,11,1,2,3,4,5,6_元_3.0%',
            '168',
            '1011010203040506',
            dollar,
            rb30
        ],
        [
            '38.' + gameName + '-任選膽拖-任選二中二：7|8_角_2.0%',
            '170',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(2) > button:nth-child(2)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(3)'
            ],
            dime,
            rb20
        ],
        [
            '39.' + gameName + '-任選膽拖-任選三中三：9|10,11_角_2.0%',
            '171',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(2) > button:nth-child(4)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(5)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button'
            ],
            dime,
            rb20
        ],
        [
            '40.' + gameName + '-任選膽拖-任選四中四：1|2,3,4_角_2.0%',
            '172',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)'
            ],
            dime,
            rb20
        ],
        [
            '41.' + gameName + '-任選膽拖-任選五中五：5|6,7,8,9_角_2.0%',
            '173',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(1) > button:nth-child(5)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(3)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(4)'
            ],
            dime,
            rb20
        ],
        [
            '42.' + gameName + '-任選膽拖-任選六中五：10|11,1,2,3,4_角_2.0%',
            '174',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(2) > button:nth-child(5)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)'
            ],
            dime,
            rb20
        ],
        [
            '43.' + gameName + '-任選膽拖-任選七中五：5|6,7,8,9,10,11_角_2.0%',
            '175',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(1) > button:nth-child(5)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(3)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(4)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(5)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button'
            ],
            dime,
            rb20
        ],
        [
            '44.' + gameName + '-任選膽拖-任選八中五：1|2,3,4,5,6,7,8_角_2.0%',
            '176',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(5)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(3)'
            ],
            dime,
            rb20
        ],
        [
            '45.' + gameName + '-任選複式-任選一中一：9_分_1.0%',
            '152',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(4)'
            ],
            cent,
            rb10
        ],
        [
            '46.' + gameName + '-任選複式-任選二中二：10,11_分_1.0%',
            '153',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(5)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button'
            ],
            cent,
            rb10
        ],
        [
            '47.' + gameName + '-任選複式-任選三中三：1,2,3_分_1.0%',
            '154',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)'
            ],
            cent,
            rb10
        ],
        [
            '48.' + gameName + '-任選複式-任選四中四：4,5,6,7_分_1.0%',
            '155',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(5)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)'
            ],
            cent,
            rb10
        ],
        [
            '49.' + gameName + '-任選複式-任選五中五：8,9,10,11,1_分_1.0%',
            '156',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(5)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)'
            ],
            cent,
            rb10
        ],
        [
            '50.' + gameName + '-任選複式-任選六中五：2,3,4,5,6,7_分_1.0%',
            '157',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(5)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)'
            ],
            cent,
            rb10
        ],
        [
            '51.' + gameName + '-任選複式-任選七中午：8,9,10,11,1,2,3_分_1.0%',
            '158',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(5)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(3)'
            ],
            cent,
            rb10
        ],
        [
            '52.' + gameName + '-任選複式-任選八中五：4,5,6,7,8,9,10,11_分_1.0%',
            '159',
            [
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(5)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(3)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(4)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(5)',
                '#bet-area-component-renderer > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button'
            ],
            cent,
            rb10
        ],
    ]


def kl8(gameName):
    return [
        [
            '01.' + gameName + '-任選-一中一：11_元_7.0%',
            '300',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button:nth-child(1)'
            ],
            dollar,
            rb70
        ],
        [
            '02.' + gameName + '-任選-二中二：12,22_元_6.0%',
            '301',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button:nth-child(2)',
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(5) > button:nth-child(2)'
            ],
            dollar,
            rb60
        ],
        [
            '03.' + gameName + '-任選-三中三：13,23,33_元_5.0%',
            '302',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button:nth-child(3)',
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(5) > button:nth-child(3)',
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(7) > button:nth-child(3)'
            ],
            dollar,
            rb50
        ],
        [
            '04.' + gameName + '-任選-四中四：14,24,34,44_角_4.0%',
            '303',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button:nth-child(4)',
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(5) > button:nth-child(4)',
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(7) > button:nth-child(4)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(4)'
            ],
            dime,
            rb40
        ],
        [
            '05.' + gameName + '-任選-五中五：15,25,35,45,55_角_3.0%',
            '304',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button:nth-child(5)',
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(5) > button:nth-child(5)',
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(7) > button:nth-child(5)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(5)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > button:nth-child(5)'
            ],
            dime,
            rb30
        ],
        [
            '06.' + gameName + '-任選-六中五：16,26,36,46,56,66_角_2.0%',
            '305',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(4) > button:nth-child(1)',
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(6) > button:nth-child(1)',
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(8) > button:nth-child(1)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(4) > button:nth-child(1)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(6) > button:nth-child(1)'
            ],
            dime,
            rb20
        ],
        [
            '07.' + gameName + '-任選-七中五：17,27,37,47,57,67,77_分_1.0%',
            '306',
            [
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(4) > button:nth-child(2)',
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(6) > button:nth-child(2)',
                '#bet-area-component-renderer > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(8) > button:nth-child(2)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(4) > button:nth-child(2)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(6) > button:nth-child(2)',
                '#bet-area-component-renderer > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(8) > button:nth-child(2)'
            ],
            cent,
            rb10
        ]

    ]


def getLottery(lottery, game):
    if game == 'ssc_1':
        return ssc_1(lottery)
    elif game == 'ssc_2':
        return ssc_2(lottery)
    elif game == 'ssc_3':
        return ssc_3(lottery)
    elif game == 'ffc_0':
        return ffc_0(lottery)
    elif game == 'ffc_1':
        return ffc_1(lottery)
    elif game == 'ffc_2':
        return ffc_2(lottery)
    elif game == 'ffc_3':
        return ffc_3(lottery)
    elif game == 'ffc_4':
        return ffc_4(lottery)
    elif game == 'ffc_5':
        return ffc_5(lottery)
    elif game == 'ffc_6':
        return ffc_6(lottery)
    elif game == 'ffc_7':
        return ffc_7(lottery)
    elif game == 'pk10':
        return pk10(lottery)
    elif game == 'k3':
        return k3(lottery)
    elif game == '3d':
        return td(lottery)
    elif game == 'klsf':
        return klsf(lottery)
    elif game == 'six_1':
        return six_1(lottery)
    elif game == 'six_2':
        return six_2(lottery)
    elif game == 'six_3':
        return six_3(lottery)
    elif game == 'syxw_1':
        return syxw_1(lottery)
    elif game == 'syxw_2':
        return syxw_2(lottery)
    elif game == 'kl8':
        return kl8(lottery)
