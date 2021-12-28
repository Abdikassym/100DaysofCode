from bs4 import BeautifulSoup
import requests
import smtplib
from os import environ

my_email = "thespasrabota@gmail.com"
my_pass = environ.get("my_email_pass")

current_price = 81.00
my_price = 70.00
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"
accept_lng = "en-GB,en-US;q=0.9,en;q=0.8"

headers = {
    "User-Agent": user_agent,
    "Accept-Language": accept_lng,
}

good_url = "https://www.amazon.com/Luby-GT606-Pressure-Cooker-340320340mm/dp/B07DWHSPCF/ref=sr_1_1_sspa?crid=2BHNMPH0H8HQQ&keywords=pressure+cooker&qid=1640673886&sprefix=pressure+cooker%2Caps%2C245&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyS0RWVVFUWUNGSllHJmVuY3J5cHRlZElkPUEwODg1NzU4MTU0RDk3ME1IOVBMWSZlbmNyeXB0ZWRBZElkPUEwNTA0NzMwUFRTNDRZWDhXUEJUJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="

respone = requests.get(url=good_url, headers=headers)
webpage = respone.content
soup = BeautifulSoup(webpage, "lxml")

price = float(soup.find(name="span", id="price_inside_buybox").text[2:])

if price <= my_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_pass)
        connection.sendmail(from_addr=my_email,
                            to_addrs="abdikasymt@gmail.com",
                            msg=f"Price has went down!\nPrevious price was: {current_price}.\nNow it's {price}")