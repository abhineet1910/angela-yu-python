from get_spreadsheet import GetSpreadsheet
from config import *
from scrape_data import SCRAPE
zilliow_data=SCRAPE(zillow_clone)
links,prices,addresses=zilliow_data.get_lists()

# googleform=GetSpreadsheet()
# for i in range(len(links)):
#
#     googleform.fill_address(addresses[i])
#     googleform.fill_price(prices[i])
#     googleform.fill_links(links[i])
#     googleform.click_summit()
#     googleform.summit_another_request()
# # one more better way is that we
# # #
# links, prices, addresses = get_lists(zillow_clone)

spreadsheet = GetSpreadsheet()

for link, price, address in zip(links, prices, addresses):

    spreadsheet.fill_address(address)
    spreadsheet.fill_price(price)
    spreadsheet.fill_links(link)
    spreadsheet.click_submit()
    spreadsheet.submit_another_request()
print("complete filling google form")
# why ZIP
# zip() combines them like this:
#
# (link1, $2000, Address 1)
# (link2, $2500, Address 2)
# (link3, $3000, Address 3)