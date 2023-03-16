import re

def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub(r"[^a-z0-9_.-]","",new_id)
    new_id = ".".join([s for s in new_id.split(".") if s != ""])
    new_id = new_id.strip(".")
    if new_id == "":
        new_id = "a"
    if len(new_id) >= 16:
        new_id = new_id[:15].strip(".")
    elif len(new_id) <= 2:
        new_id = new_id + new_id[-1] * 3
        new_id = new_id[:3]

    return new_id