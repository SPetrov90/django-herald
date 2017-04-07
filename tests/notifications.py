from herald.base import EmailNotification, TwilioTextNotification
from herald import registry
from herald.base import EmailNotification
from email.mime.image import MIMEImage

class MyNotification(EmailNotification):
    context = {'hello': 'world'}
    template_name = 'hello_world'
    to_emails = ['test@test.com']

    def get_attachments(self):
        # this returns two attachments, one a text file, the other an inline attachment that can be referred to in a
        # template using cid: notation
        fp = open('python.jpeg', 'rb')
        img = MIMEImage(fp.read())
        img.add_header('Content-ID', '<{}>'.format('python.jpg'))

        raw_data = 'Some Report Data'

        return [
            ('Report.txt', raw_data, 'text/plain'),
            img,
        ]


registry.register(MyNotification)


class MyTwilioNotification(TwilioTextNotification):
    context = {'hello': 'world'}
    template_name = 'hello_world'
    to_emails = ['test@test.com']

registry.register(MyTwilioNotification)
