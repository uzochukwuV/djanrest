from allauth.account.views import LoginView

class MyLoginView(LoginView):
    def __init__(self, *args, **kwargs):
        super(MyLoginView, self).__init__(*args, **kwargs)
        print(self)
