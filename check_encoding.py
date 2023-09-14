### This code block checks the underlying encoding of a datafile to ensure it's readiness for analysis###
###Inspired by datasets that would not read because they were not UTF-8 encoded###

# try-except to import unicodecsv
try:
    import cchardet as cd
except:
    print("You need to install cchardet before deploying this function")

# identify encoding of the data file; replace FILENAME with actual file path
with open('FILENAME', 'rb') as f:
    result = cd.detect(f.read())
    
# store encoding style and confidence level
encoding = result['encoding']
confidence = result['confidence']

# print encoding analysis results using f-strings
print(f"Encoding:{encoding}"+'\n'+f"Confidence:{confidence}")