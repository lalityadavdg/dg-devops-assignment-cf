import operator
import json
words = []
ops = { "+": operator.add,
        "-": operator.sub, 
        "*": operator.mul}
def checknumber(a):
    try:
        a = int(a)
        return type(a) == int
    except:
        return False


def checkoperator(b):
    operators = ['+','-','*']
    return b in operators
    
def solver(words):
    if (checknumber(words[0]) and checknumber(words[2]) and checkoperator(words[1])):
        print(ops[words[1]](int(words[0]),int(words[2])))
        return ops[words[1]](int(words[0]),int(words[2]))
    else:
        print("please check your syntax.e.g. 3+5")
        return None

def lambda_handler(event,context):
    print("successful working")
    print(event)
    input_exp = event['exp']
    stripped = input_exp.replace(" ","")
    for i in stripped:
        words.append(i)
    return solver(words)
