import sys, os, nmap
### CONFIG ###
nmap = nmap.PortScanner()
##############
os.system("clear")
print("###    ####")
print("#      #")
print("### ## #")
print("  #    #")
print("###    ####")
print("made by Nova Studio")
while True:
    command = input("$ ")
    if command == "clear":
        os.system("clear")
    if command == "exit":
        os.system("clear")
        sys.exit()
    if command == "nmap":
        target = input("target: ")
        print(nmap.scan(target, "21-443"))
