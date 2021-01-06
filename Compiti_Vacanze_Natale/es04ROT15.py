def rot15(s):
    cript = ""

    for v in range(len(s)):
        if (ord(s[v]) >= ord('a') and ord(s[v]) <= ord('z')):
            if ord(s[v])+15 > ord('z'):
                cript += chr(96+(ord(s[v])+15-ord('z')))
            else:
                cript += chr(ord(s[v])+15)
        else:
            if (ord(s[v]) >= ord('A') and ord(s[v]) <= ord('Z')):
                if ord(s[v])+15 > ord('Z'):
                    cript += chr(64+(ord(s[v])+15-ord('Z')))
                else:
                    cript += chr(ord(s[v])+15)

   
    return cript

def decriptROT15(s):
    cript=""
    for v in range(len(s)):
        if (ord(s[v]) >= ord('a') and ord(s[v]) <= ord('z')):
            if(ord(s[v])-15 < ord('a')):
                cript += chr(123-(ord('a')-(ord(s[v])-15)))
            else:
                cript += chr(ord(s[v])-15)
        else:
            if (ord(s[v]) >= ord('A') and ord(s[v]) <= ord('Z')):
                if ord(s[v])-15 < ord('A'):
                    cript += chr(91-(ord('A')-(ord(s[v])-15)))
                else:
                    cript += chr(ord(s[v])-15)
    
    
    return cript



