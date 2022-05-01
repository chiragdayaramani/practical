import re

f = open('InputProg.c','r')

keywords = ['auto','break','case','char','const','continue','default','do','double','else','enum','extern','float','for','goto','if','int','long','register','return','short','signed','sizeof','static','struct','switch','typedef','union','unsigned','void','volatile','while','string','class','struc','include']

operators = ['++','-','=','*','/','%','--','<=','>=']

built_in_function = ['main()','printf','scanf']

numerals = "^(\d+)$"

symbols = ['_','`','~','!','@','#','$','%','^','&','*','(',')','|','"',':','{','}','[',']','<','>','?','/']

identifiers = "^[a-zA-Z_]+[a-zA-Z0-9_]*"

headers = "([a-zA-Z]+\.[h])"

i = f.read()

count = 0
program =  i.split('\n')

for line in program:
    count = count+1
    print ("Line @",count,"\n",line) 
    tokens = line.split(' ')
    for token in tokens:
        if token in operators:
            print("Operator => ",token)
        elif (re.findall(headers,token)):
            print("Header File => ",token)
        elif token in built_in_function:
            print("Built In Function => ",token)
        elif token in keywords:
            print("Keyword => ",token)
        elif token in symbols:
            print("Symbols => ",token)
        elif (re.findall(numerals,token)):
            print("Numeric Value => ",token)
        elif (re.findall(identifiers, token)):   
            print("identifier => ",token)
    print ("________________________________________________________")

f.close()
