# Really long, just a sanity check for more testing.
ORIGINAL_GAMES_STRING = \
    """[
    {
        "neutral": false,
        "visTeamName": "Cardinals",
        "visStats": {
            "statIdCode": "10001002620200913",
            "gameCode": "0001002620200913",
            "teamCode": 1,
            "gameDate": "Sep 13, 2020",
            "rushYds": 180,
            "rushAtt": 36,
            "passYds": 224,
            "passAtt": 40,
            "passComp": 26,
            "penalties": 9,
            "penaltYds": 102,
            "fumblesLost": 0,
            "interceptionsThrown": 1,
            "firstDowns": 29,
            "thridDownAtt": 14,
            "thirdDownConver": 7,
            "fourthDownAtt": 0,
            "fourthDownConver": 0,
            "timePoss": 1886,
            "score": 24
        },
        "homeTeamName": "49ers",
        "homeStats": {
            "statIdCode": "260001002620200913",
            "gameCode": "0001002620200913",
            "teamCode": 26,
            "gameDate": "Sep 13, 2020",
            "rushYds": 123,
            "rushAtt": 25,
            "passYds": 243,
            "passAtt": 33,
            "passComp": 19,
            "penalties": 5,
            "penaltYds": 53,
            "fumblesLost": 0,
            "interceptionsThrown": 0,
            "firstDowns": 18,
            "thridDownAtt": 11,
            "thirdDownConver": 2,
            "fourthDownAtt": 2,
            "fourthDownConver": 0,
            "timePoss": 1714,
            "score": 20
        },
        "isFinal": false,
        "date": "2020-09-13"
    },
    {
        "neutral": false,
        "visTeamName": "49ers",
        "visStats": {
            "statIdCode": "260026002020200920",
            "gameCode": "0026002020200920",
            "teamCode": 26,
            "gameDate": "Sep 20, 2020",
            "rushYds": 182,
            "rushAtt": 29,
            "passYds": 177,
            "passAtt": 27,
            "passComp": 22,
            "penalties": 5,
            "penaltYds": 59,
            "fumblesLost": 0,
            "interceptionsThrown": 1,
            "firstDowns": 17,
            "thridDownAtt": 13,
            "thirdDownConver": 7,
            "fourthDownAtt": 0,
            "fourthDownConver": 0,
            "timePoss": 1933,
            "score": 31
        },
        "homeTeamName": "Jets",
        "homeStats": {
            "statIdCode": "200026002020200920",
            "gameCode": "0026002020200920",
            "teamCode": 20,
            "gameDate": "Sep 20, 2020",
            "rushYds": 104,
            "rushAtt": 29,
            "passYds": 173,
            "passAtt": 32,
            "passComp": 21,
            "penalties": 5,
            "penaltYds": 65,
            "fumblesLost": 0,
            "interceptionsThrown": 0,
            "firstDowns": 17,
            "thridDownAtt": 14,
            "thirdDownConver": 5,
            "fourthDownAtt": 2,
            "fourthDownConver": 0,
            "timePoss": 1667,
            "score": 13
        },
        "isFinal": false,
        "date": "2020-09-20"
    },
    {
        "neutral": false,
        "visTeamName": "49ers",
        "visStats": {
            "statIdCode": "260026001220200927",
            "gameCode": "0026001220200927",
            "teamCode": 26,
            "gameDate": "Sep 27, 2020",
            "rushYds": 93,
            "rushAtt": 35,
            "passYds": 327,
            "passAtt": 36,
            "passComp": 25,
            "penalties": 6,
            "penaltYds": 45,
            "fumblesLost": 0,
            "interceptionsThrown": 0,
            "firstDowns": 29,
            "thridDownAtt": 12,
            "thirdDownConver": 8,
            "fourthDownAtt": 0,
            "fourthDownConver": 0,
            "timePoss": 2384,
            "score": 36
        },
        "homeTeamName": "Giants",
        "homeStats": {
            "statIdCode": "120026001220200927",
            "gameCode": "0026001220200927",
            "teamCode": 12,
            "gameDate": "Sep 27, 2020",
            "rushYds": 66,
            "rushAtt": 15,
            "passYds": 165,
            "passAtt": 32,
            "passComp": 17,
            "penalties": 5,
            "penaltYds": 28,
            "fumblesLost": 2,
            "interceptionsThrown": 1,
            "firstDowns": 13,
            "thridDownAtt": 10,
            "thirdDownConver": 4,
            "fourthDownAtt": 2,
            "fourthDownConver": 1,
            "timePoss": 1216,
            "score": 9
        },
        "isFinal": false,
        "date": "2020-09-27"
    },
    {
        "neutral": false,
        "visTeamName": "Eagles",
        "visStats": {
            "statIdCode": "220022002620201004",
            "gameCode": "0022002620201004",
            "teamCode": 22,
            "gameDate": "Oct 5, 2020",
            "rushYds": 93,
            "rushAtt": 28,
            "passYds": 174,
            "passAtt": 28,
            "passComp": 18,
            "penalties": 3,
            "penaltYds": 25,
            "fumblesLost": 0,
            "interceptionsThrown": 1,
            "firstDowns": 18,
            "thridDownAtt": 13,
            "thirdDownConver": 4,
            "fourthDownAtt": 2,
            "fourthDownConver": 2,
            "timePoss": 1769,
            "score": 25
        },
        "homeTeamName": "49ers",
        "homeStats": {
            "statIdCode": "260022002620201004",
            "gameCode": "0022002620201004",
            "teamCode": 26,
            "gameDate": "Oct 5, 2020",
            "rushYds": 116,
            "rushAtt": 20,
            "passYds": 301,
            "passAtt": 45,
            "passComp": 32,
            "penalties": 6,
            "penaltYds": 42,
            "fumblesLost": 1,
            "interceptionsThrown": 2,
            "firstDowns": 25,
            "thridDownAtt": 11,
            "thirdDownConver": 5,
            "fourthDownAtt": 1,
            "fourthDownConver": 0,
            "timePoss": 1831,
            "score": 20
        },
        "isFinal": false,
        "date": "2020-10-05"
    },
    {
        "neutral": false,
        "visTeamName": "Dolphins",
        "visStats": {
            "statIdCode": "160016002620201011",
            "gameCode": "0016002620201011",
            "teamCode": 16,
            "gameDate": "Oct 11, 2020",
            "rushYds": 94,
            "rushAtt": 33,
            "passYds": 342,
            "passAtt": 28,
            "passComp": 22,
            "penalties": 7,
            "penaltYds": 69,
            "fumblesLost": 0,
            "interceptionsThrown": 0,
            "firstDowns": 22,
            "thridDownAtt": 12,
            "thirdDownConver": 4,
            "fourthDownAtt": 2,
            "fourthDownConver": 2,
            "timePoss": 2213,
            "score": 43
        },
        "homeTeamName": "49ers",
        "homeStats": {
            "statIdCode": "260016002620201011",
            "gameCode": "0016002620201011",
            "teamCode": 26,
            "gameDate": "Oct 11, 2020",
            "rushYds": 131,
            "rushAtt": 19,
            "passYds": 128,
            "passAtt": 35,
            "passComp": 16,
            "penalties": 7,
            "penaltYds": 75,
            "fumblesLost": 1,
            "interceptionsThrown": 2,
            "firstDowns": 19,
            "thridDownAtt": 10,
            "thirdDownConver": 2,
            "fourthDownAtt": 2,
            "fourthDownConver": 0,
            "timePoss": 1387,
            "score": 17
        },
        "isFinal": false,
        "date": "2020-10-11"
    },
    {
        "neutral": false,
        "visTeamName": "Rams",
        "visStats": {
            "statIdCode": "270027002620201018",
            "gameCode": "0027002620201018",
            "teamCode": 27,
            "gameDate": "Oct 19, 2020",
            "rushYds": 113,
            "rushAtt": 19,
            "passYds": 198,
            "passAtt": 38,
            "passComp": 19,
            "penalties": 6,
            "penaltYds": 34,
            "fumblesLost": 0,
            "interceptionsThrown": 1,
            "firstDowns": 17,
            "thridDownAtt": 12,
            "thirdDownConver": 4,
            "fourthDownAtt": 1,
            "fourthDownConver": 0,
            "timePoss": 1325,
            "score": 16
        },
        "homeTeamName": "49ers",
        "homeStats": {
            "statIdCode": "260027002620201018",
            "gameCode": "0027002620201018",
            "teamCode": 26,
            "gameDate": "Oct 19, 2020",
            "rushYds": 122,
            "rushAtt": 37,
            "passYds": 268,
            "passAtt": 33,
            "passComp": 23,
            "penalties": 7,
            "penaltYds": 63,
            "fumblesLost": 0,
            "interceptionsThrown": 0,
            "firstDowns": 24,
            "thridDownAtt": 13,
            "thirdDownConver": 5,
            "fourthDownAtt": 1,
            "fourthDownConver": 1,
            "timePoss": 2275,
            "score": 24
        },
        "isFinal": false,
        "date": "2020-10-19"
    },
    {
        "neutral": false,
        "visTeamName": "49ers",
        "visStats": {
            "statIdCode": "260026001820201025",
            "gameCode": "0026001820201025",
            "teamCode": 26,
            "gameDate": "Oct 25, 2020",
            "rushYds": 197,
            "rushAtt": 37,
            "passYds": 270,
            "passAtt": 25,
            "passComp": 20,
            "penalties": 6,
            "penaltYds": 65,
            "fumblesLost": 0,
            "interceptionsThrown": 2,
            "firstDowns": 26,
            "thridDownAtt": 9,
            "thirdDownConver": 5,
            "fourthDownAtt": 0,
            "fourthDownConver": 0,
            "timePoss": 2303,
            "score": 33
        },
        "homeTeamName": "Patriots",
        "homeStats": {
            "statIdCode": "180026001820201025",
            "gameCode": "0026001820201025",
            "teamCode": 18,
            "gameDate": "Oct 25, 2020",
            "rushYds": 94,
            "rushAtt": 22,
            "passYds": 147,
            "passAtt": 25,
            "passComp": 15,
            "penalties": 3,
            "penaltYds": 30,
            "fumblesLost": 0,
            "interceptionsThrown": 4,
            "firstDowns": 17,
            "thridDownAtt": 6,
            "thirdDownConver": 1,
            "fourthDownAtt": 0,
            "fourthDownConver": 0,
            "timePoss": 1297,
            "score": 6
        },
        "isFinal": false,
        "date": "2020-10-25"
    },
    {
        "neutral": false,
        "visTeamName": "49ers",
        "visStats": {
            "statIdCode": "260026002520201101",
            "gameCode": "0026002520201101",
            "teamCode": 26,
            "gameDate": "Nov 1, 2020",
            "rushYds": 52,
            "rushAtt": 22,
            "passYds": 299,
            "passAtt": 41,
            "passComp": 29,
            "penalties": 6,
            "penaltYds": 36,
            "fumblesLost": 1,
            "interceptionsThrown": 1,
            "firstDowns": 24,
            "thridDownAtt": 13,
            "thirdDownConver": 6,
            "fourthDownAtt": 2,
            "fourthDownConver": 2,
            "timePoss": 1742,
            "score": 27
        },
        "homeTeamName": "Seahawks",
        "homeStats": {
            "statIdCode": "250026002520201101",
            "gameCode": "0026002520201101",
            "teamCode": 25,
            "gameDate": "Nov 1, 2020",
            "rushYds": 101,
            "rushAtt": 28,
            "passYds": 249,
            "passAtt": 37,
            "passComp": 27,
            "penalties": 6,
            "penaltYds": 30,
            "fumblesLost": 0,
            "interceptionsThrown": 0,
            "firstDowns": 27,
            "thridDownAtt": 15,
            "thirdDownConver": 9,
            "fourthDownAtt": 0,
            "fourthDownConver": 0,
            "timePoss": 1858,
            "score": 37
        },
        "isFinal": false,
        "date": "2020-11-01"
    },
    {
        "neutral": false,
        "visTeamName": "Packers",
        "visStats": {
            "statIdCode": "110011002620201105",
            "gameCode": "0011002620201105",
            "teamCode": 11,
            "gameDate": "Nov 6, 2020",
            "rushYds": 111,
            "rushAtt": 31,
            "passYds": 294,
            "passAtt": 31,
            "passComp": 25,
            "penalties": 5,
            "penaltYds": 45,
            "fumblesLost": 0,
            "interceptionsThrown": 0,
            "firstDowns": 21,
            "thridDownAtt": 12,
            "thirdDownConver": 6,
            "fourthDownAtt": 1,
            "fourthDownConver": 1,
            "timePoss": 2190,
            "score": 34
        },
        "homeTeamName": "49ers",
        "homeStats": {
            "statIdCode": "260011002620201105",
            "gameCode": "0011002620201105",
            "teamCode": 26,
            "gameDate": "Nov 6, 2020",
            "rushYds": 55,
            "rushAtt": 17,
            "passYds": 282,
            "passAtt": 35,
            "passComp": 22,
            "penalties": 4,
            "penaltYds": 33,
            "fumblesLost": 1,
            "interceptionsThrown": 1,
            "firstDowns": 17,
            "thridDownAtt": 10,
            "thirdDownConver": 3,
            "fourthDownAtt": 1,
            "fourthDownConver": 0,
            "timePoss": 1410,
            "score": 17
        },
        "isFinal": false,
        "date": "2020-11-06"
    },
    {
        "neutral": false,
        "visTeamName": "49ers",
        "visStats": {
            "statIdCode": "260026001920201115",
            "gameCode": "0026001920201115",
            "teamCode": 26,
            "gameDate": "Nov 15, 2020",
            "rushYds": 49,
            "rushAtt": 25,
            "passYds": 232,
            "passAtt": 39,
            "passComp": 24,
            "penalties": 6,
            "penaltYds": 51,
            "fumblesLost": 2,
            "interceptionsThrown": 2,
            "firstDowns": 21,
            "thridDownAtt": 16,
            "thirdDownConver": 7,
            "fourthDownAtt": 1,
            "fourthDownConver": 0,
            "timePoss": 1974,
            "score": 13
        },
        "homeTeamName": "Saints",
        "homeStats": {
            "statIdCode": "190026001920201115",
            "gameCode": "0026001920201115",
            "teamCode": 19,
            "gameDate": "Nov 15, 2020",
            "rushYds": 114,
            "rushAtt": 30,
            "passYds": 123,
            "passAtt": 23,
            "passComp": 14,
            "penalties": 5,
            "penaltYds": 61,
            "fumblesLost": 2,
            "interceptionsThrown": 0,
            "firstDowns": 17,
            "thridDownAtt": 12,
            "thirdDownConver": 2,
            "fourthDownAtt": 0,
            "fourthDownConver": 0,
            "timePoss": 1626,
            "score": 27
        },
        "isFinal": false,
        "date": "2020-11-15"
    },
    {
        "neutral": false,
        "visTeamName": "49ers",
        "visStats": {
            "statIdCode": "260026002720201129",
            "gameCode": "0026002720201129",
            "teamCode": 26,
            "gameDate": "Nov 29, 2020",
            "rushYds": 115,
            "rushAtt": 33,
            "passYds": 233,
            "passAtt": 35,
            "passComp": 24,
            "penalties": 5,
            "penaltYds": 40,
            "fumblesLost": 2,
            "interceptionsThrown": 1,
            "firstDowns": 18,
            "thridDownAtt": 14,
            "thirdDownConver": 3,
            "fourthDownAtt": 1,
            "fourthDownConver": 1,
            "timePoss": 2043,
            "score": 23
        },
        "homeTeamName": "Rams",
        "homeStats": {
            "statIdCode": "270026002720201129",
            "gameCode": "0026002720201129",
            "teamCode": 27,
            "gameDate": "Nov 29, 2020",
            "rushYds": 126,
            "rushAtt": 28,
            "passYds": 182,
            "passAtt": 31,
            "passComp": 19,
            "penalties": 3,
            "penaltYds": 27,
            "fumblesLost": 2,
            "interceptionsThrown": 2,
            "firstDowns": 14,
            "thridDownAtt": 13,
            "thirdDownConver": 4,
            "fourthDownAtt": 0,
            "fourthDownConver": 0,
            "timePoss": 1557,
            "score": 20
        },
        "isFinal": false,
        "date": "2020-11-29"
    },
    {
        "neutral": false,
        "visTeamName": "Bills",
        "visStats": {
            "statIdCode": "40004002620201207",
            "gameCode": "0004002620201207",
            "teamCode": 4,
            "gameDate": "Dec 8, 2020",
            "rushYds": 81,
            "rushAtt": 27,
            "passYds": 368,
            "passAtt": 40,
            "passComp": 32,
            "penalties": 4,
            "penaltYds": 50,
            "fumblesLost": 1,
            "interceptionsThrown": 0,
            "firstDowns": 31,
            "thridDownAtt": 9,
            "thirdDownConver": 4,
            "fourthDownAtt": 3,
            "fourthDownConver": 2,
            "timePoss": 2098,
            "score": 34
        },
        "homeTeamName": "49ers",
        "homeStats": {
            "statIdCode": "260004002620201207",
            "gameCode": "0004002620201207",
            "teamCode": 26,
            "gameDate": "Dec 8, 2020",
            "rushYds": 86,
            "rushAtt": 21,
            "passYds": 316,
            "passAtt": 39,
            "passComp": 26,
            "penalties": 7,
            "penaltYds": 43,
            "fumblesLost": 0,
            "interceptionsThrown": 2,
            "firstDowns": 24,
            "thridDownAtt": 11,
            "thirdDownConver": 6,
            "fourthDownAtt": 1,
            "fourthDownConver": 0,
            "timePoss": 1502,
            "score": 24
        },
        "isFinal": false,
        "date": "2020-12-08"
    },
    {
        "neutral": false,
        "visTeamName": "Washington",
        "visStats": {
            "statIdCode": "300030002620201213",
            "gameCode": "0030002620201213",
            "teamCode": 30,
            "gameDate": "Dec 13, 2020",
            "rushYds": 98,
            "rushAtt": 28,
            "passYds": 95,
            "passAtt": 32,
            "passComp": 15,
            "penalties": 5,
            "penaltYds": 30,
            "fumblesLost": 0,
            "interceptionsThrown": 1,
            "firstDowns": 12,
            "thridDownAtt": 15,
            "thirdDownConver": 3,
            "fourthDownAtt": 0,
            "fourthDownConver": 0,
            "timePoss": 1669,
            "score": 23
        },
        "homeTeamName": "49ers",
        "homeStats": {
            "statIdCode": "260030002620201213",
            "gameCode": "0030002620201213",
            "teamCode": 26,
            "gameDate": "Dec 13, 2020",
            "rushYds": 108,
            "rushAtt": 27,
            "passYds": 236,
            "passAtt": 45,
            "passComp": 25,
            "penalties": 5,
            "penaltYds": 35,
            "fumblesLost": 2,
            "interceptionsThrown": 1,
            "firstDowns": 21,
            "thridDownAtt": 15,
            "thirdDownConver": 4,
            "fourthDownAtt": 1,
            "fourthDownConver": 0,
            "timePoss": 1931,
            "score": 15
        },
        "isFinal": false,
        "date": "2020-12-13"
    },
    {
        "neutral": false,
        "visTeamName": "49ers",
        "visStats": {
            "statIdCode": "260026000820201220",
            "gameCode": "0026000820201220",
            "teamCode": 26,
            "gameDate": "Dec 20, 2020",
            "rushYds": 150,
            "rushAtt": 36,
            "passYds": 308,
            "passAtt": 43,
            "passComp": 26,
            "penalties": 4,
            "penaltYds": 39,
            "fumblesLost": 2,
            "interceptionsThrown": 2,
            "firstDowns": 28,
            "thridDownAtt": 15,
            "thirdDownConver": 6,
            "fourthDownAtt": 1,
            "fourthDownConver": 1,
            "timePoss": 2096,
            "score": 33
        },
        "homeTeamName": "Cowboys",
        "homeStats": {
            "statIdCode": "80026000820201220",
            "gameCode": "0026000820201220",
            "teamCode": 8,
            "gameDate": "Dec 20, 2020",
            "rushYds": 87,
            "rushAtt": 22,
            "passYds": 204,
            "passAtt": 34,
            "passComp": 20,
            "penalties": 5,
            "penaltYds": 58,
            "fumblesLost": 0,
            "interceptionsThrown": 0,
            "firstDowns": 15,
            "thridDownAtt": 15,
            "thirdDownConver": 6,
            "fourthDownAtt": 0,
            "fourthDownConver": 0,
            "timePoss": 1504,
            "score": 41
        },
        "isFinal": false,
        "date": "2020-12-20"
    },
    {
        "neutral": false,
        "visTeamName": "49ers",
        "visStats": {
            "statIdCode": "260026000120201226",
            "gameCode": "0026000120201226",
            "teamCode": 26,
            "gameDate": "Dec 26, 2020",
            "rushYds": 227,
            "rushAtt": 30,
            "passYds": 171,
            "passAtt": 22,
            "passComp": 13,
            "penalties": 4,
            "penaltYds": 27,
            "fumblesLost": 1,
            "interceptionsThrown": 0,
            "firstDowns": 22,
            "thridDownAtt": 9,
            "thirdDownConver": 2,
            "fourthDownAtt": 0,
            "fourthDownConver": 0,
            "timePoss": 1664,
            "score": 20
        },
        "homeTeamName": "Cardinals",
        "homeStats": {
            "statIdCode": "10026000120201226",
            "gameCode": "0026000120201226",
            "teamCode": 1,
            "gameDate": "Dec 26, 2020",
            "rushYds": 120,
            "rushAtt": 27,
            "passYds": 230,
            "passAtt": 50,
            "passComp": 31,
            "penalties": 4,
            "penaltYds": 20,
            "fumblesLost": 1,
            "interceptionsThrown": 1,
            "firstDowns": 20,
            "thridDownAtt": 16,
            "thirdDownConver": 4,
            "fourthDownAtt": 6,
            "fourthDownConver": 4,
            "timePoss": 1936,
            "score": 12
        },
        "isFinal": false,
        "date": "2020-12-26"
    },
    {
        "neutral": false,
        "visTeamName": "Seahawks",
        "visStats": {
            "statIdCode": "250025002620210103",
            "gameCode": "0025002620210103",
            "teamCode": 25,
            "gameDate": "Jan 3, 2021",
            "rushYds": 121,
            "rushAtt": 27,
            "passYds": 159,
            "passAtt": 36,
            "passComp": 20,
            "penalties": 4,
            "penaltYds": 35,
            "fumblesLost": 0,
            "interceptionsThrown": 0,
            "firstDowns": 21,
            "thridDownAtt": 12,
            "thirdDownConver": 4,
            "fourthDownAtt": 1,
            "fourthDownConver": 1,
            "timePoss": 1660,
            "score": 26
        },
        "homeTeamName": "49ers",
        "homeStats": {
            "statIdCode": "260025002620210103",
            "gameCode": "0025002620210103",
            "teamCode": 26,
            "gameDate": "Jan 3, 2021",
            "rushYds": 86,
            "rushAtt": 24,
            "passYds": 242,
            "passAtt": 37,
            "passComp": 25,
            "penalties": 2,
            "penaltYds": 25,
            "fumblesLost": 1,
            "interceptionsThrown": 0,
            "firstDowns": 17,
            "thridDownAtt": 15,
            "thirdDownConver": 6,
            "fourthDownAtt": 1,
            "fourthDownConver": 1,
            "timePoss": 1940,
            "score": 23
        },
        "isFinal": false,
        "date": "2021-01-03"
    }
]"""
