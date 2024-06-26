
import sys 

def saying_hello(user_name=None):
  """
    This function accept user_name and returns 
       `Hello, {user_name},  nice to meet you!"

    if argument is absent, return this otherwise
       `Hello World, you're welcome!"

    Example
    >>> saying_hello("Doni Mbaga")
    >>> Hello, Doni Mbaga, nice to meet you!
    >>> saying_hello()
    >>> Hello World, nice to meet you!
  """

  if (user_name==None):
    return "Hello World, nice to meet you!"
  else:
    return "Hello, " + user_name + ", " + "nice to meet you!"

