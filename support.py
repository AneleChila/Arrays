# Somehelp
# Anele Chila
# 19 April 2016

def welcome():
    print('Welcome to the automated technical support system.')
    print('Please describe your problem.')

def get_input():
    return input().lower()


def main():
    import random
    responses = ['Have you tried it on a different operating system?','Did you reboot it?','What colour is it?' ,'You should consider installing anti-virus software. ','Contact Telkom.' ,'I should get that looked at if I were you.']
    keyword_response_pair = {'crashed' : 'Are the drivers up to date?' , 'blue':'Ah, the blue screen of death. And then what happened?','hacked' : 'You should consider installing anti-virus software.' , 'bluetooth' : 'Have you tried mouthwash?' , 'windows' : 'Ah, I think I see your problem. What version?' , 'apple' : 'You do mean the computer kind?' , 'spam' : 'You should see if your mail client can filter messages.' , 'connection' : 'Contact Telkom.'}

    welcome()    
    query = get_input()
    
    while (not query=='quit'):
        #print(responses[random.randint(1,7)])
        if query in keyword_response_pair:
            print(keyword_response_pair[query])
        else:
            print('Curious, tell me more.')

        query = get_input()    
    
if __name__ =='__main__':
    main()