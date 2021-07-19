def decimal_to_bukiyip(a):
    q=a//3
    r=a%3
    rim=""
    while q!=0:
        rim=str(r)+rim
        r=q%3
        q=q//3
    if q==0:
        rim=str(r)+rim
    
    return rim


def bukiyip_to_decimal(a):
    answer=0
    a=str(a)
    index=len(a)
    for i in range(index):
        digit=a[index-1]
        index-=1
        answer+=(int(digit)*3**i)
    return answer


def bukiyip_add(a,b):
    c= bukiyip_to_decimal(a)
    d =bukiyip_to_decimal(b)
    e= c+d
    return decimal_to_bukiyip(e)

def bukiyip_multiply(a,b):
    c=bukiyip_to_decimal(a)
    d=bukiyip_to_decimal(b)
    e= c*d
    return decimal_to_bukiyip(e)

    
  
  
    
    
    
    
        
        
    
    
    
    
    
    
    
    


        
        
    
        
        