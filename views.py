from django.core import mail
from django.core.mail import send_mail, EmailMessage
from django.template import Context
from boto.ses.exceptions import SESError

#To store the exceptions returned from sending the email
class GozoMailError(object):
    '''This stores email address and its delivery errors'''
    def __init__(self, email_recipient, ses_error):
        '''Constructor'''
        self.email_recipient = email_recipient
        self.error = ses_error

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
    '''Mailer provides methods to send out emails, single or mass'''
    
    def send_individual_mail(self, envelope, message, reply_to=None, plain_text=True):
        '''This sends out the same message to the list of recipients without each recipients being able to see each other email address'''
        #Control the opening and closing of the connections to improve efficiency to prevent creating and destroying a connection every time an email is sent.
        connection = mail.get_connection()
        connection.open()
        error_list = []
        
        n = len(envelope.recipient_list)
        for i in range(n):
            try:
                email_recipient = [envelope.recipient_list[i]]
                if reply_to != None:
                    email = EmailMessage(envelope.subject, message, envelope.from_email, email_recipient, connection=connection, headers = {'Reply-To': reply_to})
                else:
                    email = EmailMessage(envelope.subject, message, envelope.from_email, email_recipient, connection=connection)
                if plain_text != True:
                    email.content_subtype = 'html'
                email.send()
            except SESError, e:
                #Store each email address and its corresponding error
                gozo_mail_error = GozoMailError(email_recipient, e)
                error_list.append(gozo_mail_error)
        
        connection.close()
        return error_list