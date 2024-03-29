from urllib.request import urlopen as uReq
from urllib.request import Request
from bs4 import BeautifulSoup as soup
import csv

# The following code makes a request to the the site below which holds all of the data
# Keeping actual website anonymous
url = "https://www.somewebsite"
req = Request(
    url,
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
    }
)
uClient = uReq(req)
page_html = uClient.read()
uClient.close()
# This makes the content as a BeautifulSoup object
page_soup = soup(page_html, "html.parser")
# Parses though page content and stores all of the price information in one list
all_columns = page_soup.findAll("div", {"class": "cell__content"})
# Saves the prices of the previous day into a variable 
date = all_columns[7].text
open_price = all_columns[8].text.replace("$", "")
high_price = all_columns[9].text.replace("$", "")
low_price = all_columns[10].text.replace("$", "")
close_price = all_columns[11].text.replace("$", "")

# Saves bitcoin prices into an excel file
new_row = [date, str(open_price.replace(",", "")), str(high_price.replace(
    ",", "")), str(low_price.replace(",", "")), str(close_price.replace(",", ""))]
with open("C:\\MLCourse\\Projects\\Bitcoin_2021.csv", 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(new_row) 
    

# Confirm results
print("The bitcoin prices for", date,
      "have been succesfully saved into the excel file")
print("Open:", open_price, "\nClose:", close_price,
      "\nHigh:", high_price, "\nLow:", low_price)
print("The magic number is 324")
