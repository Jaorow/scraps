from app.adapters.csvdatareader import DataReader

import os


dirname = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
posts_file_name = os.path.join(dirname, 'scraps/app/adapters/data/posts.csv')
reader = DataReader(posts_file_name,posts_file_name)

posts_dict = reader.read_posts()

posts = reader.get_posts()
print(len(posts))

