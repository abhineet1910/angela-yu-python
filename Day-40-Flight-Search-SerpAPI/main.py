import requests_cache
from pprint import pprint
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager


# ==================== Conserve requests and preserve your free plan ====================
requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600,
    }
)
# ==================== Setup ====================
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
# pprint(sheet_data)
customer_data= data_manager.get_customer_emails()
customer_email_list =[row["whatIsYourEmail?"] for row in customer_data]

flight_search = FlightSearch()

# Create an instance of the NotificationManager
notification_manager = NotificationManager()

# ==================== Set the Dates and Origin Airport ====================
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
ORIGIN_CITY_IATA = "BOM"  # London Heathrow

# ==================== Find Cheap Flights ====================

for row in sheet_data:
    pprint(f"Getting flights for {row['city']}...")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        row["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flights, return_date=six_month_from_today.strftime("%Y-%m-%d"))
    pprint(f"{row['city']}: INR {cheapest_flight.price}")

    if cheapest_flight.price == "N/A":
        pprint(f"No direct flight to {row['city']}: Looking for indirect flight")
        stopover_flights = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            row["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today,
            is_direct=False
        )
        cheapest_flight = find_cheapest_flight(stopover_flights, return_date=six_month_from_today.strftime("%Y-%m-%d"))
        print(f"Cheapest indirect flight price is: INR {cheapest_flight.price}")

    # --- moved OUTSIDE the "N/A" check, so it runs for BOTH direct and indirect cases ---
    print(f"DEBUG: {row['city']} -> price={cheapest_flight.price}, sheet_lowest={row['lowestPrice']}")

    if cheapest_flight.price != "N/A" and cheapest_flight.price < row["lowestPrice"]:
        data_manager.update_lowest_price(row["id"], cheapest_flight.price)

        if cheapest_flight.stops == 0:
            message = f"Low price alert! Only GBP {cheapest_flight.price} to fly direct " \
                      f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, " \
                      f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        else:
            message = f"Low price alert! Only GBP {cheapest_flight.price} to fly " \
                      f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, " \
                      f"with {cheapest_flight.stops} stop(s) " \
                      f"departing on {cheapest_flight.out_date} and returning on {cheapest_flight.return_date}."

        print(f"Check your email. Lower price flight found to {row['city']}!")
        notification_manager.send_whatsapp(message_body=message)
        # notification_manager.send_email(email_list=customer_email_list, email_body=message)
        print(f"DEBUG: {row['city']} -> price={cheapest_flight.price}, type={type(cheapest_flight.price)}, sheet_lowest={row['lowestPrice']}")