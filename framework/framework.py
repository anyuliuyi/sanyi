#coding=utf-8
import time
import datetime
import random


class gl:
    @staticmethod
    def repaceSpecialCharactersinString(content):
        return content.replace("^", "").replace("a", "").replace("link", "").replace("text", "").replace("href",
                                                                                                       "").replace(
            "url", "").replace("link", "").replace("~", "").replace("；", "").replace("、", "").replace("=", "").replace(
            "<", "").replace(">", "").replace("{", "").replace("}", "").replace("/", "").replace("+", "").replace("*",
                                                                                                                  "").replace(
            "(", "").replace(")", "").replace("[", "").replace("]", "").replace(" ", "").replace(".", "").replace("-",
                                                                                                                  "").replace(
            "t", "").replace("\t", "").replace("\"", "").replace("“", "").replace("”", "").replace("？", "").replace("?",
                                                                                                                    "").replace(
            "：", "").replace("!", "").replace("。", "").replace("！", "").replace("|", "").replace("n", "").replace("\n", "").replace(
            "，", "").replace(",", "").replace(":", "").replace("～", "").replace("\r", "").replace("r", "").replace("\\", "").replace(' ','')

    @staticmethod
    def getTimewithSeconds():
        return datetime.datetime.now().strftime('%Y%m%d%H%M%S')

    @staticmethod
    def getTimestamp():
        return int(time.time() * 1000)

    @staticmethod
    def getUniqueDateTime():
        return datetime.datetime.now().strftime('%Y%m%d%H%M%S') + str(random.randint(10000, 20000))







    # print(gl.getUniqueDateTime())
    # print('哈喽','\\n','你好呀')
test1={
    "status": 200,
    "message": "success",
    "tspan": 96,
    "data": [
        {
            "type": "text",
            "subType": "text",
            "value": "您好，",
            "data": []
        },
        {
            "type": "text",
            "subType": "relatelist",
            "value": "您是否想问以下问题：",
            "data": [
                "北京时间异常如何处理",
                "工作时间异常如何处理"
            ]
        }
    ],
    "info": {
        "module": "faq",
        "source": "ml",
        "textScore": 100,
        "emotion": "中性",
        "emotionScore": 80,
        "tokens": [
            "时间/n",
            "异常/a",
            "如何/ry",
            "处理/v"
        ],
        "matchQuestion": "时间异常如何处理"
    },
    "extendData": {}
}

if __name__ == '__main__' :
    test2 = test1['data'][1]['data']
    gl = gl()
    print(test2)
    if "北京时间异常如何处理" in test2:
        print("pass")
    else:
        print("error")
