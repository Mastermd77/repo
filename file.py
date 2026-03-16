import shutil
import os
data = "Hello Python\n"
with open("test.txt", "w") as f:
    f.write(data) 
    
    
with open("test.txt", "r") as f:
    print(f.read())

with open("test.txt", "a") as f:
    f.write("Next line\n")
    
    
   

shutil.copy("test.txt", "copy.txt")

if os.path.exists("copy.txt"):
    os.remove("copy.txt")   
    
    
if os.path.exists("test.txt"):
    shutil.move("test.txt", "a/test.txt")