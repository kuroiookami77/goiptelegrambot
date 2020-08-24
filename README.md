# GOIP Telegram Bot
Telegram Bot with auth by whitelist (sqlite3) was used to send sms of a certain type (goip simbase api) and generate csv-reports. Bot can also show last transactions (from db sqlite3).
___
Telegram Bot с авторизацией по whitelist (используя sqlite3), использовался для отправки смс определенного типа (через апи goip simbase, для автоматизации отправки денежных средств с симкарт теле2). Бот умеет показывать последние транзакции (имеется в виду, что каждое отправленное сообщение - есть транзакция), создавать отчеты в формате CSV.

На данный момент не используется. 
Для запуска следовать инструкции ниже.
![alt text](https://iili.io/dSxQDu.jpg)
___

If you want to start this bot with all functions you should:
0) pip install -r req.txt
1) in bot.py set TOKEN (@botfather)
2) in content.py set ip address goip SMS-server database (dbhost, dbpass) for db 'goip'
3) in content.py set ip address goip SIM-base ('our_gsm_gateway_ip')
4) add in main.db (sqlite3) in table whitelist:

id phonenumber firstname lastname <br/>
for example <br/>
3 +71234567890 User Name 
