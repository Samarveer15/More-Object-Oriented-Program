class Employee:

    def __init__(self):
        print('Employee created')

    def __del__(self):
        print("destructer called")

def Create_obj():
        print('making Object...')
        obj = Employee()
        print('function end...')
        return obj
    

print("calling Create_obj() function...")
obj = Create_obj()
print('Program End...')