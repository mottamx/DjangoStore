class Cart():

    def __init__(self, request):
        #Returning user
        self.session = request.session
        cart = self.session.get('session_key')
        #Create new session
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
        self.cart = cart
