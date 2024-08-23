from datetime import datetime

class FormatMessage:
    def __init__(self, data) -> None:
        self.contact_name = data.get('chatName')if data.get('chatName') else '?'
        self.user_name = data.get('senderName') if data.get('senderName') else '?'
        self.client_phone = data.get('phone') if data.get('phone') else '?'
        self.owner_phone = data.get('connectedPhone') if data.get('connectedPhone') else '?'
        self.is_group = data.get('isGroup') if data.get('isGroup') != None else False
        self.from_client = not data.get('fromMe') if data.get('fromMe') != None else False
        self.message_time = data.get('momment') if data.get('momment') else datetime.now()
        
    def message_fields(self):
        return {
            "contact_name":self.contact_name,
            "user_name":self.user_name,
            "client_phone":self.client_phone,
            "owner_phone":self.owner_phone,
            "is_group":self.is_group,
            "from_client":self.from_client,
            "message_time":self.message_time,
        }