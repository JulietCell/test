salaryTxt = '''
name: Jack   ;    salary:  12000
 name :Mike ; salary:  12300
name: Luk ;   salary:  10030
  name :Tim ;  salary:   9000
name: John ;    salary:  12000
name: Lisa ;    salary:   11000
'''
data0 = salaryTxt.splitlines()      #按行切割，data0列表存储
data0.pop(0)                        #去除首元素
length = len(data0)
names =[]
salaries = []
for i in range(length):             #循环处理data0
    date1 = data0[i].strip().split(";")     #按;切割，data1列表存储
    date2 = date1[0].rstrip().split(":")    #按:切割data1[0]，为了提取人名
    date3 = date1[1].rstrip().split(":")    #按:切割data1[1]，为了提取工资数字
    names.append(date2[1].replace(" ",""))
    salaries.append(date3[1].replace(" ",""))
# print(names)
# print(salaries)                               #提取出人名和工资数字，一一对应关系

def SalaryAndTax(names,salaries):
    length = len(names)
    for i in range(length) :
        tax = int(salaries[i]) * 0.1
        income = int(salaries[i]) - tax
        print(f"name: {names[i]:10};\tsalary: {salaries[i]:10};\ttax: {int(tax):6}\t;\tincome:{int(income):10}")
SalaryAndTax(names,salaries)
