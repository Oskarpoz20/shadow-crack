import sys, os, nmap
### CONFIG ###
nmap_ = 8291
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
        scanner = nmap.PortScanner()
        target = input("target: ")
        print("Scanning ports: 1-" + str(nmap_))
        for i in range(1, nmap_ + 1):
            res = scanner.scan(target, str(i))
            res = res["scan"][target]["tcp"][i]["state"]
            if res == "open":
                print(f"{i} is open.")
