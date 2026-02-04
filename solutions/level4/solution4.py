secret = """Wklv lv ohyho ilyh ri wkh fkdoohqjh. Dw wklv srlqw, vlpsoh wulfnv duh qr orqjhu hqrxjk dqg Brx pxvw uhoB rq fduhixo dqdoBvlv. SdB dwwhqwlrq wr ohwwhu iuhtxhqflhv dqg frpprq sdwwhuqv lq wkh odqjxdjh. Orqj djr, hyhq Fdhvdu eholhyhg klv phvvdjhv zhuh vdih, exw klvwruB suryhg rwkhuzlvh. Olnh DvwhulA dqg ReholA rxwvpduwlqj wkh Urpdq Hpsluh, Brx mxvw rxwvpduwhg xv eB hlwkhu euxwh iruflqj wr uhfhlyh wkh phvvdjh, ru eB xvlqj iuhtxhqfB dqdoBvlv wr ilqg wkh nhB. Frqjudwv iru ilqglqj wkh vroxwlrq [fd3vdu_vdodg.kwpo]""" .lower()


     

letter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] 
frequency_secret = {} 
 
for i in range(0,len(letter)): 
    amount = secret.count(letter[i]) 
    frequency_secret.update({letter[i]:amount}) 

print(f"amount of the letters in the secret text: {frequency_secret},\n total:{len(secret)}" ) 
result = ""
# h most common e --> key is 3 
for char in secret:
    if 'a' <= char <= 'z':
        result += chr((ord(char) - ord('a') - 3) % 26 + ord('a'))
    else:
        result += char

print(result)
