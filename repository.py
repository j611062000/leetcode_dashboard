import pickle

from models import ProblemSet

def dump(file_path: str, p: ProblemSet):
    with open(file_path, "wb") as f:
        pickle.dump(p, f)

def read(file_path: str) -> ProblemSet:
    with open(file_path, "rb") as f:
        return pickle.load(f)