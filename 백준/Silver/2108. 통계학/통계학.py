import sys
input = sys.stdin.readline
N = int(input())
num_list = []
def arithmetic_mean(num_list):
    sum_value = sum(num_list)
    return round(sum_value / N)

def mid_value(num_list):
    num_list.sort()
    return num_list[len(num_list)//2]

def mode_value(num_list):
    dic = dict()
    for i in num_list:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    mx = max(dic.values())
    mx_dic = []
    for i in dic:
        if mx == dic[i]:
            mx_dic.append(i)
    if len(mx_dic) > 1:
        return(mx_dic[1])
    else:
        return(mx_dic[0])

def bound_value(num_list):
    return max(num_list) - min(num_list)

for i in range(N):
    num_list.append(int(input()))

print(arithmetic_mean(num_list))
print(mid_value(num_list))
print(mode_value(num_list))
print(bound_value(num_list))