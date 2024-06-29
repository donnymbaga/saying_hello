

def say_hello(user_name):
  """
    This function accept user_name and returns 
       `Hello, {user_name},  nice to meet you!"

    if argument is absent, return this otherwise
       `Hello World, you're welcome!"

    Example
    >>> say_hello("Doni Mbaga")
    >>> Hello, Doni Mbaga, nice to meet you!
    >>> say_hello()
    >>> Hello World, nice to meet you!
  """
  message = "Hello, " + user_name + ", " + "nice to meet you!"
  return message

print(say_hello())
print(say_hello("Doni"))
print(say_hello("Doni", "Mbaga"))
