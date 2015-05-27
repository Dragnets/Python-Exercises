import os
from string import digits

def rename_files():
    
    #(1) get file names from a folder
    file_list = os.listdir(r"C:\Users\Raitis\Desktop\Python Exercises\prank") # P.S Chnage this to your dir
    #(2_ for each file, rename filename
    os.chdir(r"C:\Users\Raitis\Desktop\Python Exercises\prank") # P.S Change this to your dir
    for file_name in file_list:
        os.rename(file_name,''.join([i for i in file_name if not i.isdigit()]))
                           
rename_files()
