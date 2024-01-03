class User:
    def __init__(self, username, email, password):
        self.__username = username
        self.__email = email
        self.__password = password
        self.__posts = []
        self.__role = "Regular User"

    def create_post(self, content):
        new_post = Post(content, self)
        self.__posts.append(new_post)
        return new_post

    def like_post(self, post):
        post.add_like(self)

    def get_posts(self):
        return self.__posts

    def get_username(self):
        return self.__username

    def get_email(self):
        return self.__email

    def get_role(self):
        return self.__role

    def display_info(self):
        print(f"Username: {self.__username}, Email: {self.__email}, Role: {self.__role}")


class Admin(User):
    def __init__(self, username, email, password):
        super().__init__(username, email, password)
        self.__admin_actions = []

    def promote_to_admin(self, user):
        user.__role = "Admin"
        admin_action = f"{self.get_username()} promoted {user.get_username()} to Admin."
        self.__admin_actions.append(admin_action)
        return admin_action

    def get_admin_actions(self):
        return self.__admin_actions

    def display_info(self):
        print(f"Username: {self.get_username()}, Email: {self.get_email()}, Role: {self.get_role()}")


class Post:
    def __init__(self, content, author):
        self.__content = content
        self.__author = author
        self.__likes = []

    def add_like(self, user):
        self.__likes.append(user)

    def get_likes(self):
        return self.__likes

    def display_info(self):
        print(f"Author: {self.__author.get_username()}, Content: {self.__content}")


# Example usage:

# Create regular user and admin instances
regular_user = User("Azlan", "azlan@example.com", "password123")
admin_user = Admin("AdminUser", "admin@example.com", "adminpassword")

# Regular user creates a post
user_post = regular_user.create_post("Hello, social media world!")

# Admin promotes regular user to admin
admin_user.promote_to_admin(regular_user)

# Admin likes the user's post
admin_user.like_post(user_post)

# Display user and admin information
regular_user.display_info()
admin_user.display_info()

# Display user's posts and likes on the post
user_posts = regular_user.get_posts()
for post in user_posts:
    post.display_info()
    likes = post.get_likes()
    print(f"Likes: {len(likes)}")

# Display admin actions
admin_actions = admin_user.get_admin_actions()
for action in admin_actions:
    print(action)
