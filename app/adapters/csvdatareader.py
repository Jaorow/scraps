"""a data reader"""
from app.domainmodel.post import Post
from app.domainmodel.user import User

import os
import csv
import ast

class TrackCSVReader:

    def __init__(self, albums_csv_file: str, tracks_csv_file: str):
        if type(albums_csv_file) is str:
            self.__albums_csv_file = albums_csv_file
        else:
            raise TypeError('albums_csv_file should be a type of string')

        if type(tracks_csv_file) is str:
            self.__tracks_csv_file = tracks_csv_file
        else:
            raise TypeError('tracks_csv_file should be a type of string')

        # List of unique tracks
        self.__dataset_of_posts = []
        self.__dataset_of_users = []
