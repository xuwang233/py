from itertools import combinations,permutations
'''
s="abcd"
c, res = list(s), []
def dfs(x):
    if x == len(c) - 1:
        res.append(''.join(c))   # 添加排列方案                                                                                                                             
        return
    dic = set()
    for i in range(x, len(c)):
        if c[i] in dic: continue # 重复，因此剪枝
        dic.add(c[i])
        c[i], c[x] = c[x], c[i]  # 交换，将 c[i] 固定在第 x 位
        dfs(x + 1)               # 开启固定第 x + 1 位字符
        c[i], c[x] = c[x], c[i]  # 恢复交换
dfs(0)
'''


s="abc"

def permutations(arr, position, end):
    if position == end:

    else:
        for index in range(position, end):
            arr[index], arr[position] = arr[position], arr[index]
            permutations(arr, position + 1, end)
            arr[index], arr[position] = arr[position], arr[index]


arr = list(s)
permutations(arr, 0, len(arr))
lists = []
for i in list:
    if i not in lists:
        lists.append(i)
return lists