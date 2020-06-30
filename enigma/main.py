def enigma_basic():
    # create keys string
    keys = 'abcdefghijklmnopqrstuvwxyz !'
# autogenerate the values string by offsetting original string
    values = keys[-1] + keys[0:-1]
    #print(keys)
    #print(values)
# create two dictionaries
    dict_e = dict(zip(keys,values))
    dict_d = dict(zip(values,keys)) 

#user input message and mode

    message = input('Enter your secret message!')
    mode = input('Crypto mode: (e) encrypt or decrypt as default')

# run encode or decode 
    if mode.lower() == 'e':
        new_msg = ''.join([dict_e[letter] for letter in message.lower()])
    else:
        new_msg = ''.join([dict_d[letter] for letter in message.lower()])    

    return new_msg.capitalize()     


    if __name__ == '__main__':
        enigma_basic()