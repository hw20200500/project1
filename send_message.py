import requests
import telegram
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

SLACK_API_TOKEN = ""
SLACK_CHANNEL = "#python-slack-test"
def sendSlackWebHook(message):
    try:
        # WebClient 인스턴스를 생성하고, 생성자에 Slack API 토큰을 전달합니다.
        client = WebClient(token=SLACK_API_TOKEN)
        # chat_postMessage 메소드를 사용하여 메시지를 Slack 채널에 전송합니다.
        response = client.chat_postMessage(
            channel=SLACK_CHANNEL,
            text=message
        )
        # 응답을 출력하여 메시지 전송 성공 여부를 확인합니다.
        print(f"Slack message sent: {response['message']['text']}")
        return f"Slack message sent: {response['message']['text']}"
    except SlackApiError as e:
        # 메시지 전송 중 발생한 에러를 캐치하고, 에러 메시지를 출력합니다.
        print(f"Error sending message to Slack: {e.response['error']}")
        return f"Error sending message to Slack: {e.response['error']}"


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
api_token="6997403129:AAGkFmx9pOZrAACqLlvTLjBen7nSyCASRLE"
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