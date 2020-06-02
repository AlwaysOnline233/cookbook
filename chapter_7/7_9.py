# 将单方法的类转换为函数

from urllib.request import urlopen


# 使用闭包来将单个方法的类转换成函数
class UrlTemplate:
    def __init__(self, template):
        self.template = template

    def open(self, **kwargs):
        return urlopen(self.template.format_map(kwargs))  # 根据某个模板方案来获取到URL链接地址


# 函数代替上面的类
def urltemplate(template):
    def opener(**kwargs):
        return urlopen(template.format_map(kwargs))
    return opener


