from django.core import mail
from django.core.mail import send_mail, EmailMessage

#To store the details of the message
class Envelope(object):
    '''This is the email that we are sending from'''
    
    def __init__(self, from_email, recipient_list, subject=None):
        '''Constructor'''
        self.from_email = from_email
        self.recipient_list = recipient_list
        self.subject = subject



#Handles the sending of emails
class Mailer(object):
    '''This will send the list of recipients the email without each other being seen in the To: field'''
    def send_individual_mail(self, envelope, message, reply_to=None, plain_text=True):
        #Set up the parameters needed to send the email
        
        #Control the opening and closing of the connections to improve efficiency to prevent creating and destroying a connection every time an email is sent.
        connection = mail.get_connection()
        connection.open()
        
        n = len(envelope.recipient_list)
        for i in range(n):
            email_recipient = [envelope.recipient_list[i]]
            if reply_to == None
                email = EmailMessage(envelope.subject, message, envelope.from_email, email_recipient, connection=connection)
            else
                email = EmailMessage(envelope.subject, message, envelope.from_email, email_recipient, connection=connection, headers = {'Reply-To': reply_to})
            if plain_text != True:
                email.content_subtype = 'html'
            email.send()
        
        connection.close()