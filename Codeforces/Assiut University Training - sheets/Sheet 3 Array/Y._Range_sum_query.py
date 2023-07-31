n ,q =  map(int,input().split())
l = list(map(int,input().split()))

def prefix_sum1( Array ):
  prefix_array = []

  for i in range( len( Array ) ): 
    if i == 0:
      prefix_array .append( Array[i] )
    else:
      prefix_array .append( Array[i] + prefix_array[i-1] )
  return prefix_array 


def query(l,r,prefix_array ):
  if r-1  >= 0  and l-2 >=0:
     return  prefix_array[r-1]  -  prefix_array[l-2] 
  else : 
    return  prefix_array[r-1]

prefix_array = prefix_sum1(l)
for i in range ( q ):
    l , r = map( int , input().split() )
    print(query( l , r , prefix_array ) )