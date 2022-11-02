from app.domainmodel.post import Post


class User:

    def __init__(self, user_id: int, user_name: str, password: str):
        if type(user_id) is not int or user_id < 0:
            raise ValueError("User ID should be a non negative integer.")
        self.__user_id = user_id

        if type(user_name) is str:
            self.__user_name = user_name.lower().strip()
        else:
            self.__user_name = None

        if isinstance(password, str) and len(password) >= 7:
            self.__password = password
        else:
            self.__password = None


        self.__posts: list[Post] = []

    @property
    def user_id(self) -> int:
        return self.__user_id

    @property
    def user_name(self) -> str:
        return self.__user_name

    @property
    def password(self) -> str:
        return self.__password

    @property
    def posts(self) -> list:
        return self.__posts

    def add_post(self, new_post: Post):
        if not isinstance(new_post, Post) or new_post in self.__posts:
            return
        self.__posts.append(new_post)

    def remove_post(self, post: Post):
        if not isinstance(post, Post) or post not in self.__posts:
            return
        self.__posts.remove(post)

    def __repr__(self):
        return f'<User {self.user_name}, user id = {self.user_id}>'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.user_id == other.user_id

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return True
        return self.user_id < other.user_id

    def __hash__(self):
        return hash(self.user_id)
