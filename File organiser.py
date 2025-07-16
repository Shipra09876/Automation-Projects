import os 

# if not os.path.exists("Data"):
#     os.mkdir("Data")

#     for i in range(1,100):
#         os.mkdir(f"Data/day{i+1}")


# with open("Data/day2/info.txt",'r') as file:
#     content=file.read()
#     print(content)

#     # file name
#     filename=file.name
#     print(filename)

#     # os path file
#     filename=os.path.basename("Data/day2/info.txt")
#     print(filename)

    # os.mkdir("Data/day3/info2.txt")

    # path="Data/day3/info2.txt"
    # # os.rmdir(path) # remove the file 
    # # create the file 
    # with open(path,"w") as file:
    #     content="Hey baby this is for u , i love u so much "
    #     file.write(content)

    # file=open(path,"r")
    # content=file.read()
    # print(content)

# for i in range(1,100):
#     os.rename(f"Data/day{i+1}",f"Data/Tut{i+1}")

# folders=os.listdir("Data")
# print(folders)
# for folder in folders:
#     print(folder)

print(os.getcwd())