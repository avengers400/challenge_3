### objects = {“a”:{“b”:{“c”:”d”}}}

##taking every element as input and converting to nested dictionary as above and sending the output as input to dict function

d = {}
num = int(input("Enter the dictionaries: "))
for i in range(num):
     dict_x = input("enter parent dict: ")
     d[dict_x] = {}
     firstkey = input("enter first key : ")
     d[dict_x][firstkey] = {}
     secondkey = input("enter 2nd key: ")
     value = input("enter the value: ")
     d[dict_x][firstkey][secondkey] = value
#
#
# print(d)
def dict(a):
      for id in a:

          for k in a[id]:

              for l in a[id][k]:
                  print(a[id][k][l])

result = dict(d)
