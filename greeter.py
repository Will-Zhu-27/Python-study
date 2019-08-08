def greet_user(username_list):
    """向列表中的每一位用户问好"""
    for name in username_list:
        msg = "Hello, " + name.title() + "!"
        print(msg)

greet_user(['Yuqiang', 'Linger', 'Holo'])