import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = ""

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = ""

stock_param = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=stock_param)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_closing = data_list[0]['4. close']
day_before_yesterday_closing = data_list[1]['4. close']

change_in_price = (float(day_before_yesterday_closing) - float(yesterday_closing))
up_down = None
if change_in_price > 0:
    up_down = "🔺"
else:
    up_down = "🔻"


diff_percentage = round((change_in_price / float(yesterday_closing))* 100)
if abs(diff_percentage) >= 2:
    news_param = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_param)
    news_response.raise_for_status()
    articles = news_response.json()["articles"][:3]
    formatted_article = [f"{STOCK}: {up_down}{diff_percentage}% \nHeadline: {article['title']}. \nBrief: {article['description']}" for article in articles]


## STEP 3: Use https://www.twilio.com
    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)

    for article in formatted_article:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=f'{article}',
            to='whatsapp:+918884000438'
        )

# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

