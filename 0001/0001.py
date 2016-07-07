import random,os

#生成随机数
def Activation_Code():  
    code = ''
    for i in range(0,10):
        randnum = random.randint(0,9)
        code += str(randnum)
    code += ' '    
    return code

#保存结果
def result_save():
    result = open("result.txt",'ab')
    result.write(Activation_Code().encode()) #Python3中此处需使用encode方法
    result.close()

for i in range(0,200):
    result_save()
