class Solution:
    def intToRoman(self, num: int) -> str:
        n = int(num)
        string_number = str(n)
        
        
        
        if len(string_number) == 1:
            if n == 9 :
                return "IX"
            elif n < 9:
                if n >= 5:
                    return "V"+"I"*(n-5)
                elif n < 4:
                    return "I"*n
                else:
                    return "IV"
                
                
                
        elif len(string_number) == 2:
            if int(string_number[0]) == 9:
                tensdigit = "XC"
            elif int(string_number[0]) < 9:
                if int(string_number[0]) >= 5:
                    tensdigit ="L"+"X"*(int(string_number[0])-5)
                elif int(string_number[0]) < 4:
                    tensdigit = "X"*int(string_number[0])
                else:
                    tensdigit = "XL"
                    
            if int(string_number[1]) == 9 :
                onesdigit = "IX"
            elif int(string_number[1]) < 9:
                if int(string_number[1]) >= 5:
                    onesdigit = "V"+"I"*(int(string_number[1])-5)
                elif int(string_number[1]) < 4:
                    onesdigit = "I"*int(string_number[1])
                else:
                    onesdigit = "IV"
            return tensdigit + onesdigit
            
            
            
        elif len(string_number) == 3:
            if int(string_number[0]) == 9:
                hundredsdigit = "CM"
            elif int(string_number[0]) < 9:
                if int(string_number[0]) >= 5:
                    hundredsdigit ="D"+"C"*(int(string_number[0])-5)
                elif int(string_number[0]) < 4:
                    hundredsdigit = "C"*int(string_number[0])
                else:
                    hundredsdigit = "CD"
                    
            if int(string_number[1]) == 9:
                tensdigit = "XC"
            elif int(string_number[1]) < 9:
                if int(string_number[1]) >= 5:
                    tensdigit ="L"+"X"*(int(string_number[1])-5)
                elif int(string_number[1]) < 4:
                    tensdigit = "X"*int(string_number[1])
                else:
                    tensdigit = "XL"
                    
            if int(string_number[2]) == 9 :
                onesdigit = "IX"
            elif int(string_number[2]) < 9:
                if int(string_number[2]) >= 5:
                    onesdigit = "V"+"I"*(int(string_number[2])-5)
                elif int(string_number[2]) < 4:
                    onesdigit = "I"*int(string_number[2])
                else:
                    onesdigit = "IV"
            return hundredsdigit + tensdigit +onesdigit       
                
            
            
        elif len(string_number) == 4:
            thousandsdigit = "M"*int(string_number[0])
            if int(string_number[1]) == 9:
                hundredsdigit = "CM"
            elif int(string_number[1]) < 9:
                if int(string_number[1]) >= 5:
                    hundredsdigit ="D"+"C"*(int(string_number[1])-5)
                elif int(string_number[1]) < 4:
                    hundredsdigit = "C"*int(string_number[1])
                else:
                    hundredsdigit = "CD"
                    
            if int(string_number[2]) == 9:
                tensdigit = "XC"
            elif int(string_number[2]) < 9:
                if int(string_number[2]) >= 5:
                    tensdigit ="L"+"X"*(int(string_number[2])-5)
                elif int(string_number[2]) < 4:
                    tensdigit = "X"*int(string_number[2])
                else:
                    tensdigit = "XL"
                    
            if int(string_number[3]) == 9 :
                onesdigit = "IX"
            elif int(string_number[3]) < 9:
                if int(string_number[3]) >= 5:
                    onesdigit = "V"+"I"*(int(string_number[3])-5)
                elif int(string_number[3]) < 4:
                    onesdigit = "I"*int(string_number[3])
                else:
                    onesdigit = "IV"
            
            return thousandsdigit + hundredsdigit + tensdigit + onesdigit
                
        
