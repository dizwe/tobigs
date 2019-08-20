f_r = open("phone_book.txt","r")
f_w = open("new_phone_book.txt","w")
while True:
    line = f_r.readline().rstrip('\n') # 뒤에 \n 삭제하기
    if not line : break
    number_chunks = line.split('-')
    if number_chunks[0] == "010" and int(number_chunks[1])>int(number_chunks[2]): 
        f_w.write(''.join(number_chunks)+'\n')
    else:
        continue

f_r.close()
f_w.close()