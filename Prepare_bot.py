import requests
import datetime

url = https://api.telegram.org/bot780801796:AAHOJaIURXOIvDmcajEOHGA2zEsp_uwOZJk/

def lastUpdate(dataEnd):
res = dataEnd['result']
totalUpdates = len(res) - 1
return res[totalUpdates]

def getChatID(update):
chatID = update['message']['chat']['id']
return chatID

def sendResp(chat, value):
settings = {'chat_id': chat, 'text': value}
resp = requests.post(url + 'sendMessage', data=settings)
return resp

def getUpdatesJson(request):
settings = {'timeout': 100, 'offset': None}
response = requests.get(request + 'getUpdates', data=settings)
return response.json()

def main():
chatID = getChatID(lastUpdate(getUpdatesJson(url)))
sendResp(chatID, 'Your massege')
updateID = lastUpdate(getUpdatesJson(url))['update_id']

while True:

if updateID == lastUpdate(getUpdatesJson(url))['update_id']:
sendResp(getChatID(lastUpdate(getUpdatesJson(url))), 'проба')
updateID += 1
sleep(1)

if __name__ == '__main__':
main()
