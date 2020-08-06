# Invert a Binary Tree
'''
层序遍历比较简单，使用广度优先搜索即可。‘倒置二叉树’的中序遍历其实就是二叉树的中序遍历倒置输出
'''


def find_root(nodes, now):
    temp = [x for x in nodes if now[0] in x and x != now]
    if len(temp) > 0:
        return find_root(nodes, temp[0])
    else:
        return now[0]


def level(nodes, root):
    step = [root]
    result = []
    while(len(step) >0):
        temp = []
        for x in step:
            if nodes[x][1]!= -1:
                temp.append(nodes[x][1])
            if nodes[x][2]!= -1:
                temp.append(nodes[x][2])
        result += step[::-1]
        step = temp
    print(*result)


def inorder(nodes, root):
    global result
    if nodes[root][1] != -1:
        inorder(nodes, nodes[root][1])
    result.append(root)
    if nodes[root][2] != -1:
        inorder(nodes, nodes[root][2])


if __name__ == "__main__":
    n = int(input())
    nodes = []
    for x in range(n):
        unit = input().split(" ")
        try:
            left = int(unit[0])
        except:
            left = -1
        try:
            right = int(unit[1])
        except:
            right = -1
        nodes.append([x, left, right])
    root = find_root(nodes, nodes[0])
    result = []
    level(nodes, root)
    inorder(nodes, root)
    print(*result[::-1])