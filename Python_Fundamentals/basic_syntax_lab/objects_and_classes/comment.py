class Comment:
    def __init__(self, username, content, likes=0):  #parameters
        self.username = username   #atributes
        self.content = content     #atributes
        self.likes = likes         #atributes

comment = Comment("user1", "I like this book")
print(comment.username)
print(comment.content)
print(comment.likes)
