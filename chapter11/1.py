"""
Command Line Emailer
Write a program that takes an email address and string of text on the command line and then, using Selenium, logs into your email account and
sends an email of the string to the provided address. (You might want to set
up a separate email account for this program.)
This would be a nice way to add a notification feature to your programs.
You could also write a similar program to send messages from a Facebook
or Twitter account

"""

class Message:

    def __init__(self, text):
        self.text = text


    def send_email(self, address):
        pass


    def send_whatsapp(self,):
        pass


    def send_twitter(self):
        pass


if __name__ == '__main__':
    send_email()
