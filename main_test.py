import random
import main


def test_lambda1():

    strval = 'Python Programming'
    ret = main.getalnum(strval)
    print('Your result: ', ret)
    retstr = ''.join(ret)
    # retstr = list(ret)
    print('Your result ', retstr)

    assert retstr == 'PythonProgramming'


def test_lambda2():
    strval = 'Python     Programming C++     '
    ret = main.getalnum(strval)
    # retstr = list(ret)
    retstr = ''.join(ret)
    print('Your result :', retstr)

    assert retstr == 'PythonProgrammingC'
