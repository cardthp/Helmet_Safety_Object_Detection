def send_mail():
    API_KEY='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'

    import base64
    import os
    import json
    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import (
        Mail, Attachment, FileContent, FileName,
        FileType, Disposition, ContentId)
    try:
        # Python 3
        import urllib.request as urllib
    except ImportError:
        # Python 2
        import urllib2 as urllib

    import os
    import json
    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail

    message = Mail(
        from_email='thanaphat.kar@gmail.com',
        to_emails='thanaphat.kar@gmail.com',
        subject='Helmet Found',
        html_content='<strong>Pass</strong>')
    file_path = 'C:/Tensorflow/models/research/object_detection/zresult/imagepdf.pdf'
    with open(file_path, 'rb') as f:
        data = f.read()
        f.close()
    encoded = base64.b64encode(data).decode()
    attachment = Attachment()
    attachment.file_content = FileContent(encoded)
    attachment.file_type = FileType('application/pdf')
    attachment.file_name = FileName('Helmet Found.pdf')
    attachment.disposition = Disposition('attachment')
    attachment.content_id = ContentId('Example Content ID')
    message.attachment = attachment
    try:
        #for environ on computer
        #sendgrid_client = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        sendgrid_client = SendGridAPIClient(API_KEY)
        response = sendgrid_client.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)