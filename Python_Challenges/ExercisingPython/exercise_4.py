"""
    Make a code that separates a phone number code (local code) from the rest of the phone number
"""

import phonenumbers

imsi_brazilian = "+5511992671955"


class GetBrazilDDDCodeService:

    def __init__(self, imsi: str):
        self._imsi = imsi

    def _get_parsed_imsi(self):
        return phonenumbers.parse(self._imsi)

    def _extract_brazil_country_code(self) -> int:
        return phonenumbers.parse(self._imsi, None).country_code

    def _get_brazil_national_number(self):
        return phonenumbers.format_number(self._get_parsed_imsi(), phonenumbers.PhoneNumberFormat.NATIONAL)

    def _validate_brazil_country_code(self) -> bool:
        country_code = self._extract_brazil_country_code()
        return True if country_code == 55 else None

    def extract_brazil_ddd(self) -> str:
        p = self._get_brazil_national_number()
        return p[1:3] if self._validate_brazil_country_code() is not None else print("===>>> This is not a local phone "
                                                                                     "number code for Brazil")


get_ddd = GetBrazilDDDCodeService(imsi=imsi_brazilian)
brazil_ddd = get_ddd.extract_brazil_ddd()
print(f"===>>> Brazil DDD: {brazil_ddd}")
# x = phonenumbers.parse(imsi_brazilian, None).country_code
# print(x)
# print(type(x))
# print(f"===>>> x: {x}")
# print(f"COUNTRY CODE: {x.country_code}")
# country_code = x.country_code
# p = phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.NATIONAL)
# p = phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.RFC3966)
# region = phonenumbers.region_codes_for_country_code(x.country_code)
# region = phonenumbers.national_significant_number(x)
# print(f"===>>> {p}")
# if country_code == 55:
#     ddd = p[1:3]
#     print(ddd)
    # p.replace(")", "")

# print(p)
# print(f"===>>> Region Code: {region}")

# usa_imsi = "+632835551054"
#
# z = phonenumbers.parse(usa_imsi, None)
# print(f"===>>> {z}")
#
# q = phonenumbers.format_number(z, phonenumbers.PhoneNumberFormat.NATIONAL)
# print(f"===>>> {q}")
