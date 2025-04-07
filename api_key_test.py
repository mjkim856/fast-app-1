import base64
import hmac
from datetime import datetime


def parse_params_to_str(params: dict):
    url = "?"
    for key, value in params.items():
        url = url + str(key) + "=" + str(value) + "&"
    return url[1:-1]


def hash_string(params: dict, secret_key: str):
    mac = hmac.new(
        bytes(secret_key, encoding="utf8"), bytes(parse_params_to_str(params), encoding="utf-8"), digestmod="sha256"
    )
    digest = mac.digest()
    validating_secret = str(base64.b64encode(digest).decode("utf-8"))
    return validating_secret


p = {"ts": int(datetime.utcnow().timestamp()), "access_key": "3BU9iFmRSZu93at9ZeX86fMd"}
print(p)
print(hash_string(p, "OPPMQle42N5Uxb2V5UR85n1sxriHjMQ0"))
