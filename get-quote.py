import random

def main():
  print("Keep it logically awesome.")
  print("hey! whats up.")
  
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[0])
  print(quotes[2])
  
  last = 13
  rnd = random.randint(0, last)
  last = len(quotes) - 1 
  print(quotes[rnd])

  if __name__== "__main__":
  main()
