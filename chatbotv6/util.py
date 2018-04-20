#coding:utf-8
import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
sourceFileName = "test.conv" #定义要分割的文件
questionFileName = "./samples/question"
answerFileName = "./samples/answer"
result = 10000

def cutFile():
    print ("Reading...")
    sourceFileData = open(sourceFileName,'r',encoding='utf-8')
    #ListOfLine = sourceFileData.read().splitlines()#将读取的文件内容按行分割，然后存到一个列表中
    #n = len(ListOfLine)
    #tmp_str="File contains "+str(n)+u"line"
    #print (tmp_str)
    #for line in sourceFileData.readlines():
    
    qfile = open(questionFileName, 'a', encoding='utf-8')
    afile = open(answerFileName, 'a', encoding='utf-8')
    
    for (num,line) in enumerate(sourceFileData):
        line = line.strip()
        tmp_str="Line number is "+str(num)+" content is "+line+ "\n" 
        print(tmp_str)
        if num%3==0:
            if line.find('E')!=-1:
                print("line start with E, continue!")                
            else:
                print("Error, first line is not starting with E")
                tmp_str="Line number is "+str(num)+" content is "+line+ "\n" 
                print(tmp_str)
                break
        elif num%3==1:
            if line.find('M')==0:
                print("Question:  ")
                print(line[2:])
                qline=line[2:]+'\n'
                qfile.write(qline)
            else:
                print("Error, second line is not starting with M")
                tmp_str="Line number is "+str(num)+" content is "+line+ "\n" 
                print(tmp_str)
                break
        elif num%3==2:
            if line.find('M')==0:
                print("Answer:  ")
                print(line[2:])
                aline=line[2:]+'\n'
                afile.write(aline)
            else:
                print("Error, third line is not starting with M")
                tmp_str="Line number is "+str(num)+" content is "+line+ "\n" 
                print(tmp_str)
                break
        else:
            break
        if num==result*3:
            break
        
    sourceFileData.close()
    qfile.close()
    afile.close()
    
cutFile()    
