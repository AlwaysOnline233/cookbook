# 可接受任意数量参数的函数    *

import html


# 接受任意数量的位置参数   *
def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))


a = avg(1, 2)
print(a)             # 1.5
b = avg(1, 2, 3, 4)
print(b)             # 2.5


# 接受任意数量的关键字参数  **
def make_element(name, value, **attrs):    # attrs是一个包含所有被传入进来的关键字参数的字典
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
                name=name,
                attrs=attr_str,
                value=html.escape(value))
    return element


# Creates '<item size="large" quantity="6">Albatross</item>'
c = make_element('item', 'Albatross', size='large', quantity=6)
print(c)

# Creates '<p>&lt;spam&gt;</p>'
d = make_element('p', '<spam>')
print(d)


# 同时接受任意数量的位置参数和关键字参数，可以同时使用*和**
def anyargs(*args, **kwargs):
    print(args)          # A tuple
    print(kwargs)        # A dict