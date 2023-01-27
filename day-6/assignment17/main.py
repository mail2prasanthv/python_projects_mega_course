#combining 2 lists - zip

contents =["Content 1","Content 2","Content 3"];
filenames=["file1.txt","file2.txt","file3.txt"]

for fileName, content in zip(filenames,contents):
    print(fileName, ":", content)
