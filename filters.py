def filter_leetify(a, **kw):
    """Leetify text ('a' becomes '4', 'e' becomes '3', etc.)"""
    return a.replace('a','4').replace('e','3').replace('i','1').replace('o','0').replace('u','^')
