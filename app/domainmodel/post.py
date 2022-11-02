from requests import post
from sqlalchemy import desc


class Post:
    """
    POST CLASS 

    TODO: 
    add tags functionalty
    maybe add into user as created?
    
    """
    def __init__(self, post_id:int, Title: str, Description: str, User_id: int) -> None:
        if post_id > 0:
            self.__post_id = post_id
        if User_id > 0:
            self.__user_id = User_id
        if len(Description) > 0:
            self.__description = Description
        if len(Title) > 0: 
            self.__title = Title

    @property
    def post_id(self) -> int:
        return self.__post_id

    @property 
    def title(self) -> str:
        return self.__title
    
    @title.setter
    def title(self, new):
        if len(new.strip()) > 0:
            self.__title = new.strip()
    
    @property
    def description(self):
        return self.__description
    
    @description.setter
    def description(self, new):
        if len(new.strip()):
            self.__description = new
    
    @property
    def user_id(self) -> int:
        return self.__user_id
    
    @user_id.setter
    def user_id(self, new):
        try:
            if int(new) > 0:
                self.__user_id = new
        except:
            pass

    def __repr__(self):
        return f"< Post {self.__post_id} -- {self.__title} -- {self.__description} >"
    
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.post_id == other.post_id

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return True
        return self.post_id < other.post_id

    def __hash__(self):
        return hash(self.__post_id)
