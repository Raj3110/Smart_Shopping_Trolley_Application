import random
import datetime
from storage import log_event

def generate_otp():
    return random.randint(1000, 9999)

def timestamp():
    return str(datetime.datetime.now())

def audit(message):
    log_event(f"{timestamp()} - {message}")
