# Program 4.10: Program to Demonstrate the Use of Keyword Arguments

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print(f"This parrot wouldn't {action}, if you put {voltage}, volts through it.")
    print(f"Lovely plumage, the {type}")
    print(f"It's {state} !!!")


parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword


#parrot()                     # required argument missing
#parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
#parrot(110, voltage=220)     # duplicate value for the same argument
#parrot(actor='John Cleese')  # unknown keyword argument