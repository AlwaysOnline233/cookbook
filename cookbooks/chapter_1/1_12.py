# 序列中出现次数最多的元素  collections.Counter类   most_common()

from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look',
    'into', 'my', 'eyes', "you're", 'under'
]
word_counts = Counter(words)
# print(word_counts)
top_three = word_counts.most_common(3)  # 出现频率最高的3个单词
print(top_three)
print(word_counts['not'])

print('————————————————————————————')
print('手动增加计数')
morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
for word in morewords:
    word_counts[word] += 1

# word_counts.update(morewords)   # update()更新 增加计数
print(word_counts['not'])

print('————————————————————————————')
print('Counter实例可以跟数学运算操作相结合')
a = Counter(words)
b = Counter(morewords)
c = a + b
d = a - b
print(a)
print(b)
print(c)
print(d)