# run in bash
'''
export var1="Test Variable"
export var2="Another Test Variable"
'''

import os

print(os.getenv("var1"))
print(os.getenv("var2"))

