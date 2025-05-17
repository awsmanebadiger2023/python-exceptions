class MyException(Exception):
    def __init__(self, data,value):
        self.data=data
        self.value=value

    def __str__(self):
        return f'Exception occured data is {self.data} and value is {self.value}'

try:
    raise MyException(3,4)
except MyException as e:
    print( e)
    print(e.args)