import re


def check_valid_email(inbound_email: str):

    pattern = re.compile(r"[a-zA-Z+-_.]+@[a-z]+\.[a-z]+")
    if re.match(pattern, inbound_email):
        return True
    else:
        return False


def check_valid_phone_number(inbound_country_code: str, inbound_number: str):

    phone_pattern = re.compile(r"[0-9]{10}")
    country_code_pattern = re.compile(r"\+[0-9]{1-4}")

    if re.match(phone_pattern, inbound_number) and re.match(
        country_code_pattern, inbound_country_code
    ):
        return True
    return False


def check_valid_name(inbound_name: str):
    pattern = re.compile(r"[a-zA-Z]*\s?[a-zA-Z]?")

    if re.match(pattern, inbound_name):
        return True
    return False
