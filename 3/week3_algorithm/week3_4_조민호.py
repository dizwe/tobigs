#%%
power = [i**2 for i in range(1,11)]
print(power)

#%%
gugudan = [[f'{i}X{j}='+str(i*j) for j in range(1,10)]for i in range(1,10)]
for row in gugudan:
    print(row)

#%%
gugudan2 = [[f'{i}X{j}='+str(i*j) for j in range(1,10) if i!=j]for i in range(1,10)]
for row in gugudan2:
    print(row)
