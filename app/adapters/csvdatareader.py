"""a data reader"""
from app.domainmodel.post import Post
from app.domainmodel.user import User

import os
import csv
import ast

def create_post_object(row):
    "create and return a post object from a row"
    p = Post(int(row['post_id']),row['title'],row['description'],int(row['user_id']))
    return p
class DataReader:

    def __init__(self, posts_csv_file: str, users_csv_file: str):
        if type(posts_csv_file) is str:
            self.__posts_csv_file = posts_csv_file
        else:
            raise TypeError('posts_csv_file should be a type of string')

        if type(users_csv_file) is str:
            self.__users_csv_file = users_csv_file
        else:
            raise TypeError('users_csv_file should be a type of string')

        # List of unique tracks
        self.__dataset_of_posts = []
        
    

    def get_posts(self):
        return self.__dataset_of_posts
    

    def read_posts(self) -> dict:
        if not os.path.exists(self.__posts_csv_file):
            print(f"path {self.__posts_csv_file} does not exist!")

        self.__posts_dict = dict()
        # encoding of unicode_escape is required to decode successfully
        with open(self.__posts_csv_file, encoding="unicode_escape") as post_csv:
            reader = csv.DictReader(post_csv)
            for row in reader:

                post_id = int(
                    row['post_id']) if row['post_id'].isdigit() else row['post_id']
                if type(post_id) is not int:
                    print(f'Invalid post_id: {post_id}')
                    print(row)
                    continue
                post = create_post_object(row)
                # add to list here too (dataset of posts)
                # however having a dict will be very helpfull for quicky finding posts by post id
                # but not much else
                if post not in self.__dataset_of_posts:
                    self.__dataset_of_posts.append(post)
                self.__posts_dict[post_id] = self.__posts_dict
        
        return self.__dataset_of_posts


    def read(self):
        posts = self.read_posts()

        return posts

