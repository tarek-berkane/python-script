import os
import sys

def info_script():
   
	print('''this script is creat by t.b
enter one file if you want to extract text from it
enter two files to mix them''')


def mix_files(pathEnFile,pathArFile):

	File_En = open(pathEnFile, "r")
	File_Ar = open(pathArFile, "r")
	File_comb = open("finale.txt", "w")

	try:
		txt1 = File_En.read()
		txt2 = File_Ar.read()

		t = txt1.split('\n')
		t2 = txt2.split('\n')

		for i in range(0, len(t)-1):
			File_comb.write(t[i] + " = " + t2[i] + "\n")



	except e:
		print(e)

	finally:
		File_Ar.close()
		File_En.close()
		File_comb.close()



def extract_words(path_of_file):
	
	file_w = open(path_of_file, 'r')
	text = ''

	try:
		text = file_w.read()

	except e:
		print(e)

	finally:
		file_w.close()
	
	list_of_text = text.split(' ')
	
	new_list = []
	
	for word in list_of_text:
		word_lower = word.lower()

		if  word_lower.isalpha() and len(word_lower) >= 3 and word_lower not in new_list:
			new_list.append(word_lower)
	try:
		finaltext = open('text0001.txt', 'w')
	
		for a in new_list:
			try:
				finaltext.write(a + "\n")
			except Exception as e:
				print(e)
	except ex:
		print(ex)
	finally:
		finaltext.close()


if __name__ == '__main__':

	num_inp = len(sys.argv)


	if num_inp == 1:
		info_script()

	elif num_inp == 2:
		extract_words(sys.argv[1])

	else :
		mix_files(sys.argv[1],sys.argv[2])

