op = ["+","-","*","/"]
solution = []
mini = 0
idx = 0

def Compute(b1, ch, b2):
	return eval(str(b1)+ch+str(b2))

def Diff(bil):
	return abs(24-bil)

def PrintSolution(bil, solution):
	tmp = ""
	for i in range(0, 4):
		if (i <= 2):
			tmp = tmp+str(bil[i])+solution[i]
			print(bil[i],solution[i], end=" ")
		else:
			tmp = tmp + str(bil[3])
			print(bil[3])
	solution.append(str(eval(tmp)))
	print(eval(tmp))

def Solve(bil,solution):
	# solution = []
	bil.sort(reverse = True)
	if (Diff(bil[0]+bil[1]) <= Diff(bil[0]*bil[1])):
		#+ _ _
		solution.append("+")
		curr = bil[0] + bil[1]
		if (curr <= 24):
			solution.append("+")
			for j in range(0, 5):
				if (j <= 3):
					tmp = Compute(bil[2], op[j], bil[3])
				else:
					tmp = Compute(bil[3], op[3], bil[2])
				tmp = curr + tmp
				if (j == 0):
					mini = Diff(tmp)
					idx = j
				elif (Diff(tmp) < mini):
					mini = Diff(tmp)
					idx = j
			if (idx == 4):
				solution.append(op[3])
			else:
				solution.append(op[idx])
			if (idx == 4):
				bil[2], bil[3] = bil[3], bil[2]
			PrintSolution(bil, solution)
		else:
			for j in range(0, 5):
				if (j == 0):
					tmp = bil[2]+bil[3]
				elif (j == 1):
					tmp = bil[2]-bil[3]
				elif (j == 2):
					tmp = bil[3]-bil[2]
				elif (j == 3):
					tmp = bil[2]/bil[3]
				else:
					tmp = bil[3]/bil[2]
				tmp = curr - tmp;
				if (j == 0):
					mini = Diff(tmp)
					idx = j
				elif (Diff(tmp) < mini):
					mini = Diff(tmp)
					idx = j
			solution.append("-")
			if (idx == 0):
				solution.append("-")
			elif (idx == 1 or idx == 2):
				solution.append("+")
			elif (idx == 3 or idx == 4):
				solution.append("/")
			if (idx == 4 or idx == 2):
				bil[2], bil[3] = bil[3], bil[2]
			PrintSolution(bil, solution)
	else:
		#* _ _
		solution.append("*")
		curr = bil[0] * bil[1]
		for j in range(0, 2):
			for i in range(0, 4):
				tmp = Compute(curr, op[i], bil[j+2])
				if (i == 0):
					mini = Diff(tmp)
					idx = i
				elif (Diff(tmp) < mini):
					mini = Diff(tmp)
					idx = i
			solution.append(op[idx])
			if (j == 0):
				curr = Compute(curr, op[idx], bil[2])
				prv = idx
		if (idx == 2 or idx == 3):
			if (prv == 0 or prv == 1):
				print("(", bil[0], solution[0], bil[1], solution[1], bil[2], ")", solution[2], bil[3])
				print(eval("("+str(bil[0])+solution[0]+str(bil[1])+solution[1]+str(bil[2])+")"+solution[2]+str(bil[3])))
				solution.append(str(eval("("+str(bil[0])+solution[0]+str(bil[1])+solution[1]+str(bil[2])+")"+solution[2]+str(bil[3]))))
			else:
				PrintSolution(bil, solution)
		else:
			PrintSolution(bil, solution)

#Langkah-langkah greedy:
#Strategi greedy : Pilih operator yang menghasilkan nilai sedekat mungkin dengan 24
#Langkah optimal disini adalah langkah yang menghasilkan nilai sedekat mungkin dengan 24

#1. Pertama sort empat bilangan tersebut secara descending (b[0] >= b[1] >= b[2] >= b[3])
#2. Selanjutnya kita pilih mana yg lebih optimal antara memilih (b[0] + b[1]) atau (b[0]*b[1])
#3. Apabila di langkah kedua lebih optimal untuk menggunakan '+', maka akan ada beberapa kemungkinan:
#		3.1.1 jumlah b[0]+b[1] <= 24
#			Maka langkah optimal yang harus kita lakukan adalah menambah bilangan ini dengan bilangan hasil operasi 
#			b[2] dan b[3]. Yang mungkin hanya menambah dengan b[2]+b[3], b[2]-b[3], b[2]*b[3], b[2]/b[3] atau b[3]/b[2]
#			Pilih mana yang paling mendekati hasilnya dengan 24
#		3.1.2 jumlah b[0]+b[1] > 24
#			Maka langkah optimal yang harus kita lakukan adalah mengurangi bilangan ini dengan bilangan hasil operasi b[2]
#			dan b[3]. Yang mungkin adalah menguranginya dengan (b[2]+b[3]), (b[2]-b[3]), (b[3]-b[2]), (b[2]/b[3]), dan (b[3]/b[2]). 
#			Pilih mana yang paling mendekati hasilnya dengan 24
#	Apabila di langkah kedua lebih optimal untuk menggunakan '*', maka kita harus mengecek dua operator berikutnya mana yang 
#   paling optimal. Perlu hati-hati dikasus ini adalah ketika kita memakai operator '+' lalu operator '*', maka kita harus memakai
#	kurung