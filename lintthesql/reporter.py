import atexit

class Reporter:
    messages = []

    @staticmethod
    def add_message(message):
        Reporter.messages.append(message)

@atexit.register
def report():
    for message in Reporter.messages:
        print(message)
