from datetime import datetime
import pytz

def ist_date():
    utc = datetime.now(pytz.utc)
    timezone = pytz.timezone("Asia/Kolkata") 
    ist = utc.astimezone(timezone)
    return ist.date()