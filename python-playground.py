# Playing with date time

# from datetime import timedelta, datetime
#
# timestamp = datetime.utcnow()
# print(f"===>>> Now: {timestamp}")
# # print(f"===>>> Date object type: {type(timestamp)}")
#
# fourty_minutes_before_now = timestamp - timedelta(minutes=40.0)
# print(f"===>>> Twenty minutes before: {fourty_minutes_before_now}")
#
# half_hour_before_now = timestamp - timedelta(minutes=30.0)
# print(f"===>>> Half hour before: {half_hour_before_now}")
#
# print(f"{half_hour_before_now >= fourty_minutes_before_now}")


# response = timestamp - twenty_minutes_before_now
# print(f"===>>> Response: {twenty_minutes_before_now in range(half_hour_before_now, timestamp)}")
# print(f"Is this hour in half hour ago? {}")
# now = datetime.utcnow()
# print(f"DATE TIME NOW IS: {now}")
# print(f"Data type: {type(now)}")

# updated_at=datetime.datetime(2022, 10, 10, 17, 54, 41, 158743, tzinfo=<UTC>)
# (ano= 2022, mes = 10, dia = 10, hora = 17, minuto = 54, segundo = 41, microsegundo = 158743, tzinfo=<UTC>

# from datetime import datetime
#
# # now() gives current date and time
# current = datetime.now()
#
# # print combinedly
# print(current)
# print("\n")
# print("print each term individually")
#
# day = current.strftime("%d")
#
# # print day
# print("day:", day)
#
# month = current.strftime("%m")
#
# # print month
# print("month:", month)
#
# year = current.strftime("%Y")
#
# # print year
# print("year:", year)
#
# time = current.strftime("%H:%M:%S")
#
# # time in hour, minute and second
# print("time:", time)
#
# print("\n")
# print("printing date and time together")
# date_time = current.strftime("%m/%d/%Y, %H:%M:%S")
# print("date and time:", date_time)
# print("\n")
#
# # fetching details from timestamp
# timestamp = 1615797322
# date_time = datetime.fromtimestamp(timestamp)
#
# # %c, %x and %X are used for locale's proper date and time representation
# time_1 = date_time.strftime("%c")
# print("first_output:", time_1)
#
# time_2 = date_time.strftime("%x")
# print("second_output:", time_2)
#
# time_3 = date_time.strftime("%X")
# print("third_output:", time_3)
#
# print("\n")
#
# # assigning each term manually
# manual = datetime(2021, 3, 28, 23, 55, 59, 342380)
# print("year =", manual.year)
# print("month =", manual.month)
# print("hour =", manual.hour)
# print("minute =", manual.minute)
# print("timestamp =", manual.timestamp())


# Playing with dictionaries
# class Payload:
#     def __init__(self, connection_type: str, operator_name: str, imsi, ddd: str, sample_number: str):
#         self.connection_type = connection_type
#         self.operator_name = operator_name
#         self.imsi = imsi
#         self.ddd = ddd
#         self.sample_number = sample_number
#
#     def get_request_configuration(self):
#         return {
#             "connectionType": f"{self.connection_type}",
#             "operatorName": f"{self.operator_name}",
#             "imsi": f"{self.imsi}",
#             "ddd": f"{self.ddd}",
#             "sampleNumber": f"{self.sample_number}"
#         }
#
#     def validate_request_configuration(self, config: dict) -> dict:
#         config.pop("operatorName") if config["operatorName"] == "False" else None
#         config.pop("imsi") if config["imsi"] == "False" else None
#         config.pop("ddd") if config["ddd"] == "False" else None
#         config.pop("sampleNumber") if config["sampleNumber"] == "False" else None
#         return config
#
#
# Config_Class = Payload(connection_type="wifi",
#                        operator_name="Tim",
#                        imsi=["+5592992671932", "+5511993623481"],
#                        ddd="False",
#                        sample_number="False"
#                        )
#
# # config_dict = Config_Class.get_request_configuration()
# # config_dict_validated = Config_Class.validate_request_configuration(config_dict)
# # print(f"validated request: {config_dict_validated['imsi']}")
# # print(f"===>>> Possui solicitacao de imsi: {config_dict_validated["imsi"]}")
#
# config_dict = Config_Class.get_request_configuration()
# config_dict_validated = Config_Class.validate_request_configuration(config_dict)
# print(config_dict_validated)
#
#
# def is_imsi(configuration: dict) -> bool:
#     return configuration.get('imsi') is not None
#
#     # is_imsi: bool = True
#     # try:
#     #     config_dict_validated[imsi]
#     #     return is_imsi
#     # except KeyError:
#     #     is_imsi = False
#     #     return is_imsi
#
#
# # try:
# #     config_dict_validated["imsi"]
# #     print('The key exists in the dictionary')
# # except KeyError as error:
# #     print("The key doesn't exist in the dictionary")
# #
# print(f"==>> Possui imsi: {is_imsi(config_dict_validated)}")


# Playing with strings

# Extract the ddd code from a cellphone number
# class GetBrazilDDDCode:
#
#     def validate_brazil_country_code(self, country_code: int) -> bool:
#         return True if country_code == 55 else None
#
#     def get_brazil_code(self, imsi: str):
#         parsed_number = phonenumbers.parse(imsi)
#         country_code_number = phonenumbers.parse(imsi, None).country_code
#         is_brazil_code = self.validate_brazil_country_code(country_code_number)
#         brazil_national_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)
#         return brazil_national_number[1:3] if is_brazil_code is not None else None


# Playing with random and list (selecting random samples from a list)
# import random
# #
# # test_list = [1, 4, 5, 2, 7]
# # print("Original list is : " + str(test_list))
# #
# # print("Random element is :", random.sample(test_list, 4))


# Playing with datetime utc format (extracting actual datetime utc value)
# from datetime import datetime

# actual_utc_datetime = datetime.utcnow()
# print(f"ACTUAL DATETIME: {actual_utc_datetime}")

# from datetime import datetime

# Getting the current date and time
# dt = datetime.now()
#
# # getting the timestamp
# ts = datetime.timestamp(dt)
#
# print("Date and time is:", dt)
# print("Timestamp is:", ts)


#token 1
# token_1 = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhZG1pbkBiZWVnb2wuY29tIiwiaWF0IjoxNjY5MTQ4MjA2LCJuYmYiOjE2NjkxNDgyMDYsImp0aSI6IjgzZDRiMWM3LTAyN2QtNGMxNy04YzE3LWQzN2Y4YjQ1MGMxMiIsImV4cCI6MTY2OTE0OTEwNiwidHlwZSI6ImFjY2VzcyIsImZyZXNoIjpmYWxzZX0.JgK65WPdUzsBCOTsEvdfWKumjPH_bKbWrhB2DbChvjw"
# token_2 = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhZG1pbkBiZWVnb2wuY29tIiwiaWF0IjoxNjY5MTQ4MjA2LCJuYmYiOjE2NjkxNDgyMDYsImp0aSI6IjgzZDRiMWM3LTAyN2QtNGMxNy04YzE3LWQzN2Y4YjQ1MGMxMiIsImV4cCI6MTY2OTE0OTEwNiwidHlwZSI6ImFjY2VzcyIsImZyZXNoIjpmYWxzZX0.JgK65WPdUzsBCOTsEvdfWKumjPH_bKbWrhB2DbChvjw"
#
# print(token_2 == token_1)

# Playing with datime
from datetime import datetime, date, timedelta

# Get string format and return datetime format
# date_string = "11/29/2022"
# print("date_string =", date_string)
#
# date_object = datetime.strptime(date_string, "%m/%d/%Y")
# print("date_object =", date_object)
# print(type(date_object))

# Get date format and return datetime format
# my_time = datetime.min.time()
# print("The time object:" , my_time)
# my_date: date = 2022-11-29
# my_datetime = datetime.combine(my_date, my_time)
# print("The combined datetime object:",my_datetime)

# Get datetime format and return a 24 four hour later date of the datetime type
# my_datetime = datetime.today()
# print(f"====>>>> MY DATETIME: {my_datetime}")
# twenty_four_hours_later = my_datetime + timedelta(hours=24)
# print(f"===>>> Twenty minutes before: {twenty_four_hours_later}")
# print(f"{type(twenty_four_hours_later)}")


branch_detailing_body ="""{"startDate":"${dataInicial}","endDate":"${dataFinal}","node":null,"state":[],"city":[],"daysMinWithProblem":"1","KPI":["D","U","PL","L","J"],"numberMax":"500","mac":"","cmts":null,"port":"","cto":null,"typeFilter":"any","nodeRootProblem":false,"qoe":[0,7],"qoeAccess":[0,7],"qoeAvailability":[0,7],"qoeWifi":[0,7],"enableSliderQoe":false,"enableSliderQoeAccess":false,"enableSliderQoeAvailability":false,"EnableSliderQoeWifi":false,"tab":2,"view":"mean"}"""
jmeter_detailing_body ="""{"startDate":"${dataInicial}","endDate":"${dataFinal}","node":null,"state":[],"city":[],"daysMinWithProblem":"1","KPI":["D","U","PL","L","J"],"numberMax":"500","mac":"","cmts":null,"port":"","cto":null,"typeFilter":"any","nodeRootProblem":false,"qoe":[0,7],"qoeAccess":[0,7],"qoeAvailability":[0,7],"qoeWifi":[0,7],"enableSliderQoe":false,"enableSliderQoeAccess":false,"enableSliderQoeAvailability":false,"EnableSliderQoeWifi":false,"tab":2,"view":"mean"}"""

print(50*"=")
print("Is branch body equal to jmeter body request?")
print(f"====>>>>{branch_detailing_body == jmeter_detailing_body}")
print(50*"=")