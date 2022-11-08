import csv
from pathlib import Path
from datetime import date, datetime
from typing import List

from bisect import bisect, bisect_left, insort_left

from werkzeug.security import generate_password_hash

from app.adapters.repository import AbstractRepository
from app.adapters.csvdatareader import DataReader as reader

from app.domainmodel.post import Post
"""
import domain models
"""



class MemoryRepository(AbstractRepository):
    def __init__(self):
        self.__posts = list()

    def add_post(self,post: Post):
        self.__posts.append(post)
    
    def add_posts(self,posts):
        # TODO: this could be whats not working
        for post in posts:
            self.add_post(post)

    
    def get_posts(self, start_index, end_index):
        return self.__posts[start_index:end_index]

    def get_all_posts(self):
        return self.__posts

    


def load_posts(path, repo):
    posts_csv = str(Path(path) / "posts.csv")
    users_csv = str(Path(path) / "users.csv")
    r = reader(posts_csv,users_csv)
    repo.add_posts(r.read())

def populate(data_path: Path,repo:MemoryRepository):
    load_posts(data_path,repo)