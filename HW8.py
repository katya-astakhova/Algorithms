import hashlib


def find_sub(str):
    sub = set()
    for i in range(len(str)):
        for j in range(i+1, len(str)+1):
            a = hashlib.sha1(str[i:j].encode('utf-8')).hexdigest()
            sub.add(a)
    return len(sub)-1


print(f"Подстрок {find_sub('aab')}")