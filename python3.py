s = input("Input a letter of the alphabet: ")

if s in ('a', 'e', 'i', 'o', 'u'):
	print("%s is a vowel." % s)
elif s == 'y':
	print("Sometimes letter y stand for vowel, sometimes stand for consonant.")
else:
	print("%s is a consonant." % s) 
	
