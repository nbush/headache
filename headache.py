"""

python -> CSS monospace font obfuscator

by n.bush

"""
import string
import random


def mess_maker(size=6, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def headache(text):
    charlist = list(text)
    obfuscated = []
    class_a = mess_maker(10)
    class_b = mess_maker(10)
    css =   """
            <style>
            span.%s {}
            span.%s {color: transparent; letter-spacing:-1em;}
            </style>
            """ % (class_a, class_b)
    obfuscated.append(css)
    for i in charlist:
        mess = mess_maker(10)
        span = '<span class="%s">%s</span><span class="%s">%s</span>' % (class_a, i, class_b, mess)
        obfuscated.append(span)
    return ''.join(obfuscated)


print headache("Hi. This is copyable. Not.")
