import os
import logging
class Config:
    API_ID = int(os.environ.get("API_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    Channel_id = os.environ.get("Channel_id", "-1002097884361")
    Drivebuzz_crypt = os.environ.get("Drivebuzz_crypt", "")
    Drivefire_crypt = os.environ.get("Drivefire_crypt", "cXRocHpOUzJEcFhHUWhhQmdvbVU5a1VnVG15cHFZQ0h5c2o5UGpUSkhaOD0%3D")
    Jiodrive_crypt = os.environ.get("Jiodrive_crypt", "")
    Gadrive_crypt = os.environ.get("Gadrive_crypt", "")
    Kolop_crypt = os.environ.get("Kolop_crypt", "")
    Katdrive_crypt = os.environ.get("Katdrive_crypt", "")
    Gtot_crypt = os.environ.get("Gtot_crypt", "bzBSd2p5RWN3b2FaOWEvWWRRU0F2WEo4THhOQWI2bUpEUjhWSFJlZUZXWT0%3D")
    Appdrive_email = os.environ.get("Appdrive_email", "pp2121696@gmail.com")
    Appdrive_password = os.environ.get("Appdrive_password", "Satyajit@#$123")
    Hubdrive_crypt = os.environ.get("Hubdrive_crypt", "a2VlUUVqZElndE4wT2txUVBPZ3R5VWorUnBUTHlmVDdhZ1p5NVNDeGpQUT0%3D")
    Sharerpw_xsrf_token = os.environ.get("Sharerpw_xsrf_token", "eyJpdiI6IlBITUYyTUcwblllb2pUa0xcL2lcL1FMQT09IiwidmFsdWUiOiJmRVJMaUtYeDdwYjhPY0g1ekhjeVwvWHZjMEhmMXhiNGFqbnhDbDV4S3hya3RNVExhTlVZXC95SDRQV1hOQzZTZysiLCJtYWMiOiIyYTM5MTk3Njg4NDJlYTY4ZjRiZWQ1MzAwOWYwZWEwMzdlOWJkOGU2YzgxYWI2ZTRjNTQwMjgzMGU1ZDAzNDRjIn0")
    Sharerpw_laravel_session = os.environ.get("Sharerpw_laravel_session", "eyJpdiI6IjJkb1dYOE03cEpRQTBQMFJ0RDBweWc9PSIsInZhbHVlIjoiRTJpWlk2ZTEzbkhPY3hLQ0x1WnBUMnQ4YVdITFR2VTJ1WlNcL2ZmUFpQOUFKQ0VjXC92dk5reCtpYk1XamRYZGFQIiwibWFjIjoiYmZmMjU4NjdjZTQ0NGZkNDM2OGUwOGQ4MGVmNDk1YWNiMGZhZjg3OTQ2NzQyMzU2ZDFmN2Q3NDE0ZmM5OGNlNiJ9")
