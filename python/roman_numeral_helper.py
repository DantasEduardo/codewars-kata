class RomanNumerals:

    def to_roman(val):
        digit = ['M', 'CM', 'D', 'C', 'XC', 'L', 'X', 'V', 'IV', 'I']
        num = [1000, 900, 500, 100, 90, 50, 10, 5, 4, 1]

        roman = ''        
        indice = 0
        while val >0:
            if val >= num[indice]:
                val -= num[indice]
                roman+= digit[indice]
            else: 
                indice += 1

        return roman

    def from_roman(roman_num):
        if roman_num == 0:
            return 1

        digit = ['M', 'CM', 'D', 'C', 'XC', 'L', 'X', 'V', 'IV', 'I']
        num = [1000, 900, 500, 100, 90, 50, 10, 5, 4, 1]

        total = 0
        array = []

        for i in range(0, len(roman_num)-1):
            if roman_num[i]+ roman_num[i+1] == 'CM' or roman_num[i]+ roman_num[i+1] == 'XC' or roman_num[i]+ roman_num[i+1] == 'IV':
                array.append(roman_num[i] + roman_num[i+1])
            else:
                array.append(roman_num[i])
        
        if len(roman_num) > 2:        
            array.append(roman_num[-1])

        for i in array:
            total += num[digit.index(i)]
    
        return total


print(RomanNumerals.to_roman(1000) == 'M')
print(RomanNumerals.to_roman(4) == 'IV')
print(RomanNumerals.to_roman(1) == 'I')
print(RomanNumerals.to_roman(1990) == 'MCMXC')
print(RomanNumerals.to_roman(2008) == 'MMVIII')
# print(RomanNumerals.from_roman('XXI') == 21)
# print(RomanNumerals.from_roman('I') == 1)
# print(RomanNumerals.from_roman('IV') == 4)
# print(RomanNumerals.from_roman('MMVIII')  == 2008)
# print(RomanNumerals.from_roman('MDCLXVI')  == 1666)