def welcome():
 print("welcome to python")

welcome()    


def my_decorator(func):

 def wrapper():
  print("Before function execution")
  func()
  print("After function execution")
  return wrapper

 @my_decorator

def welcome():
 print("welcome to python")


  