from datetime import datetime

def utcnow():
    return datetime.utcnow().isoformat(timespec='milliseconds')
