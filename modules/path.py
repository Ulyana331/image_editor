import os

def search_path(name_file):
    path = __file__.split("\\") 
    for i in range(2):
        del path[-1]
    path = "\\".join(path)
    path = os.path.join(path, name_file)
    return path 
    