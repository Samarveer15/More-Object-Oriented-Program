class IOString():
    def __init__(self):
        self.str1 = ""


    def get_String(self):
        self.str1 = input("Enter String : ")


    def print_String(self):
        print("Result is :", self.str1.upper())

    def print_String2(self):
        print("Result is :", self.str1.lower())


str1 = IOString()


str1.get_String()
str1.print_String()

str1.print_String2()       