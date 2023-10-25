def phone_keyboard(n):
    b=""
    n+=4
    for _ in range(n):
        for i in range(1,n):
            b+=f"{i} "
            n+=1
    
        c=""
        for l in range(n-3,n):
            c+=f"{l} "
            n+=1
        k=""
        for o in range(n-3,n):
            k+=f"{o} "
            n+=1
    
        return(f"{b}\n{c}\n{k}")
    

print(phone_keyboard(1))