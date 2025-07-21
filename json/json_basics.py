# # JSON Basics
#
# import json
#
# car_data = {"name": "byd", "engine": "electric"}
#
# print(type(car_data))
#
# # json.dumps() - converts to string (returns string)
# car_data_json_string = json.dumps(car_data)
# print(car_data_json_string)
# print(type(car_data_json_string))
#
# # vs json.dump() - creates a stream object and writes that object to a file (returns None)
# with open("car_data.json", "w") as jsonfile:
#     json.dump(car_data, jsonfile)



# # Extracting info from json_file
#
# import json
#
# class RatesParser:
#
#     def __init__(self, rates_file):
#         rates_info = self._open_json_file(rates_file)
#         self.base = rates_info['base']
#         self.date = rates_info['date']
#         self.rates = rates_info['rates']
#         self.aud = self.rates['AUD']
#         self.gbp = self.rates['GBP']
#
#     def _open_json_file(self, file):
#         with open(file) as rates:
#             return json.load(rates)
#
# rate_reader = RatesParser("exchange_rates.json")
#
# print(rate_reader.gbp)
# print(rate_reader.rates)
#




# # Using APIs with requests
#
# import json
#
# import requests
#
# post_codes_req = requests.get("http://api.open-notify.org/astros.json")
#
# print(post_codes_req.text)
# print(post_codes_req.status_code)
# print(post_codes_req.headers)
# print(post_codes_req.encoding)
# print(post_codes_req.content)
# print(type(post_codes_req.json()))
#




# # Reading JSON
# import json
#
# #json.load() - reads json from file, convert to python dict
# with open("car_data.json", "r") as jsonfile:
#     car = json.load(jsonfile)
#     print(type(car))
#     print(car)
#
# # json.loads() - convert into dict
# my_json_data = '{"name": "luke", "Birthplace": "southport"}'
# print(type(my_json_data))
#
# # converted into dict
# parsed_json_data = json.loads(my_json_data)
# print(type(parsed_json_data))
#




# # Post request for postcodes api
#
# import requests
# import json
#
# json_body = json.dumps({"postcodes": ["PR3 0SG", "M45 6GN", "EX165BL"]})
# headers = {"Content-Type": "application/json"}
#
# post_multi_req = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json_body)
#
# print(post_multi_req.json())

