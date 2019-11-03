import re

txt = 'To be, or not to be, that is the question'
samo = re.findall('[eyuioa]',txt)
print(f"Liczba samogłosek w tekście: {len(samo)}")