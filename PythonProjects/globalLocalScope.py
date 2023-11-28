def spam():
    eggs = 'Hello' #local to spam
    print(eggs)

eggs = 42
spam()
print(eggs) #global eggs variable


# ----------------------------------

def spam2():
    global eggs #global variable replacement possible
    eggs = 'Hello 2' # Local variable also replaces global variable
    print(eggs)

spam2()
print(eggs) #global rewritten
