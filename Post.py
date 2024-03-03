import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

class Post:
    def __init__(self, user):
        self.user = user
        self.likes = []  # Set to store users who liked the post
        self.comments = []  # List to store comments
    
    def like(self, other_user):
        self.likes.append(other_user)
        self.user.receive_notification_about_your_post(f"{other_user.username} liked your post")
    
    def comment(self, other_user, comment):
        self.comments.append([other_user, comment])
        self.user.receive_notification_about_your_post(f"{other_user.username} commented on your post", comment)
    


class TextPost(Post):
    def __init__(self, user, content):
        super().__init__(user)
        self.content = content

    def __str__(self):
        return f"{self.user.username} published a post:\n\"{self.content}\"\n"

    def like(self, other_user):
        super().like(other_user)
    
    def comment(self, other_user, comment):
        super().comment(other_user, comment)
        
class ImagePost(Post):
    def __init__(self, user, image_path):
        super().__init__(user)
        self.image_path = image_path

    def __str__(self):
        return f"{self.user.username} posted a picture\n"
    
    def like(self, other_user):
        super().like(other_user)
    
    def comment(self, other_user, comment):
        super().comment(other_user, comment)

    def display(self):
        try:
            img = mpimg.imread(self.image_path)
            plt.imshow(img)
            plt.axis('off')  # Hide axis
            plt.show()
            print("Shows picture")
        except FileNotFoundError:
            print("Image not found.")
        except Exception as e:
            print("Error displaying image:", e)

class SalePost(Post):
    def __init__(self, user, description, price, pickup_location, availability=True):
        super().__init__(user)
        self.description = description
        self.price = price
        self.pickup_location = pickup_location
        self.availability = availability

    def __str__(self):
        availability_status = "For sale!" if self.availability else "sold!"
        return f"{self.user.username} posted a product for sale:\n{availability_status} {self.description}, price: {self.price}, pickup from: {self.pickup_location}\n"
    
    def like(self, other_user):
        super().like(other_user)
    
    def comment(self, other_user, comment):
        super().comment(other_user, comment)

    def sold(self, password):
        if self.user.password == password and self.user.connected:
            self.availability = False
            print(f"{self.user.username}'s product is sold")
    
    def discount(self, discount_percentage, password):
        if password == self.user.password and self.user.connected:
            self.price *= (1 - discount_percentage / 100)
            print(f"Discount on {self.user.username} product! the new price is: {self.price}")
        else:
            print("Invalid password. Cannot update price.")
    
   