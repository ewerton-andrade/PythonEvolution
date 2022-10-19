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
class Payload:
    def __init__(self, connection_type: str, operator_name: str, imsi, ddd: str, sample_number: str):
        self.connection_type = connection_type
        self.operator_name = operator_name
        self.imsi = imsi
        self.ddd = ddd
        self.sample_number = sample_number

    def get_request_configuration(self):
        return {
            "connectionType": f"{self.connection_type}",
            "operatorName": f"{self.operator_name}",
            "imsi": f"{self.imsi}",
            "ddd": f"{self.ddd}",
            "sampleNumber": f"{self.sample_number}"
        }

    def validate_request_configuration(self, config: dict) -> dict:
        config.pop("operatorName") if config["operatorName"] == "False" else None
        config.pop("imsi") if config["imsi"] == "False" else None
        config.pop("ddd") if config["ddd"] == "False" else None
        config.pop("sampleNumber") if config["sampleNumber"] == "False" else None
        return config


Config_Class = Payload(connection_type="wifi",
                       operator_name="Tim",
                       imsi=["+5592992671932", "+5511993623481"],
                       ddd="False",
                       sample_number="False"
                       )

# config_dict = Config_Class.get_request_configuration()
# config_dict_validated = Config_Class.validate_request_configuration(config_dict)
# print(f"validated request: {config_dict_validated['imsi']}")
# print(f"===>>> Possui solicitacao de imsi: {config_dict_validated["imsi"]}")

config_dict = Config_Class.get_request_configuration()
config_dict_validated = Config_Class.validate_request_configuration(config_dict)
print(config_dict_validated)


def is_imsi(configuration: dict) -> bool:
    return configuration.get('imsi') is not None

    # is_imsi: bool = True
    # try:
    #     config_dict_validated[imsi]
    #     return is_imsi
    # except KeyError:
    #     is_imsi = False
    #     return is_imsi


# try:
#     config_dict_validated["imsi"]
#     print('The key exists in the dictionary')
# except KeyError as error:
#     print("The key doesn't exist in the dictionary")
#
print(f"==>> Possui imsi: {is_imsi(config_dict_validated)}")
