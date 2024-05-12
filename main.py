import requests, time
import send_message
import crawling_excel
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    product = request.form['product']
    alarm = request.form['alarm']
    id = request.form['id']
    if __name__ == "__main__":
        data = crawling_excel.danawa_crawling(product)
        product_list = data[:5]
        for i in range(len(product_list)): product_list[i].append(id)
        print(product_list)
        crawling_excel.save_to_excel(product_list, f"product_info.xlsx")
        message  = f"{product}의 최저가 상품 리스트입니다.\n\n"
        for i in range(5):
            for text in product_list[i]:
                if text!=product_list[i][-1]:
                    message = message+text+"\n"
            message = message+"="*50+"\n\n"
        print(message)
        
    if alarm=="ntfy":
        send_message.ntfy0(f"danawa_{id}", message)
        time.sleep(10)
        return redirect(f"https://ntfy.sh/danawa_{id}")
    elif alarm=="slack":
        return redirect("https://app.slack.com/client/T072KG05545/C072QT9TFJQ")
    # 여기서는 입력된 제품과 알람 설정을 사용하여 필요한 작업을 수행합니다.
    # 예를 들어 데이터베이스에 저장하거나 다른 서비스로 전송하는 등의 작업을 수행할 수 있습니다.
    else:
        return f'제품: {product}, 알람 선택: {alarm}'

if __name__ == '__main__':
    app.run(debug=True)