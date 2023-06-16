# def strcount(s):
#     for sym in set(s):
#         counter = 0
#         for subsim in s:
#             if sym == subsim:
#                 counter +=1
#         print(sym, counter)
#
# strcount('abbcccccc')

def strcount(s):
    dct = {}
    for sym in s:
        dct[sym] = dct.get(sym, 0) + 1
    for key, value in dct.items():
        print(key, value)

strcount('aaabcd')
