import operator
import json
words = []
ops = { "+": operator.add,
        "-": operator.sub,
        "*": operator.mul}
def checknumber(a):
    try:
        a = int(a)
        assert type(a) == int
        return type(a) == int
    except:
        return False


def checkoperator(b):
    operators = ['+','-','*']
    assert b in operators
    return b in operators


# print(checknumber(words[2]))
# print(checknumber(words[0]))
# print(checkoperator(words[1]))
def solver(words):
    if (checknumber(words[0]) and checknumber(words[2]) and checkoperator(words[1])):
        print(ops[words[1]](int(words[0]),int(words[2])))
        return ops[words[1]](int(words[0]),int(words[2]))
    else:
        print("please check your syntax.e.g. 3+5")
        return None
# for i in operators:
#     if i in input_exp:
#         sl = input_exp.split(i)
#     else:
#         print("Provide the expression in right way.")
def lambda_handler(event,context):
    print(event)
    input_exp = event['exp']
    stripped = input_exp.replace(" ","")
    for i in stripped:
        words.append(i)
    return solver(words)

