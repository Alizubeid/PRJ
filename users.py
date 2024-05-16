class User:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self._auth = False
        
    def auth(self):
        query = "SELECT password FROM users where username='{}'".format(self.username)
        