def printf(*sr:object,sep:str=' ') ->None:
    re = __import__("re")
    ast = __import__("ast")
    f = __import__('sys').stdout
    sin_comas =r',(?=[)}\]])'
    if isinstance(ast.literal_eval(str(re.sub(sin_comas,'',str(sr)))),tuple):
        rx = re.sub(r'^\[|\]$|^\(|\)$','',str(sr))
        x = re.sub(r'(, )(?![^(]*\))',sep, rx)
        f.write(x+'\n')
        return
    f.write(str(re.sub(r'^\(|\)$|,\)$','',str(sr)))+'\n')
printf([1,2,3,(1,2)])
printf(*[1,2,3,(1,2)])
printf(*[1,2,3,(1,2)],sep='\n')