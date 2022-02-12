from Ders12_User import User

class Post:
    def __init__(self,pid:int,detail:str,likeCount:int,dislikeCount:int,comments:list,user:User) -> None:
        self.ID = pid
        self.Detail = detail
        self.LikeCount = likeCount
        self.DislikeCount = dislikeCount
        self.Comments = comments
        self.User = user

    def AddComment(self,commentText:str):
        self.Comments.append(commentText)

    def __str__(self) -> str:
        return "Post ID: "+str(self.ID)

    def Print(self):
        print(f"""      Gönderen : {self.User.FullName}
        ----------------------------------------
        Post Details
        ----------------------------------------
        {self.Detail}
        ----------------------------------------
        Comments
        ----------------------------------------
        {self.Comments}
        ----------------------------------------
        Like: {self.LikeCount}  |||   Dislike: {self.DislikeCount}
        """)