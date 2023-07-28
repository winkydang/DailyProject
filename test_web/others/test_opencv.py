import re

pattern = r'^\d{2}[\u4E00-\u9FA5]{2,8}[A-Za-z]+\d+[A-Za-z]{0,2}$|^\d{2}[\u4E00-\u9FA5]{2,10}\d{0,8}$|^\d{0,2}[A-Za-z]{1,3}[\u4E00-\u9FA5]{2,8}$|^\d{2}[\u4E00-\u9FA5]{2,8}[A-Za-z]{0,2}$|^[\u4E00-\u9FA5]{2,8}\d{1,4}$|^[\u4E00-\u9FA5]{2,8}[A-Za-z]{1,2}$|^\d{1,4}[A-Za-z]{1,6}\d{1,4}$|^\d{0,2}[A-Za-z]{1,3}[\u4E00-\u9FA5]{1,2}[A-Za-z]{1,3}\d{0,3}$|^\d{2}[a-z]+\d[a-z]$|^\d{1,2}[\u4E00-\u9FA5]{2,5}\d{1,2}[\u4E00-\u9FA5]{2,5}$'

text = "23华靖资产MTN001(资产担保)"
matches = re.findall(pattern, text)
print(matches)
