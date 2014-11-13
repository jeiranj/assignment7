import module1, module2, module3, module4

def main():
    for m in [ module1, module2, module3, module4]:
        m.exec_module()

if __name__ == '__main__':
    main()