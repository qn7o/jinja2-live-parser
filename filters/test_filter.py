
def litefy(a, **kw):
    '''Make geeky, nerdy readable text'''
    lite = a.replace('a','4')
    lite = lite.replace('e','3')
    lite = lite.replace('i','1')
    lite = lite.replace('o','0')
    return lite.replace('u','^')
