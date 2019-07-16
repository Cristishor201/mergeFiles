import glob, os, datetime

timestamp = datetime.datetime.now()
result = timestamp.strftime("%Y-%m-%d-%H-%M-%S-%f") + ".txt"

def openFile(file):
    with open(file) as myfile:
        content = myfile.read()
        return content

os.chdir("files")
files = glob.glob("*.txt")

with open("../" + result, "w") as res:
    for file in files:
        content = openFile(file)
        res.write(content + "\n")
