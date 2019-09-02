print('hello, django girls')
if 3>2:
    print('it works!')

if 5>2:
    print('5 is indeed greater than 2')
else:
    print('5 is not greater than 2')

volume = 57
if volume < 20:
    print('it is kinda quiet.')
elif 20 <= volume <  40:
    print('it is nice for background music')
elif 40 <= volume < 80:
    print('perfect, I can hear all the details')
elif 60 <= volume < 80:
    print('nice for parties')
else:
    print('my ears are hurting! :(')
# change the volume if it is too loud or too quiet

#funciones....
def hi():
    print('Hi there!')
    print('How are you?')

hi()

def hi(name):
    if name == 'ola':
        print('Hi ola!')
    elif name == 'sonja':
        print('Hi Sonja!')
    else:
        print('Hi anonymous!')

hi('Jorge')

def hi(name):
    print('hi ' + name + '!')

hi("Rachel")

def hi(name):
    print('Hi ' + name + '!')

#bucles....

girls = ['Rachel', 'Monica', 'Phoebe', 'ola', 'you']
for name in girls:
    hi(name)
    print('next girl')

for i in range(1, 6):
    print(2+i)
    
