import time
p = 1000 #principle
r = .02 #rate
t = 50 # time in days
x = 1 # counter
np =[] # new principle
g = [] # gain
np.append(p)

def cal(x):
    """
        The function calculates the compunding return given variables
        a = the for compunding daily return
        
    """
        print('fig '+ str(x),)
        a = np[-1]*(1+r)
        print(f'{a:,.2f}','USD')
        print('increase of ' , '$', f'{ a-np[-1]:,.2f}','USD'+ '\n')
        g.append(( a-np[-1]))
        np.append(a)

def get_gain(start=None , end=None):
    """
    The function calaculates the sum returns in a given time period of days
    """
    t_gains =sum(g[start:end])
    print('Total gains for ', end, 'days $',   f'{t_gains:,.2f}','USD')
	
while x < t :
	cal(x)
	x += 1
	
    
get_gain(0,t) 
time.sleep(20)
