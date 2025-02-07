import os
from numpy import dot
from numpy.linalg import norm



def confirm_directory(path):
    if not os.path.isdir(path):
        os.makedirs(path)
    return


def cosine_similarity(a, b):
    return dot(a, b)/(norm(a)*norm(b))