#coding=utf-8

# python (渣打马拉松大赛)
# 分类： python 2013-08-05 13:08 564人阅读 评论(5) 收藏 举报
# 题目：http://blog.csdn.net/mrpre/article/details/9765979
# 题目就加减，挺简单的，所以没通过后缀表达式解析
# 现在已经写好了 中缀转后缀 表达式的解析算法。比赛结束后再贴出来。
# 此程序:在解释器版本Python 2.7.3 中通过
# 假设1:不知道规则，不知道规则个数，不知道规则单位类型,
# 假设2:不知道计算个数，不知道计算单位类型，不知道加减运算符个数
# 仅加减，无优先级，故无需采用堆栈计算出后缀表达式的方法，来解析算术表达式，采用递归解析即可

# WARNING:
#官方给的题目(input.txt)有问题
#按英美通行的一些格式规则，大于1或小于-1，单位用复数；-1和1之间，用单数。
#但是实际运用中，英语国家习惯是只有等于1或-1时用单数，其余都用复数，
#但在github给出的input文件中，却综合出现。例如出现了 "0.15 yard" 以及"0.9 miles"


#file start

global line #Limit the number of lines

#functiuon used to add/open "input.txt" to list(initialization ) 
def init():
    list_tmp=[]
    split_tmp=split=0
    for line in open("input.txt") :
        if (line!='\n'):
            list_tmp.append(line)
            split_tmp=split_tmp+1
        else:
            split=split_tmp
    return list_tmp,split

#add new rule to dict ,promote the ability to mach
def renew(dic_rule):
    list_tmp=[]
    for i in dic_rule:
        list_tmp.append(i)
    for i in list_tmp:
        dic_rule[i[0:len(i)-1]]=dic_rule[i]
    return dic_rule

#extract rule
def extractrule(list_rule):
    dict_tmp={}
    for i in list_rule:
        number_eql=i.index("=")
        number_unitm=i.index("m\n")
        dict_tmp[i[2:(number_eql-1)]]=i[(number_eql+2):(number_unitm-1)]
    return dict_tmp


#calculator
def calculator(list_quen):
   global line
   line=0
   for i in list_quen:
       if i.find("+")>0 or i.find("-")>0:
           compute(i)
           line=line+1
       else:
           answer=convert(i)
           answer=round(answer,2)
           line=line+1
           fp.write(str(answer)+" m\n") 

             
#convert
def convert(i):
    sp=i.find(" ")
    length=len(i)
    if(i[length-1]==" "or i[length-1]=="\n"): #forma unit
        unit=i[sp+1:length-1]
    else:
        unit=i[sp+1:length]
        
    value=i[0:sp]
    value=value.replace(" ","")#forma value
    value=eval(value)
    
    if unit=="feet" or unit=="inches":
        if unit=="feet":unit="foot"
        if unit=="inches":unit="inch"
    else:
        unit=unit[0:len(unit)-1]
        
    answer=eval(dic_rule[unit])*value
    return answer


#change (recursive function)
def change(st):
    global answer_change
    if(st.count("+ ")>1 and st.count("- ")==0):
        list_tmp=st.split("+ ")
        change(str(list_tmp[0]))
        change(str(list_tmp[1]))
        
    if(st.count("+ ")==0 and st.count("- ")>1):
        list_tmp=st.split("+ ")
        change(str(list_tmp[0]))
        change(str(list_tmp[1]))
        
    if(st.count("+ ")==1 and st.count("- ")==0):
        list_tmp=st.split("+ ")
        answer=convert(list_tmp[0])+convert(list_tmp[1])
        answer_change=answer_change+answer
    if(st.count("- ")==1 and st.count("+ ")==0):
        list_tmp=st.split("- ")
        answer=convert(list_tmp[0])-convert(list_tmp[1])
        answer_change=answer_change+answer
    if(st.count("+ ")==0 and st.count("- ")==0):
        st_tmp=convert(st)
        answer_change=answer_change+st_tmp
    if(st.count("+ ")>0 and st.count("- ")>0):
        list_tmp=st.split("+ ")
        change(str(list_tmp[0]))
        change(str(list_tmp[1]))


#add and substract
def compute(i):
    global answer_change
    global line
    afchange_str=change(i)
    answer_change=round(answer_change,2)#with accuracy of 2 decimal points
    fp.write(str(answer_change)+" m")#output to "output.txt"
    if line<len(list_quen)-1:
        fp.write("\n")                 #Don't add "\n" to last line 
    answer_change=0#reset answer_change ,preparing for next question

#output personal information
def outputinfo():
    fp.write("xxxxxxxxxx@126.com \n\n")


#main
fp=open("output.txt","w")
answer_change=0 #global variability used to conserve the answer

list_main=init()#init
split=list_main[1]
length=len(list_main[0])

list_rule=list_main[0][0:split]#extract information about rule to list
list_quen=list_main[0][split:length]#generate question to list
dic_rule=extractrule(list_rule) #generate rule to dict
dic_rule=renew(dic_rule) #采用模糊匹配(允许结尾字母的出错)

outputinfo()    #output personal info
calculator(list_quen)   #compute
fp.close()  #close output.txt
#file end
#print 
#print "ALL:",list_main
#print "RULE origin:",list_rule
#print "RULE answer:",dic_rule
#print "quen:",list_quen