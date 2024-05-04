class Email:
    def __init__(self,sender,receiver,content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
information = input()
while information != "Stop":
    sender,receiver,content = information.split()
    email = Email(sender, receiver, content)
    emails.append(email)

    information = input()


indexes = [int(el) for el in input().split(", ")]

for index, some_email in enumerate(emails):
    if index in indexes:
        emails[index].send()
    print(emails[index].get_info())