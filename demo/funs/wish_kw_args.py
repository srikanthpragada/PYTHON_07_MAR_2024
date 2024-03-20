def wish(message, user):
    print(f"{message} {user}")


wish("Hi", "Larry")  # positional
wish(user="Steve", message="Hi")  # keyword
