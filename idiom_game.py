import random
import copy

all_idiom = []
rand_all_idiom = []
memory = set()  # 记忆集合，用于判断成语是否被重复使用

def readall():
    global all_idiom, rand_all_idiom
    with open('idiom.txt', 'r') as f:
        all_idiom = f.readlines()
    rand_all_idiom = copy.deepcopy(all_idiom)
 
def idiom_exists(x):
    """判断是否为成语的函数，参数为字符串，判断该字符串是否在成语库中"""
    x = x.strip()
    for i in set(all_idiom):
        if x == i.strip():
            return True
    return False

 
def idiom_test(idiom1, idiom2):
    """判断两个成语是否达成接龙条件"""
    idiom1 = idiom1.strip()
    idiom2 = idiom2.strip()
    if idiom2[0] != idiom1[-1] or len(idiom2) < 4:
        return False
    return True
 
def idiom_select(x):
    """核心代码部分，参数x为成语，返回该成语的接龙匹配成语"""
    if not x:
        i = random.choice(all_idiom)
        i = i.strip()
        return i
    else:
        random.shuffle(rand_all_idiom)
        x = x.strip()
        for i in rand_all_idiom:
            i = i.strip()
            if i[0] != x[-1] or len(i) < 4:
                continue
            return i
        return None

# def player_answer(t):
#     cycle_flag = 0
#     while True:
#         p = input("玩家接龙:")#玩家回答
#         p = p.strip()
#         if p == '' or cycle_flag>5:
#             p = ''
#             break
#         cycle_flag += 1#玩家有5次猜成语机会
#
#         if idiom_exists(p) == False:
#             print("该成语不存在")
#             continue
#         if p in memory:
#             print("该成语已被使用过")
#             continue
#         if idiom_test(t, p) == False:
#             print("回答错误！")
#             continue
#         break
#     return p

def pc_answer(t):
    cycle_flag = 0
    while True:  # 玩家答不上，电脑尝试思考答案
        p = idiom_select(t)

        cycle_flag += 1
        if p not in memory:
            break
        if cycle_flag > 5:
            p = ''
            break
    return p

# def player_question():
#     cycle_flag = 0
#     while True:
#         t = input("轮到玩家出题:")
#         t = t.strip()
#         if t == '' or cycle_flag>5:
#             print("玩家放弃出题！")
#             t = ''
#             break
#
#         cycle_flag += 1
#         if t in memory:
#             print("该成语已被使用过")
#             continue
#         break
#     if t:
#         memory.add(t)
#     return t

def pc_question():
    while True:
        t = idiom_select(None)
        if not t in memory:
            break
    if t:
        memory.add(t)
    return t



# def idiom_start():
#     # 电脑先手
#     t = idiom_select(None)
#     print("电脑出题:",t)
#     memory.add(t)
#
#     while True:
#         p = player_answer(t)
#
#         if not p:
#             p = pc_answer(t)
#             if not p:# 电脑没想出来
#                 print("这一轮大家都没接上")
#                 t = pc_question()# 电脑出题
#             else:# 电脑给出答案
#                 print("电脑接龙:", p)
#                 memory.add(p)
#                 t = p
#         else:
#             memory.add(p)
#
#             t = pc_answer(p)
#             if not t:# 电脑没想出来
#                 print("电脑没接上，你赢了！")
#                 t = pc_question()# 电脑出题
#             else:# 电脑给出答案
#                 print("电脑接龙:", t)
#                 memory.add(t)

