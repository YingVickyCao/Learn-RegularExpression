# 从文本中找出连续出现的重复单词

import re

test_str = "the little cat cat in the hat hat."
# the little cat in the hat.
result = re.sub(r'(\w+) \1', r'\1', test_str)
print(result)

'''
思考：
上面的正则在任何情况下是否都能够很好工作？
要不要考虑单词的边界？
反向引用有哪些需要注意的点？
'''