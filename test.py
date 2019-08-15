def fun():
    print("function1\n")

def fun(var1):
    print("function2, var1: " + str(var1) + "\n")

def fun(var1, var2):
    print("function3, var1: " + str(var1) + ", var2: " + str(var2) + "\n")

def fun(
        var1, var2, var3,
        var4, var5, var6,):
    function_body

fun()
fun('var1')
fun("var1", 'var2')