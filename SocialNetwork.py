from User import User

class SocialNetwork:
    _instance = None  # Singleton instance
    
    def __new__(cls, name): #*args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls) #*args, **kwargs)
            cls._instance.users = []  # List to store user instances
            cls._instance.name = name  # Network name
            print(f"The social network {name} was created!")
        return cls._instance
    
    def __str__(self):
        ans = f"{self.name} social network:"
        for user in self.users:
            ans += "\n" + str(user)
        return ans

    
    def sign_up(self, username, password):
        if len(password) < 4 or len(password) > 8:
            print("Password length must be between 4 and 8 characters.")
            return False
        
        if any(user.username == username for user in self.users):
            print("Username already exists. Please choose a different one.")
            return False
        
        user = User(username, self, password)
        self.users.append(user)
        #print(f"User '{username}' registered successfully.")
        return user
    
    def log_in(self, username, password):
        user = self.find_user(username)
        if user and password == user.password:
            user.connected = True
            print(f"{username} connected")
        else:
            print(f"User {username} not found")
    
    def log_out(self, username):
        user = self.find_user(username)
        if user and user.connected:
            user.connected = False
            print(f"{username} disconnected")
        else:
            print(f"User {username} not found")
    
    def find_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None
