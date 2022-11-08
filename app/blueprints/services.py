"""use for all services!"""

from app.adapters.repository import AbstractRepository


def get_posts(repo, start_idnex, end_index):
    return repo.get_posts(start_idnex,end_index)
    
