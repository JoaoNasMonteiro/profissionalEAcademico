

test1 = "LVIII"



def romanToInt(s: str) -> int:
    tokensDict = {
        "I" : 1,
        "II" : 2,
        "III" : 3,
        "IV" : 4,
        "V" : 5,
        "IX" : 9,
        "X" : 10,
        "XL" : 40,
        "L" : 50,
        "XC" : 90,
        "C" : 100,
        "CD" : 400,
        "D" : 500,
        "CM" : 900,
        "M" : 1000
    }


    def tokenize(a: str, d : dict) -> list:
        buf = ""
        tokens = []
        i = 0 

        while i in range(len(a)):
            buf += a[i]


            if (i + 2 in range(len(a))) and (buf + a[i + 1] + a[i + 2] in d):
                buf += a[i + 1] + a[i + 2]
                tokens.append(buf)
                #print("ended because of III")
                #print(f"buf = {buf}, tokens = {tokens}, i = {i}")
                break

            elif i + 1 in range(len(a)) and buf + a[i + 1] in d:
                buf += a[i + 1]
                tokens.append(buf)
                #print("Double letter!")
                #print(f"buf = {buf}, tokens = {tokens}, i = {i}")
                buf = ""
                i += 2
                continue



            tokens.append(buf)
            #print(f"buf = {buf}, tokens = {tokens}, i = {i}")
            buf = "" 
            i += 1


        return tokens


    def evaluate(tokens: list, d: dict) -> int:
        
        value: int = 0
        for t in tokens:
            value += d[t] 

        return value
    

    
    tokens = tokenize(a = s, d = tokensDict)
    return(evaluate(tokens = tokens, d = tokensDict))

romanToInt(s = test1)
