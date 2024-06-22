class Message:
    def __init__(self, text):
        self.text = text
        self.fl_like = False


class Viber:
    messages = []

    @classmethod
    def add_message(cls, msg: Message):
        cls.messages.append(msg)

    @classmethod
    def remove_message(cls, msg: Message):
        cls.messages.remove(msg)

    @staticmethod
    def set_like(msg: Message):
        msg.fl_like = not msg.fl_like

    @classmethod
    def show_last_message(cls, count: int):
        for message in cls.messages[-count]:
            print(message.text)

    @classmethod
    def total_messages(cls) -> int:
        return len(cls.messages)
