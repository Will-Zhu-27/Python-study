"""
动态添加实例变量是否会影响到其他的类实例变量？  -- 不会
给实例添加方法是否会影响到其他的类实例变量？    -- 不会
"""
class Person:
    hair = 'Black'

    def __init__(self, name='Charlie', age=8):
        self.name = name
        self.age = age

    def say(self, content):
        print(content)

def info(self):
    print("---info function---", self)

if __name__ == '__main__':
    p = Person()
    print(p.name)
    print(p.age)
    p.skills = ['Programming', 'Swimming']
    print(p.skills)
    p.foo = info
    p.foo(p)
    p2 = Person()
    p2.foo(p2)
