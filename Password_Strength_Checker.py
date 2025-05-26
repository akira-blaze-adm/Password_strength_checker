


while True:
    password = input('''    type 'exit' to Exit from Password Strength Checker
                            Enter your password here to test its strength : ''')
    def psc(password):
        lowercase = 'abcdefghijklmnopqrstuvwxyz'
        uppercase = lowercase.upper()
        digit = '0123456789'
        special_char = '~!!@#$%^&*()[]{}'
        result = 5

        if len(password) < 8:
            print('password must be 8 character long')
            result -=1
        if not any(char in lowercase for char in password):
            print('password must contain lowercase')
            result -=1

        if not any(char in uppercase for char in password):
            print('password must contain uppercase')
            result -=1
        if not any(char in digit for char in password):
            print('password must contain digit')
            result -=1
        if not any(char in special_char for char in password):
            print('password must contain special characters')
            result -=1
        
        
        else:
            print("Good, You have written your password well")


        if result == 1:
            print("Very Weak password")
            print("Password Strength Score : ", result)
            print("Don't ever type your answer by yourself, you suck")
        if result == 2:
            print('Weak Password')
            print('Password Strength Score : ', result)
        if result == 3:
            print('Moderate Password')
            print('Password Strength Score : ', result)
        if result == 4:
            print('Strong Password')
            print('Password Strength Score : ', result)
        if result == 5:
            print('Very Strong Password')
            print('Password Strength Score : ', result)
            print('Full Marks')
        else:
            pass

    try:
        if str(password) == 'exit':
            print('Exiting password strength checker')
            break
        else:
            print(psc(password))
            
    except:
        continue