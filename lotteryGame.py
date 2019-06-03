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
            '87',
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
            '652',
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
