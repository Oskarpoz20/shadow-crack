def en():
    import sys, os, platform, nmap, time, logging
    from colorama import Fore, init
    init(autoreset=True)
    success = Fore.GREEN
    error = Fore.RED
    info = Fore.BLUE
    nmap_ = 100
    time = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime())
    logging.basicConfig (
        level=logging.DEBUG,
        format="{asctime} {levelname:<8} {message}",
        style = "{",
        filename="logs.txt",
        filemode="w",
    )
    def clear():
        os.system("clear")
    clear()
    print("system: " + platform.system())
    print("platform: " + platform.platform())
    print("version: " + platform.version())
    print("processor: " + platform.processor())
    print("machine: " + platform.machine())
    print("time: " + time)
    print("max ports to scan: " + str(nmap_))
    logging.info("system: " + platform.system())
    logging.info("platform: " + platform.system())
    logging.info("version: " + platform.version())
    logging.info("processor: " + platform.processor())
    logging.info("machine: " + platform.machine())
    logging.info("time: " + time)
    logging.info("max ports to scan: " + str(nmap_))
    input("$ ")
    clear()
    print("###    ####")
    print("#      #")
    print("### ## #")
    print("  #    #")
    print("###    ####")
    print(info + "made by Nova Studio")
    print(info + "version: 1.1")
    print(info + "Obsluga NMAP!")
    print(info + "100+ lini kodu!")
    print("\n")
    while True:
        command = input("$ ")
        if command == "":
            print(error + "Error!")
        if command == "help":
            print("help - help")
            print("clear - clear of screen")
            print("exit - exit from shadow-crack")
            print("ls - list of files")
            print("cd - enter to folder")
            print("md - create new directory")
            print("cf - create new file")
            print("read - read file")
            print("rmdir - remove directory")
            print("nmap - port scanner")
        if command == "clear":
            os.system("clear")
        if command == "exit":
            os.system("clear")
            sys.exit()
        if command == "ls":
            print(os.listdir())
        if command == "cd":
            path = input("path: ")
            os.chdir(path)
        if command == "md":
            name = input("name: ")
            os.mkdir(name)
        if command == "cf":
            name = input("name: ")
            f = open(name, "w")
            f.close()
        if command == "read":
            name = input("name: ")
            f = open(name, "r")
            print(f.read())
            f.close()
        if command == "rmdir":
            name = input("name: ")
            os.rmdir(name)
        if command == "nmap":
            scanner = nmap.PortScanner()
            target = input("target: ")
            print("Scanning ports: 1-" + str(nmap_))
            for i in range(1, nmap_ + 1):
                res = scanner.scan(target, str(i))
                res = res["scan"][target]["tcp"][i]["state"]
                print(f"port {i} is {res}.")
def pl():
    import sys, os, platform, nmap, time, logging
    from colorama import Fore, init
    init(autoreset=True)
    success = Fore.GREEN
    error = Fore.RED
    info = Fore.BLUE
    nmap_ = 100
    time = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime())
    logging.basicConfig (
        level=logging.DEBUG,
        format="{asctime} {levelname:<8} {message}",
        style = "{",
        filename="logs.txt",
        filemode="w",
    )
    def clear():
        os.system("clear")
    clear()
    print("system: " + platform.system())
    print("platforma: " + platform.platform())
    print("wersja: " + platform.version())
    print("procesor: " + platform.processor())
    print("maszyna: " + platform.machine())
    print("czas: " + time)
    print("liczba skanowanych portow: " + "1-" + str(nmap_))
    logging.info("system: " + platform.system())
    logging.info("platform: " + platform.system())
    logging.info("version: " + platform.version())
    logging.info("processor: " + platform.processor())
    logging.info("machine: " + platform.machine())
    logging.info("time: " + time)
    logging.info("max ports to scan: " + str(nmap_))
    input("$ ")
    clear()
    print("###    ####")
    print("#      #")
    print("### ## #")
    print("  #    #")
    print("###    ####")
    print(info + "stworzone przez Nova Studio")
    print(info + "wersja: 1.1")
    print(info + "Obsluga NMAP!")
    print(info + "100+ lini kodu!")
    print("\n")
    while True:
        command = input("$ ")
        if command == "":
            print(error + "Bląd!")
        if command == "help":
            print("help - pomoc")
            print("clear - czyszyci ekran")
            print("exit - wychodzi z shadow-crack'a")
            print("ls - pokazuje liste plikow")
            print("cd - wchodzi do folderu")
            print("md - tworzy folder")
            print("cf - tworzy nowy plik")
            print("read - read file")
            print("rmdir - usuwa folder")
            print("nmap - skaner portow")
        if command == "clear":
            os.system("clear")
        if command == "exit":
            os.system("clear")
            sys.exit()
        if command == "ls":
            print(os.listdir())
        if command == "cd":
            path = input("path: ")
            os.chdir(path)
        if command == "md":
            name = input("name: ")
            os.mkdir(name)
        if command == "cf":
            name = input("name: ")
            f = open(name, "w")
            f.close()
        if command == "read":
            name = input("name: ")
            f = open(name, "r")
            print(f.read())
            f.close()
        if command == "rmdir":
            name = input("name: ")
            os.rmdir(name)
        if command == "nmap":
            scanner = nmap.PortScanner()
            target = input("cel: ")
            print("Skanowane porty: 1-" + str(nmap_))
            for i in range(1, nmap_ + 1):
                res = scanner.scan(target, str(i))
                res = res["scan"][target]["tcp"][i]["state"]
                print(f"port {i} jest {res}.")
import sys
print("Choice language/Wybierz język:")
print("en/pl")
choice = input("$ ")
if choice == "en":
    en()
if choice == "pl":
    pl()
else:
    sys.exit()
