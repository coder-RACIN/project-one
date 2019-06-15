#用户输入模拟含数据类型转换
'''
death_age = 80
name = input ("please enter your name:")
age = input ("please enter your age:")
print (name + "you can still live for" + str(death_age - int(age))+ "year")
------------------------------------------------------------------------------ '''
#python条件判断语句
'''really_age = 34
enter_age = int(input("please enter your age-->:"))#官方默认缩进的时候使用四个空格符而不是tab，原因在于不同系统识别不了
if enter_age == really_age:
    print("bingo ,you are right")
else:
    print("oh gad,you are wrong")
	'''
#多重条件判断语句
'''
student_score = int(input("please enter your score:-->:"))
if student_score > 90:
    print("A")
elif student_score >80:
    print("B")
elif student_score >60:
    print("C")
else:
    print("sorry,your out")
-------------------------------------------------------------------------------'''
'''
#判断三个数字那个最大

num1 = int(input("num1:"))
num2 = int(input("num2:"))
num3 = int(input("num3:"))
if num1 > num2:
    if num1 > num3:
        print("max is num1")
    else:
        print("max is num3")
elif num2 > num3:
    print("max is num2")
else:
    print("max is num3")
---------------------------------------------------------------------------------    '''
    
    #切片和索引的用法
'''world1 = "helloworld"
print (world1[5])#索引
print (world1[2:5])#切片
if world1[1] in ['E','e']:#列表数据类型
    print ("true")
else:
    print ("false")------------------------------------------------------------------'''
'''#温度转换程序
temp_except = input("请输入温度：")
if temp_except[-1] in ['F','f']:
    c = (eval(temp_except[0:-1]) - 32) / 1.8  #eval叫评估函数，作用是去除函数的外部单引号和括号
    print("转换后的温度是{:.2f}C".format(c))   #这段作用的是将C只保留小数点后面两位
elif temp_except[-1] in ['C','c']:
    f = eval(temp_except[0:-1]) * 1.8 + 32
    print("转换后的温度是{:.2f}F".format(f))
else:
    print("sorry,your input is error")
    
   -----------------------------------------------------'''
#海龟（turtle)库画蟒蛇图
'''import turtle
turtle.setup(600,400,0,0)
turtle.penup()
turtle.fd(-250)
turtle.pensize(20)
turtle.pencolor(0.5,0.6,0.3)
turtle.pendown()
turtle.seth(-45)
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.done()'''
#daydayup工作日的力量
'''dayup = 1.0 
dayf = 0.01
for i in range(365):
    if i % 7 in [6,0]:
        dayup = dayup*(1-dayf)
    else:
        dayup = dayup*(1+dayf)
print("工作日的力量是：{:.2f}".format(dayup))   '''
#身体BMI指数
'''wight,hight=eval(input("请输入您的体重（kg)和身高（m),以逗号隔开:"))
world,chn="",""
bmi = wight / pow(hight,2)
if bmi < 18.5:
    world,chn="偏瘦","偏瘦"
elif bmi > 18.5 and bmi <=24:
    world,chn="正常","正常"
elif bmi > 24 and bmi <=25:
    world,chn="正常","偏胖"
elif bmi > 25 and bmi <=28:
    world,chn="偏胖","偏胖"
elif bmi > 28 and bmi <30:
    world,chn="偏胖","肥胖"
else:
    world,chn="肥胖","肥胖"
print("您的身体BMI的情况是：\n国际标准-->{:*^30}\n国内标准-->{:*^30}".format(world,chn))'''
#通过蒙特卡蒙算法计算圆周率
'''import random
import time
size_count=1000*1000
num=0.0
start = time.perf_counter()
for i in range(1,size_count+1):
    x=random.random()
    y=random.random()
    dist = pow(x**2+y**2,0.5)
    if dist < 1.0:
        num += 1
pi=4*(num/size_count)
print("圆周率近似值为：{:.2f}\n总共花费时间为：{:.2f}s".format(pi,time.perf_counter()-start))'''
#koch雪花绘制
'''import turtle

def koch(size,n):
  
    if n==0:
        turtle.fd(size)
    else:
        for i in (0,60,-120,60):
            turtle.left(i)
            koch(size/3,n-1)
def main():
    turtle.setup(800,400)
    turtle.penup()
    turtle.goto(-300,-50)
    turtle.pendown()
    turtle.pensize(2)
    level=6
    koch(6000,level)
    turtle.right(60)
    koch(6000,level)
    turtle.right(60)  
    koch(6000,level)
    turtle.right(60)  
    koch(6000,level)   
    turtle.right(60)  
    koch(6000,level)   
    turtle.right(60)
    koch(6000,level)    
    turtle.hideturtle()
main()
turtle.done()'''
#数字计算
#获得数据
'''def get_num():
    num = []
    input_num=input("请输入您要添加的数(回车退出):")
    while input_num != "":
        num.append(eval(input_num))
        input_num=input("请输入您要添加的数(回车退出):")
    return num  
#求数据的平均值
def mean(numbers):
    s=0.0
    for i in numbers:
        s+=i
    return s / len(numbers)
#求中位数
def median(numbers):
    sorted(numbers)
    size = len(numbers)
    if size % 2 == 0 :
        med = (numbers[size//2-1] + numbers[size//2])/2
    else:
        med = numbers[size//2]
    return med
#求方差
def dev(numbers,mean):
    sdev=0.0
    for i in numbers:
        sdev += pow(i-mean,2)
    return pow(sdev / (len(numbers)-1),0.5)
n =  get_num() #主体函数
m =  mean(n)

print("平均值:{},方差:{:.2},中位数:{}.".format(m, dev(n,m),median(n)))'''
#哈姆雷特词频统计
'''def get_text():
    txt = open('E:/hamlet.txt','r').read()
    txt = txt.lower()
    for i in '!"#$%&^*+,-/:;<=>?@[\\]^_{|}~':
        txt = txt.replace(i," ")
    return txt
hamlet = get_text()
words = hamlet.split()
counts = {}
for word in words:
    counts[word] = counts.get(word,0)+1
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count=items[i]
    print("{0:<} {1:>}".format(word,count))'''
#三国演义任务出场次序
'''import jieba
excepts=("将军","却说","二人","荆州","不可","不能","如此","商议","如何","军士", \
"左右","军马","引兵","次日","大喜","天下","东吴", \
"于是","今日","不敢","魏兵","陛下","一人","都督", \
"人马","不知","汉中","只见","众将","后主","蜀兵","上马","大叫", \
"太守","此人","夫人")
tx = open('E:/threeking.txt','r',encoding='gb18030').read()
words=jieba.lcut(tx)
counts={}
for word in words:
    if len(word) == 1:
        continue
    elif word=="诸葛亮" or word=="孔明曰":
        rword="孔明"
    elif word=="关公" or word=="云长":
        rword="关羽"
    elif word=="玄德" or word=="玄德曰" or word=="主公":
        rword="刘备"
    elif word=="孟德" or word =="丞相":
        rword="曹操"
    else:
        rword=word
        counts[rword]=counts.get(rword,0)+1
for word in excepts:
    del counts[word]
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(15):
    word,count = items[i]
    print("{0} {1}".format(word,count))'''
#七段数码管的绘制
'''import turtle,time
def r_gap():
    turtle.penup()
    turtle.fd(5)
def r_pen(draw):
    r_gap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    r_gap()
    turtle.right(90)
def r_run(num):
    r_pen(True) if num in [2,3,4,5,6,8,9] else r_pen(False)
    r_pen(True) if num in [1,3,4,5,6,7,8,9,0] else r_pen(False)
    r_pen(True) if num in [2,3,5,6,8,9,0] else r_pen(False)
    r_pen(True) if num in [2,4,6,8,0] else r_pen(False)
    turtle.left(90)
    r_pen(True) if num in [4,5,6,8,9,0] else r_pen(False)
    r_pen(True) if num in [2,3,5,6,7,8,9,0] else r_pen(False)
    r_pen(True) if num in [1,2,3,4,6,7,8,9,0] else r_pen(False) 
    turtle.right(180)
    turtle.penup()
    turtle.fd(20)
    turtle.pendown()
def r_num(date):
    turtle.pencolor("red")
    for i in date:
        if i == '-':
            turtle.write('年',font=('Arial',18,'normal'))
            turtle.pencolor('green')
            turtle.penup()
            turtle.fd(40)
            turtle.pendown()
        elif i == '=':
            turtle.write('月',font=('Arial',18,'normal'))
            turtle.pencolor('blue')
            turtle.penup()
            turtle.fd(40)
            turtle.pendown()
        elif i == '+':
            turtle.write('日',font=('Arial',18,'normal'))
        else:
            r_run(eval(i))
def main():
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.pencolor("green")
    turtle.fd(-300)
    turtle.pensize(5)
    r_num(time.strftime('%Y-%m=%d+',time.gmtime()))
    turtle.hideturtle()
    turtle.done()
main()'''
#AutoTurtle.py
#定义turlte环境
'''import turtle as t
t.title("自动图形绘制")
t.setup(800,600)
t.pencolor("red")
t.pensize(5)
#readdata
datals=[]
data=open("d:/run.txt",'rt')
for line in data:
    line = line.replace('\n','')
    datals.append(list(map(eval,line.split(','))))
data.close()
for i in range(len(datals)):
    t.pencolor(datals[i][3],datals[i][4],datals[i][5])
    t.fd(datals[i][0])
    if datals[i][1]== 1:
        t.right(datals[i][2])
    else:
        t.left(datals[i][2])
t.close()'''


#词云分析
'''import jieba
import wordcloud
f = open("d:/pythonprogram/新时代中国特色社会主义.txt", "r", encoding="gb18030")
 
t = f.read()
f.close()
ls = jieba.lcut(t)
 
txt = " ".join(ls)
w = wordcloud.WordCloud( \
    width = 1000, height = 700,\
    background_color = "white",
    font_path = "msyh.ttc"    
    )
w.generate(txt)
w.to_file("grwordcloud.png")'''
#os库的操作
import os.path
import os 
print(os.getlogin())
print(os.cpu_count())
os.system("C:\\Windows\\System32\\mspaint.exe D:\\pythonprogram\\grwordcloud.png")




















    
    