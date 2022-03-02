
#Code by Kanento
enter = str(input("Enter the text : ")) 

if enter == str(enter):
  bin = ''.join(format(ord(i), '08b') for i in str(enter))
  print("message encoded : ", str(bin)) 
else:
  print("ERROR.")

#Code by Kanento 