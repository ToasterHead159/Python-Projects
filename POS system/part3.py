import sys
list1 = [1,2,3,4,5]
print("this message will be displayed on screen.")

original_stdout = sys.stdout
with open("name", "+w") as Out:
    sys.stdout = Out
    for i in list1:
        print(i)
    
sys.stdout = original_stdout

print("This will show on screen")