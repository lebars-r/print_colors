r_ = "\033[31m"
g_ = "\033[32m"
y_ = "\033[33m"
b_ = "\033[34m"
p_ = "\033[35m"
c_ = "\033[36m"

def printr(farg, *args):
    args_list = list(args)
    args_list.insert(0, farg)
    color = "\033[31m"
    if type(args_list[0]) is str:
        args_list[0] = color + args_list[0]
    else:
        args_list.insert(0, color)
    args_list.append("\033[0m")
    print(*args_list)

def printg(farg, *args):
    args_list = list(args)
    args_list.insert(0, farg)
    color = "\033[32m"
    if type(args_list[0]) is str:
        args_list[0] = color + args_list[0]
    else:
        args_list.insert(0, color)
    args_list.append("\033[0m")
    print(*args_list)

def printy(farg, *args):
    args_list = list(args)
    args_list.insert(0, farg)
    color = "\033[33m"
    if type(args_list[0]) is str:
        args_list[0] = color + args_list[0]
    else:
        args_list.insert(0, color)
    args_list.append("\033[0m")
    print(*args_list)

def printb(farg, *args):
    args_list = list(args)
    args_list.insert(0, farg)
    color = "\033[34m"
    if type(args_list[0]) is str:
        args_list[0] = color + args_list[0]
    else:
        args_list.insert(0, color)
    args_list.append("\033[0m")
    print(*args_list)

def printp(farg, *args):
    args_list = list(args)
    args_list.insert(0, farg)
    color = "\033[35m"
    if type(args_list[0]) is str:
        args_list[0] = color + args_list[0]
    else:
        args_list.insert(0, color)
    args_list.append("\033[0m")
    print(*args_list)

def printc(farg, *args):
    args_list = list(args)
    args_list.insert(0, farg)
    color = "\033[36m"
    if type(args_list[0]) is str:
        args_list[0] = color + args_list[0]
    else:
        args_list.insert(0, color)
    args_list.append("\033[0m")
    print(*args_list)
