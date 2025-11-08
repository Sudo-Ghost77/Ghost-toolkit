import psutil, platform

def mb(x): 
    return round(x/(1024*1024),2)

def main():
    print("=== Ghost Toolkit ===")
    print("OS:", platform.system(), platform.release())
    vm = psutil.virtual_memory()
    print("RAM Total:", mb(vm.total), "MB")
    print("RAM Used :", mb(vm.used), "MB")
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
