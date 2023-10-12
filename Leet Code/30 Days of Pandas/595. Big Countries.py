import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    return world.loc[(world['area']>=3000000) | ( world['population']>=25000000)  ,['name','area','population'] ]

    
 
d = {'name': ["Afghanistan", "Albania", "Algeria",'Andorra','Angola' ] ,
     'area' : [652230, 28748, 2381741 ,468 , 1246700 ] ,
     'population' : [25500100   , 2831741    , 37100000   , 78115 , 20609294  ] }   
    

d = pd.DataFrame(d)
#print(d)

print(big_countries(d))