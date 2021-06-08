"""
[Demo]
LeetCode 0850
"""


def count_num(lst):
    """根据[[l1,r1],[l2,r2]]线段列表，计算线段总长度（重合部分只记一次）"""
    if not lst:
        return 0

    lst.sort()

    ans = 0
    s, e = lst[0]
    for i in range(1, len(lst)):
        l, r = lst[i]
        if l > e:
            ans += e - s
            s, e = l, r
        else:
            e = max(e, r)
    ans += (e - s)
    return ans
