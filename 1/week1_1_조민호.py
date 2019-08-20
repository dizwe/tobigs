N, line = int(input()), input()
each_num = line.split() # 자르기
filtered_list = list(filter(lambda x: "9" not in str(x),each_num))

if len(filtered_list)>=N: # N 이라는 index를 접근할 수 없다면
    print(int(filtered_list[N-1])**2)
else:
    print("999999999")
