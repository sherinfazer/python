def1 do_stuff(input):
m,n= [int(x) for x in input.split(" ")]
print(n-m)
while True:
  try:
    value = raw_input()
    do_stuff(value.rstrip()) 
  except (EOFError):
    break 
