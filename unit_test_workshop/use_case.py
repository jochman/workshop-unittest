import uuid
from typing import TypedDict

class Data(TypedDict):
    id: str
    db_id: str
    email_id: str
    email_address: str

def send_email(data: Data):
    email = data["email_address"] 
    data["email_id"] = str(uuid.uuid4())
    return data

def create_entry_in_db(data: Data):
    data["db_id"] = str(uuid.uuid4())
    return data

def process_data(data: Data):
    data["id"] = data["id"].lower()
    return data
        


def enter_data_flow(data: Data):
    data = process_data(data)
    data = create_entry_in_db(data)
    send_email(data)
    return data
    