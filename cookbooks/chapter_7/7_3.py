# 给函数参数增加元信息


# 使用函数参数注解
def add(x: int, y: int) -> int:
    return x + y


print(help(add))
print(add.__annotations__)      # 函数注解只存储在函数的 __annotations__ 属性中