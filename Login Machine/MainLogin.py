# Login System
f=open('Passwords.txt', 'r')
g = ''
f1 = f.readlines()
for x in f1:
    g = str(f1)
    g = g.replace("']", "")
    g = g.replace("['", "")
    g = g.split()
    print(g)
    

def Main(g):
    loggedin = False
## Try change to dictionary instead of list so that there are usernames
    usr = int(input('What is your user number? '))
    log = input('Enter your password: ')
    e = ''
    for i in range(2):
        if log == g[usr]:
            print('you are now logged in!')
            loggedin = True
            while loggedin:
## More functions for when logged in
                do = input('What would you like to do? ').lower()
### Fix (maybe with usr number in list then editing document to be list?)
                if do=='change password':
                    nPsw = input('What is the password for the new account? ')
                    g[usr] = nPsw
                    for g in g:
                        e = e+' '+g
                    print(e)
                    c = open('Passwords.txt', 'w+')
                    c.write(e)
                    c.close()
                elif do=='add user':
                    aPsw = input('What password would you like to add? ')
                    a=open('guru99.txt', 'a+')
                    a.write(f' {aPsw}')
                    a.close()
                    print(f'You have succesfully created user {len(g)+1} with the password {aPsw}')
                elif do=='logout':
                    Main()
                    
        else:
            print('Incorrect password')
            print(f'You have {2-i} more attempts')
        log = input('Enter your password: ')
    print('Go away hacker')
Main(g)

