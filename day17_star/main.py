class user:
    def __init__(self,user_id,name):
        self.id = user_id
        self.name = name
        self.followers = 0
        self.following = 0

    def follow(self,other_user):
        other_user.followers+=1
        self.following+=1
        print(f"{self.name} is following {other_user.name}")
        print(f"{self.name} -> Following: {self.following}, Followers: {self.followers}")
        print(f"{other_user.name} -> Following: {other_user.following}, Followers: {other_user.followers}")


user_1 = user("oo1","abhineet")
user_2 = user("oo2","prachi")
user_1.follow(user_2)
# print(user_1.id)
# print(user_1.name)
print(user_2.followers)
print(user_2.following)
print(user_1.following)
print(user_1.followers)
# user1.name = "abhineet"
# user1.id = "001"
# print(user1,user1.name,user1.id)