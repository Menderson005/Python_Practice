def solution(N):
    # write your code in Python 3.6
   x = "{0:b}".format(N)
   C = x.count("1")
   F = x.rfind("1",0,len(x)) 
   V = x[0:F]
   S = V.split("1")
   M = max(S)
   if C < 2:
        return 0
   else:
        return(len(M))
