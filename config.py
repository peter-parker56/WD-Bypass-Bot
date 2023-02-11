import os
import logging
class Config:
    API_ID = int(os.environ.get("API_ID", "1701392"))
    API_HASH = os.environ.get("API_HASH", "96089a340f2892fd06aea683cbfb73c0")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5938759891:AAGjhzNRsfopOFAqw9iTfXxskpx1n1OnCgM")
    Channel_id = os.environ.get("Channel_id", "-1001806947034")
    Drivebuzz_crypt = os.environ.get("Drivebuzz_crypt", "")
    Drivefire_crypt = os.environ.get("Drivefire_crypt", "cTM5M1hNbGxpQVpKM3pHdnBXQW5sY0RibldacWVGYit5SUNQRGZOMlYzcz0%3D")
    Jiodrive_crypt = os.environ.get("Jiodrive_crypt", "%7B%22p%22%3A1%2C%22s%22%3A1676127290%2C%22t%22%3A1676127768%7D")
    Gadrive_crypt = os.environ.get("Gadrive_crypt", "")
    Kolop_crypt = os.environ.get("Kolop_crypt", "WW9rQUNKNW00d0VKaFVSaDVKSEUrdkxIQ3BlbEFnNUt5eVpHbENINllzdz0%3D")
    Katdrive_crypt = os.environ.get("Katdrive_crypt", "d3hpZVlSRVpWeWxDdzA2cjRmOWd4UTFKL3BVMmd4KzBIcHNWOWU2eGJkbz0%3D")
    Gtot_crypt = os.environ.get("Gtot_crypt", "cDFCSStZVTlBYVhRemlCNmhoVHg0ZDVmS3V4Q0lDcEw2akgwN2kvMnl2ND0%3D")
    Appdrive_email = os.environ.get("Appdrive_email", "wdzone318@gmail.com")
    Appdrive_password = os.environ.get("Appdrive_password", "wdzone#3300")
    Hubdrive_crypt = os.environ.get("Hubdrive_crypt", "TmppSkR5c1U3OFlkUEVzbkUrY0VXOW5OZFdTMFZ3bDVzMlBROU1nMFBydz0%3D")
    Sharerpw_xsrf_token = os.environ.get("Sharerpw_xsrf_token", "")
    Sharerpw_laravel_session = os.environ.get("Sharerpw_laravel_session", "")
