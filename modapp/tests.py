from django.test import TestCase

# Create your tests here.
"""if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('comments')

        data = {
            'name':name,
            'email': email,
            'subject': subject,
            'message': message
        }

        message = ''' 
        New Message : {}

        From : {}
        '''.format(data['message'], data['email'])

        send_mail(data['subject'], message,'' ,['qweaverinfo@gmail.com'])
        return render(request, 'layouts/auth-signup-success.html', locals())

    return render(request, 'layouts/contact.html', locals())"""