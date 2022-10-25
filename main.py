def getalnum(strval):
    ##################################################
    # make your code
    ##################################################
    # yield statement


strval = 'Python Programming'
ret = getalnum(strval)
print(ret)  # print generator information
retstr = ''.join(ret)

# retstr = list(ret)
print(retstr)
