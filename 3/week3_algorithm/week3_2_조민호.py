m = int(input()) # 층
n = int(input()) # 호수

def get_sleep_num(m,n):
    if(m==0):
        return n
    else:
        sleep_num = 0
        for room_idx in range(1,n+1):
            sleep_num += get_sleep_num(m-1,room_idx) 
        return sleep_num

print(get_sleep_num(m,n))
        

    
