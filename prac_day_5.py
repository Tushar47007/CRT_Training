user = 's2t5z3'
user_list = list(user)
out_list = []
print(user)
print(user_list)
for i in range(len(user_list)):
    if(user_list[i].isdigit()):
        temp = int(user_list[i])
        if(i>0):
            while(temp>0):
                out_list.append(user_list[i-1])
                temp-=1
        elif(user_list[i].isalpha()):
            break
print(out_list)
out_string = ''
out_string = out_string.join(out_list)  # Corrected line
print(out_string)

#Input and Output
#s2t5z3
#['s', '2', 't', '5', 'z', '3']
#['s', 's', 't', 't', 't', 't', 't', 'z', 'z', 'z']