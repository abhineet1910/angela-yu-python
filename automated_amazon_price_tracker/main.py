from pprint import pprint

from bs4 import BeautifulSoup
import requests
from sendmail import SENDMAIL

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/149.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
}



practice_url = "https://www.amazon.in/AGARO-Supreme-Pressure-Cleaning-Purpose/dp/B0C65HP665/ref=sxin_25_pa_sp_search_thematic_sspa?content-id=amzn1.sym.f7d72a1e-5698-491d-8e4e-cca77b240640%3Aamzn1.sym.f7d72a1e-5698-491d-8e4e-cca77b240640&crid=3LU8E9RM6EEOA&cv_ct_cx=pressure%2Bwasher&keywords=pressure%2Bwasher&pd_rd_i=B0C65HP665&pd_rd_r=242fbfe8-c8f5-4c8a-83ab-b40c49fcf9a6&pd_rd_w=9X0ta&pd_rd_wg=Feb11&pf_rd_p=f7d72a1e-5698-491d-8e4e-cca77b240640&pf_rd_r=BZNEZS12Z959FKCTTE0V&qid=1783111625&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sprefix=prea%2Caps%2C285&sr=1-1-66673dcf-083f-43ba-b782-d4a436cc5cfb-spons&aref=xQIJX7e3NE&sp_csd=d2lkZ2V0TmFtZT1zcF9zZWFyY2hfdGhlbWF0aWM&th=1"
response = requests.get(url=practice_url,headers=headers)
print(response.status_code)

soup = BeautifulSoup(response.content, 'html.parser')
price = soup.find('span',class_='a-price-whole')
price_text = price.get_text().strip()
# decimal=soup.find('span',class_='a-price-fraction')
# pri = soup.find(class_="a-offscreen").get_text()
current_price = int(price_text.replace(",", "").replace(".", ""))
title = soup.find(name="h1",class_="a-size-large a-spacing-none")
product_title = (title.get_text())
print(current_price)
print(product_title)
stop_loss = 6000

if current_price < stop_loss:
    message = f"{product_title} is on sale for : {current_price} Rupee!"
    print(repr(message))
    mailer = SENDMAIL()
    mailer.send_email("codinglord1227@gmail.com", message)


# price_without_currency = price.split("")
# price_as_float = float(price_without_currency)
# print(price_as_float)