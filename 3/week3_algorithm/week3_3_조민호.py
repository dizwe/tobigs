#%%
M, N = input().split() #A영역 합격, B영역 합격

A_pass_list = []
B_pass_list = []
for i in range(int(M)):
    name = input()
    A_pass_list.append(name)

for j in range(int(N)):
    name = input()
    B_pass_list.append(name)

# print(A_pass_list,B_pass_list)

#%%
# 겹치는 값 표현
intersection = list(set(A_pass_list).intersection(set(B_pass_list)))
intersection.sort()

# print(intersection)

def first_to_upper(x):
    # string은 그대로 assignment 안됨
    # # x[1]=x[1].upper()
    # 단어와 단어를 합쳐서 list에 넣기
    lst = [x[0].upper() + x[1:]]
    s = " ".join(lst)

    return s

intersection_names = list(map(first_to_upper, intersection))
print(len(intersection_names))
for i in range(len(intersection_names)):
    print(intersection_names[i])

#%%
