def wish(*users, message='Hi'):
    for n in users:
        print(f"{message} {n}")


wish("Steve", "Jack")
wish("Ben", "Kevin", "Larry", message="Hello")
