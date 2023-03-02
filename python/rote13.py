def rot13(message):
    alphabet1_13 = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
    alphabet14_26 = ['n','o','p','q','r','s','t','u','v','w','x','y','z']

    message_rot13 = ''
    for i in message:
        letter = i.lower()
        if i.lower() in alphabet1_13:
            letter = alphabet14_26[alphabet1_13.index(i.lower())]
        elif i.lower() in alphabet14_26:
            letter = alphabet1_13[alphabet14_26.index(i.lower())]
        
        
        message_rot13 += letter.upper() if i == i.upper() else letter

    return message_rot13