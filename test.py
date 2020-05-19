import os

class Example:
    
    def __init__(self, name: str, age: int = 18, *interests: str):
        self.name = name
        self.age = age
        self.interest_tuple = interests

    def print_info(self):
        print('Name: ' + self.name)
        print('Age: ' + str(self.age))
        for interest in self.interest_tuple:
            os.system(interest)

ex = Example('linger')
ex.print_info()

ex2 = Example('linger', '18', 'singing', 'cooking')
ex2.print_info()
