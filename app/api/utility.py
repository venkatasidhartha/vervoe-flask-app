from datetime import datetime
from uuid import uuid4

def writeTOfile(filenameWithExtension:str,data):
    format_data = "%d-%m-%y %H:%M:%S"
    dateTime = datetime.strftime(datetime.now(),format_data)
    with open(f"catpure_data_error/{str(uuid4())}-{dateTime}-{filenameWithExtension}","w") as f:
        f.write(data)