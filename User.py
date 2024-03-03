from Post import TextPost
from Post import ImagePost
from Post import SalePost

# Define an interface or base class for observers
class Notification:
     
    def receive_notification_about_your_follow(self, notification):
        pass
     
    def receive_notification_about_your_post(self, notification):
        pass

class User(Notification):
    def __init__(self, username, network, password):
        self.username = username
        self.network = network
        self.password = password
        self.connected = True
        self.followers = []  # followers
        self.posts = []  # List to store posts
        self.notifications = []

    def __str__(self):
        return f"User name: {self.username}, Number of posts: {len(self.posts)}, Number of followers: {len(self.followers)}\n"
        
    def follow(self, other_user):
        if other_user != self and self.connected:
            if self not in other_user.followers:
                other_user.followers.append(self)
                print(f"{self.username} started following {other_user.username}")
            else:
                pass
                #print(f"User {self.username} is already following user {other_user.username}")
        else:
            pass
            #print("Cannot follow")
    
    def unfollow(self, other_user):
        if self in other_user.followers and self.connected:
            other_user.followers.remove(self)
            print(f"{self.username} unfollowed {other_user.username}")
        else:
            print(f"Cannot unfollow")
    
    def publish_post(self, style, content, location = None, price = 0):
        if self.connected:
            if style == "Text":
                post = TextPost(self, content)
                self.posts.append(post)
                print(f"{self.username} published a post:\n\"{content}\"\n")
                for user in self.followers:
                    user.receive_notification_about_your_follow(f"{self.username} has a new post")
                return post
                
            if style == "Image":
                post = ImagePost(self, content)
                self.posts.append(post)
                print(f"{self.username} posted a picture\n")
                for user in self.followers:
                    user.receive_notification_about_your_follow(f"{self.username} has a new post")
                return post
            
            if style == "Sale":
                post = SalePost(self, content, location, price)
                self.posts.append(post)
                print(f"{self.username} posted a product for sale:\nFor sale! {content}, price: {price}, pickup from: {location}\n")
                for user in self.followers:
                    user.receive_notification_about_your_follow(f"{self.username} has a new post")
                return post
            
    def receive_notification_about_your_follow(self, notification):
        self.notifications.append(notification)

    def receive_notification_about_your_post(self, notification, comment = None):
        self.notifications.append(notification)
        if(comment != None):
            print(f"notification to {self.username}: {notification}: {comment}")
        
        else:
            print(f"notification to {self.username}: {notification}")
                  
    def print_info(self):
        print(f"Username: {self.username}")
        print("Followers:", ", ".join(self.followers))
        print("Posts:", len(self.posts))
    
    def print_notifications(self):
        print(f"{self.username}'s notifications:")
        for notification in self.notifications:
            print(f"{notification}")
