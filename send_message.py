import requests
import telegram
import asyncio

# 웹훅 주소를 변수에 넣어 사용
slack_url = "https://hooks.slack.com/services/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"
def sendSlackWebHook(strText):
    headers = {
        "Content-type": "application/json"
    }
    data = {
        "text": strText
    }
    res = requests.post(slack_url, headers=headers, json=data)
# curl -X POST -H 'Content-type: application/json' --data '{"text":"Hello, World!"}' https://hooks.slack.com/services/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
    if res.status_code == 200:
        return "OK"
    else:
        print(res)
        return "Error"
# 크롤링하여 얻은 정보 중 product_name과 product_price 정보를 가져온다
# 아래는 임의로 설정한 값

#ntfy 보내기 및 실행
def ntfy0(topic,msg):
    requests.post(f"https://ntfy.sh/{topic}", 
        data=f"{msg}".encode(encoding='utf-8'))

# ntfy0("danawa_chatbot", "hello!")
"""
사용법
ntfy0(f"{구독ID}",f"{제품}: {가격}")
"""

"""
msg = {"하나":"1","둘":"2","셋":"3","넷":"4"}
for product,price in msg.items():
    ntfy0("dokkaebi",f"{product}: {price}")
"""

# 텔레그램 보내기 및 실행
api_token=""
bot0 = telegram.Bot(token=api_token)

async def telegram_bot(my_id,msg0):
    await bot0.sendMessage(chat_id=my_id,text=msg0)

"""
사용법
사용자의 텔레그램 chat_id와 제품과 가격으로 이뤄진 딕셔너리 삽입
asyncio.run(telegram_bot(f{사용자텔레그램chat_id},{"제품": "가격"}))
"""

#GET My ID 같은 텔레그램 봇을 사용하여 자신의 chat_id를 알아낼 수 있음
"""
msg = {"하나":"1","둘":"2","셋":"3","넷":"4"}
asyncio.run(telegram_bot(2121863062,msg)) 
"""