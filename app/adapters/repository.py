import abc
"""import domainmodel stuff"""



# Static database
repo_instance = None

class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def get_posts(self, start, end ):
        """" gets posts from start index to end index """
        raise NotImplementedError

    @abc.abstractmethod
    def get_all_posts(self):
        """returns all posts"""
        raise NotImplementedError

    @abc.abstractmethod
    def add_post(self, post):
        """adds a post to the memory"""
        raise NotImplementedError

    @abc.abstractmethod
    def add_posts(self,posts):
        """adds posts to memory"""
        raise NotImplementedError