import uuid

def create_message(sender, receiver, msg_type, payload):
    return {
        "sender": sender,
        "receiver": receiver,
        "type": msg_type,
        "trace_id": str(uuid.uuid4()),
        "payload": payload
    }
