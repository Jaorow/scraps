import pytest
import os
from app.domainmodel.post import Post

class TestPost:
    def test_construction(self):
        post1 = Post(1, "Post1", "FirstPost", 1)
        assert str(post1) == "< Post 1 -- Post1 -- FirstPost >"
    
    def test_eql_posts(self):
        post1 = Post(1, "Post1", "FirstPost", 1)
        post2 = Post(1, "Post1", "FirstPost", 1)
        assert post1 == post2
