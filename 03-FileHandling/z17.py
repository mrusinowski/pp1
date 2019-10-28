import re

txt = 'To be, or not to be, that is the question'
samo = re.findall('[eyuioa]',txt)
for x in samo:
    print(x)