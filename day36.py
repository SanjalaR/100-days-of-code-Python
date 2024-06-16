STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
import requests
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

parameters1 = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': 'KXWTWLTOSHQPTT3U',
}
response1 = requests.get(url='https://www.alphavantage.co/query', params=parameters1)
response1.raise_for_status()
data1 = response1.json()
data1 = data1['Time Series (Daily)']
data1_list = [value for (key,value) in data1.items()]
print(data1_list)
yest = float(data1_list[0]['4. close'])
dby = float(data1_list[1]['4. close'])
print(yest, dby)
diff = (abs(yest - dby)/yest)*100
print(diff)
get_news = False

if diff > 3:
    print('Get News')
    get_news = True

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

if get_news:
    parameter2 = {
        'apiKey': '8e6b277e08c74593baea99ff47378ec1',
        'qInTitle': COMPANY_NAME,
    }

    response2 = requests.get(url='https://newsapi.org/v2/everything', params=parameter2)
    response2.raise_for_status()
    data2 = response2.json()
    data2 = data2['articles'][:3]
    print(data2)

## STEP 3: Use https://www.twilio.com
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

