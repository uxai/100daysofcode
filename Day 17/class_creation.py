class User:
    def __init__(self, user_id, username):
    #initialise attributes
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    
    def increase_followers(self, user):
        user.following += 1
        self.followers += 1

user_one = User("001", "uxai")
user_two = User("002", "neueux")

user_one.increase_followers(user_two)

print(user_one.followers)
print(user_two.following)