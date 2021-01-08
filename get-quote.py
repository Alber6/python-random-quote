def main():
  print("Keep it not xd logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes)
main()
