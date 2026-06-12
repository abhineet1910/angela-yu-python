capita= {
    "france":"paris",
    "india":"mumbai",
}
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"],
# }
# print(travel_log["France"][2])
# print(travel_log["Germany"][0])
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])
travel_log = {
    "France":{"no_time_visited":8,
             "vited":["Paris", "Lille", "Dijon"]},
    "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
    }
}
print(travel_log["Germany"]["cities_visited"][2])
