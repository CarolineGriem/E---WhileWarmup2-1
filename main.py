word = input("Enter your password: ")
guesses = 0

while word != 'comet' and word != 'Comet' and guesses < 2: 
  print("try again.")
  guesses = guesses + 1
  word = input("Enter your password: ")

if word != 'Comet' and word != 'comet' and guesses >= 2:
  print("You've been locked out of your account.")

elif word == 'comet' or 'Comet':
  print('Login successful.')
