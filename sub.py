##### class c code of subnet####


def class_c():
  a = int(
    input(
      "Enter How  much ip's you want on that base we  well give subnet mask &&  CIDR  ??? \n "
    ))

  host = input("Enter Network ID  \n")
  if a == "1":
    print("subnet mask is 255.255.255.252 \nCIDR is / 30")
    print(f"{host}.1\nsubnet mask is 255.255.255.254 \nCIDR is / 31")
  elif a == "2":
    print(
      f"{host}.1 \n{host}.2  \n{host}.3 \nsubnet mask is 255.255.255.252 \nCIDR is / 30"
    )
  elif a > 2 and a < 9:
    print(f"subnet mask is 255.255.255.248 \nCIDR is 29 ")
    for ip in range(1, 9):
      print(f"{host}.{ip}")
    print(f"subnet mask is 255.255.255.248 \nCIDR is 29 ")

  elif a > 8 and a < 17:
    print(f"subnet mask is 255.255.255.240 \nCIDR is 28 ")
    for ip in range(1, 17):
      print(f"{host}.{ip}")
    print(f"subnet mask is 255.255.255.240 \nCIDR is 28 ")
  elif a > 16 and a < 33:
    print(f"subnet mask is 255.255.255.224 \nCIDR is 27 ")
    for ip in range(1, 33):
      print(f"{host}.{ip}")
    print(f"{host}.{ip}")
    print(f"subnet mask is 255.255.255.224 \nCIDR is 27 ")
  elif a > 32 and a < 63:
    print(f"subnet mask is 255.255.255.192 \nCIDR is 26 ")
    for ip in range(1, 65):
      print(f"{host}.{ip}")
    print(f"{host}.{ip}")
    print(f"subnet mask is 255.255.255.192 \nCIDR is 26 ")

  elif a > 64 and a < 127:
    print(f"subnet mask is 255.255.255.128 \nCIDR is 25 ")
    for ip in range(1, 129):
      print(f"{host}.{ip}")
    print(f"{host}.{ip}")
    print(f"subnet mask is 255.255.255.128 \nCIDR is 25 ")
  elif a > 128 and a < 255:

    for ip in range(0, 256):
      print(f"subnet mask is 255.255.255.0 \nCIDR is 24 ")
      print("you are using the entire class_c ip's ")
      print(f"{host}.{ip}")
    print(f"{host}.{ip}")
    print(f"subnet mask is 255.255.255.0 \nCIDR is 24 ")
    print("you are using the entire class_c ip's ")
  else:
    print("invaild iput or invaild formate or ip's  limite exiteded ")


    #########class_b subnet code #############
def class_b():
  a = int(
    input(
      "Enter Who much ip's you want on that base we  well give subnet mask &&  CIDR  ??? \n "
    ))
  host = input("Enter Network ID  \n")

  if a > 255 and a < 513:
    print(f"subnet mask is 255.255.254.0 \nCIDR is 23 ")
    for i in range(1, 3):
      for ip in range(0, 256):
        print(f"{host}.{i}.{ip}")
    print(f"subnet mask is 255.255.254.0 \nCIDR is 23 ")

  elif a > 512 and a < 1025:
    print(f"subnet mask is 255.255.252.0 \nCIDR is 22 ")
    for i in range(4, 9):
      for ip in range(0, 256):
        print(f"{host}.{i}.{ip}")
    print(f"subnet mask is 255.255.252.0 \nCIDR is 22 ")
  elif a > 1024 and a < 2049:
    print(f"subnet mask is 255.255.252.0 \nCIDR is 23 ")
    for i in range(8, 16):
      for ip in range(0, 256):
        print(f"{host}.{i}.{ip}")
    print(f"subnet mask is 255.255.252.0 \nCIDR is 23 ")
  elif a > 2048 and a < 4097:
    print(f"subnet mask is 255.255.248.0 \nCIDR is 22 ")
    for i in range(16, 32):
      for ip in range(0, 256):
        print(f"{host}.{i}.{ip}")
    print(f"subnet mask is 255.255.248.0 \nCIDR is 22 ")
  elif a > 4096 and a < 8193:
    print(f"subnet mask is 255.255.240.0 \nCIDR is 21 ")
    for i in range(32, 64):
      for ip in range(0, 256):
        print(f"{host}.{i}.{ip}")
    print(f"subnet mask is 255.255.240.0 \nCIDR is 21 ")
  elif a > 8192 and a < 16385:
    print(f"subnet mask is 255.255.224.0 \nCIDR is 20 ")
    for i in range(64, 128):
      for ip in range(0, 256):
        print(f"{host}.{i}.{ip}")
    print(f"subnet mask is 255.255.224.0 \nCIDR is 20 ")
  elif a > 16384 and a < 32769:
    print(f"subnet mask is 255.255.192.0 \nCIDR is 19 ")
    for i in range(128, 256):
      for ip in range(0, 256):
        print(f"{host}.{i}.{ip}")
    print(f"subnet mask is 255.255.192.0 \nCIDR is 19 ")
  elif a > 32768 and a < 65537:
    print(f"subnet mask is 255.255.128.0 \nCIDR is 18 ")
    print("You are using the entire class_b Ip's ")
    for i in range(0, 256):
      for ip in range(0, 256):
        print(f"{host}.{i}.{ip}")
    print(f"subnet mask is 255.255.128.0 \nCIDR is 18 ")
    print("You are using the entire class_b Ip's ")

    ####class_a subnet code####


def class_a():
  a = int(
    input(
      "Enter Who much ip's you want on that base we  well give subnet mask &&  CIDR  ??? \n "
    ))

  host = input("Enter Network ID  \n")
  print(f"subnet mask is 255.254.0.0 \nCIDR is 15 ")
  if a > 65536 and a < 131072:
    for i in range(1, 3):
      for ip in range(0, 256):
        for s in range(0, 256):
          print(f"{host}.{i}.{ip}.{s}")
    print(f"subnet mask is 255.254.0.0 \nCIDR is 15 ")

  elif a > 131072 and a < 262144:
    print(f"subnet mask is 255.252.0.0 \nCIDR is 14 ")

    for i in range(2, 5):
      for ip in range(0, 256):
        for s in range(0, 256):
          print(f"{host}.{i}.{ip}.{s}")
    print(f"subnet mask is 255.252.0.0 \nCIDR is 14 ")

  elif a > 262144 and a < 524288:
    print(f"subnet mask is 255.248.0.0 \nCIDR is 13")

    for i in range(4, 9):
      for ip in range(0, 256):
        for s in range(0, 256):
          print(f"{host}.{i}.{ip}.{s}")

    print(f"subnet mask is 255.248.0.0 \nCIDR is 13")

  elif a > 524288 and a < 1048576:
    print(f"subnet mask is 255.240.0.0 \nCIDR is 12 ")

    for i in range(8, 17):
      for ip in range(0, 256):
        for s in range(0, 256):
          print(f"{host}.{i}.{ip}.{s}")
    print(f"subnet mask is 255.240.0.0 \nCIDR is 12 ")
  elif a > 1048576 and a < 2097152:

    print(f"subnet mask is 255.224.0.0 \nCIDR is 11 ")
    for i in range(32, 65):
      for ip in range(0, 256):
        for s in range(0, 256):
          print(f"{host}.{i}.{ip}.{s}")
    print(f"subnet mask is 255.224.0.0 \nCIDR is 11 ")

  elif a > 2097152 and a < 4194304:
    print(f"subnet mask is 255.192.0.0 \nCIDR is 10 ")

    for i in range(64, 129):
      for ip in range(0, 256):
        for s in range(0, 256):
          print(f"{host}.{i}.{ip}.{s}")
    print(f"subnet mask is 255.192.0.0 \nCIDR is 10 ")

  elif a > 4194304 and a < 8388608:
    print(f"subnet mask is 255.128.0.0 \nCIDR is 9 ")
    if a > 65536 and a < 131072:
      for i in range(128, 256):
        for ip in range(0, 256):
          for s in range(0, 256):
            print(f"{host}.{i}.{ip}.{s}")
      print(f"subnet mask is 255.128.0.0 \nCIDR is 9 ")

  elif a > 8388608 and a < 16777216:
    print(f"subnet mask is 255.128.0.0 \nCIDR is 8 ")
    print("You are using the entire class_A Ip's ")
    if a > 65536 and a < 131072:
      for i in range(0, 256):
        for ip in range(0, 256):
          for s in range(0, 256):
            print(f"{host}.{i}.{ip}.{s}")
    print(f"subnet mask is 255.128.0.0 \nCIDR is 8 ")
    print("You are using the entire class_A Ip's ")
  else:
    print("invaild iput or invaild formate or ip's  limite exiteded ")

    #### all classess  done #####
    ##################logo of subnetting##################


print("""
 ____        _     _                _   _   _             
/ ___| _   _| |__ | |__  _ __   ___| |_| |_(_)_ __   __ _ 
\___ \| | | | '_ \| '_ \| '_ \ / _ \ __| __| | '_ \ / _` |
 ___) | |_| | |_) | |_) | | | |  __/ |_| |_| | | | | (_| |
|____/ \__,_|_.__/|_.__/|_| |_|\___|\__|\__|_|_| |_|\__, |
                                                    |___/ 
""")

user = int(
  input(
    " enter which class you want to use \n1.class_a \n2.class_b \n3.class_C \n"
  ))
if user == 1:
  class_a()
elif user == 2:
  class_b()
elif user == 3:
  class_c()

else:
  print(
    "wrong input please  select 1. for class A , 2. for class B , 3. for class C"
  )
  ######   END            ###################
