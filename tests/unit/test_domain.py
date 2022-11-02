import pytest
import os
from app.domainmodel.post import Post
from app.domainmodel.user import User

class TestPost:
    def test_construction(self):
        post1 = Post(1, "Post1", "FirstPost", 1)
        assert str(post1) == "< Post 1 -- Post1 -- FirstPost >"
    
    def test_eql_posts(self):
        post1 = Post(1, "Post1", "FirstPost", 1)
        post2 = Post(1, "Post1", "FirstPost", 1)
        assert post1 == post2

    def test_title_setter(self):
        post1 = Post(1, "Post1", "FirstPost", 1)
        assert str(post1) == "< Post 1 -- Post1 -- FirstPost >"
        post1.title = "still post 1"
        assert str(post1) == "< Post 1 -- still post 1 -- FirstPost >"
    
    def test_desc_setter(self):
        post1 = Post(1, "Post1", "FirstPost", 1)
        assert str(post1) == "< Post 1 -- Post1 -- FirstPost >"
        post1.description = "Still First Post"
        assert str(post1) == "< Post 1 -- Post1 -- Still First Post >"
    

class TestUser:

    def test_construction(self):
        user1 = User(7231, 'amotys', 'amotys277')
        user2 = User(9137, '  yunwi5  ', 'urrabbit978')

        assert str(user1) == '<User amotys, user id = 7231>'
        assert str(user2) == '<User yunwi5, user id = 9137>'

        # Invalid ID type raises error
        with pytest.raises(ValueError):
            User('invalid id', 'pedri', 'pedri1928')

        # ID less than 0 raises error
        with pytest.raises(ValueError):
            User(-10, 'peri', 'pedri1928')

        # Test user_name is all lowercase
        user3 = User(3829, ' GAVI ', 'gavi1928')
        assert user3.user_name == 'gavi'

        # Invalid user_name type sets user_name to None
        user4 = User(8190, 1259, 'memphis212')
        assert user4.user_name is None

        # Invalid password type set password to None
        user5 = User(6737, 'Memphis', 325)
        assert user5.password is None

        user5 = User(9821, 'Memphis', '')
        assert user5.password is None

        # Password length < 7 sets password to None
        user5 = User(6878, 'memphis', 'mempi')
        assert user5.password is None

        # Password of length 7 sets the password correctly
        user6 = User(2918, 'Memphis', 'mempi12')
        assert user6.password == 'mempi12'

    # User class has getters for each attribute, but no setters.
    def test_attributes(self):
        user1 = User(7231, '  AMOTYS  ', 'amotys277')
        assert user1.user_id == 7231
        assert user1.user_name == 'amotys'
        assert user1.password == 'amotys277'

    def test_attributes_fail(self):
        user1 = User(7231, '  LEOROSE  ', 'LEOROSE277')

        with pytest.raises(AttributeError):
            user1.user_name = 'changed'

        with pytest.raises(AttributeError):
            user1.user_id = 1232

        with pytest.raises(AttributeError):
            user1.password = 'asdfe'
    
    def test_adding_post_to_users(self):
        user1 = User(1, 'jamie', 'passsword')
        user1.add_post(Post(1, "Post1", "FirstPost", 1))
        assert str(user1.posts) == "[< Post 1 -- Post1 -- FirstPost >]"
        user1.add_post(Post(2, "Post2", "secondPost", 1))
        assert str(user1.posts) == "[< Post 1 -- Post1 -- FirstPost >, < Post 1 -- Post2 -- secondPost >]"