# 访问闭包中定义的变量


# 想要扩展函数中的某个闭包，允许它能访问和修改函数的内部变量
# 闭包的内部变量对于外界来讲是完全隐藏的。可以通过编写访问函数并将其作为函数属性绑定到闭包上来实现
def sample():
    n = 0

    def func():          # Closure function
        print('n=', n)

    def get_n():         # Accessor methods for n
        return n

    def set_n(value):
        nonlocal n       # nonlocal 声明可以让编写函数来修改内部变量的值
        n = value

    # Attach as function attributes
    func.get_n = get_n    # 通过函数属性将访问方法绑定到闭包函数上
    func.set_n = set_n
    return func


f = sample()
f()
f.set_n(10)
f()
print(f.get_n())



