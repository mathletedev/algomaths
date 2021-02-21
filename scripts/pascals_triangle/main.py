from increment import increment

if __name__ == "__main__":
  n = int(input("Enter the number of rows you want to retrieve: "))
  for i in range(n):
    print(" " * (n - i - 1) + " ".join([str(e) for e in increment(i)]))