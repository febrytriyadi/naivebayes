import csv
import math
datatrain=[]
datatest=[]
yes=">50K";
no="<=50K";


with open('TrainsetTugas1ML.csv', 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for row in reader:
		datatrain.append(row)
datatrain.pop(0);
with open('TestsetTugas1ML.csv', 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for row in reader:
		datatest.append(row)
datatest.pop(0);

def hitung(cell,i,x) :
	return len(list(filter(lambda y: getpcix(y, cell,i,x), datatrain)))/len(list(filter(lambda y: getpc(y, x), datatrain)))
def getpc(x,y):
	return x[8]==y
def getpcix(a,cell,i,x):
	return a[i]==cell[i] and a[8]==x
def countyes(a):
	return a[8]==yes
def getc():
	return len(list(filter(countyes,datatrain)))/len(datatrain)
def prob(cell,x):
	if x==yes :
		jum = getc()
	else :
		jum = 1-getc()
	for i in range(1,len(cell)) :
		jum*=hitung(cell,i,x)
	return jum
def getlabel(cell):
	if (prob(cell,yes) > prob(cell,no)):
		return yes
	else:
		return no

with open('TebakanTugas1ML.csv','w',newline ='\n') as hasil:
	write = csv.writer(hasil,dialect='excel')
	for i in range(0,len(datatest)) : 
		write.writerow([getlabel(datatest[i])])
hasil.close()

