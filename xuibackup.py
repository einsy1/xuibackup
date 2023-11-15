import requests

token = "6823818667:AAEgHOxtIHt1FmuC5o1luJSTxkJ7d2oL2eY"
chat_id = "6403589067"
file_path = "/path/to/your/file"  # 替换为您的文件路径

def send_document(chat_id, document):
    url = f"https://api.telegram.org/bot{token}/sendDocument"
    files = {'document': open(document, 'rb')}
    data = {'chat_id': chat_id}
    r = requests.post(url, files=files, data=data)
    return r

send_document(chat_id, file_path)
