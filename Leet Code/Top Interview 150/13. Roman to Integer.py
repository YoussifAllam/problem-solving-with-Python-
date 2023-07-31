class Solution:
    def romanToInt(self, s: str) -> int:
     H_Table={
     'I'  : '1',
     'V'  : '5',
     'X'  : '10',
     'L'  : '50',
     'C' : '100',
     'D'  : '500',
     'M'  : '1000',}
     sum = 0

     
     for i in range( 1, len(s)+1 ) : 
      if len(s) > 1:
        if s[i-1] == 'I' and i <len(s):
          if s[i]  == 'V' :
            sum += int(4)
            s = s[:i-1] + "_" + s[i:]

            s = s[:i] + "_" + s[i+1:]
            
          elif s[i] == 'X' :
            sum += int(9)
            s = s[:i-1] + "_" + s[i:]
            s = s[:i] + "_" + s[i+1:]

        if s[i-1] == 'X' and i <len(s):
          if s[i] == 'L' :
            sum += int(40)
            s = s[:i-1] + "_" + s[i:]
            s = s[:i] + "_" + s[i+1:]
            
          elif s[i] == 'C' :
            sum += int(90)
            s = s[:i-1] + "_" + s[i:]
            s = s[:i] + "_" + s[i+1:]

        if s[i-1] == 'C' and i <len(s):
          if s[i] == 'D' :
            sum += int(400)
            s = s[:i-1] + "_" + s[i:]
            s = s[:i] + "_" + s[i+1:]

          elif s[i] == 'M' :
            sum += int(900)
            s = s[:i-1] + "_" + s[i:]
            s = s[:i] + "_" + s[i+1:]

      if s[i-1] in H_Table:
         num = H_Table[s[i-1]]
         sum += int(num)
         


     return sum
    
   
'''
or 
 s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").\
 replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
 
 return sum(map(lambda x: roman_to_integer[x], s))

'''
  

  
   
