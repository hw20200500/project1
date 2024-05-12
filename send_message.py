import requests
import telegram
import asyncio

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

api_token="6830788564:AAG92fwOemNTQpX0GvSfEm5PkpKAsGYeJBc"
bot0 = telegram.Bot(token=api_token)

async def telegram_bot(my_id,msg0):
    for product,price in msg0.items():
        await bot0.sendMessage(chat_id=my_id,text=f"{product}: {price}")

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