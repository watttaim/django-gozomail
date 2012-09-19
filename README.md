## django-gozomail

Django Gozomail makes emailing easier. Allows for bulk sends as well as single email sending.
Alternatively hooks into some form of analytics.


Example to send an email using django-gozomail

    from django-gozomail.views import Envelope, Mailer

    def send_email(request):
        if request.method == 'POST':
            try:
                envelope = Envelope('taimin@gozolabs.com', recipient_list=['watttaim@gmail.com'], subject='Hello dude')
                mailer = Mailer()
                username = 'Watt'
                plaintext = get_template('email.txt')
                htmly     = get_template('email.html')
                d = Context({ 'username': username })
                text_message = plaintext.render(d)
                html_message = htmly.render(d)
                reply_to = 'ubsub@advocado.com'
                mailer.send_individual_mail(envelope,html_message,reply_to,False)
            except KeyError:
                return HttpResponse('Please fill in all fields')