import os
import random

exts = {None: []}

def shuffle(arr):
    # return random.sample(arr, len(arr))
    # Fisher-Yates shuffle
    newarr = arr[:]
    for i in range(len(newarr) - 1, 0, -1):
        rindex = random.randint(0, i)
        tmp = newarr[rindex]
        newarr[rindex] = newarr[i]
        newarr[i] = tmp
    return newarr

def copy_into(fromfile, tofile):
    with open(fromfile, encoding="latin-1") as f:
        with open(tofile, "w", encoding="latin-1") as g:
            g.write(f.read())

for file in next(os.walk("."))[2]:
    if "." in file:
        _, ext = file.split(".", 1)
        if ext in exts:
            exts[ext].append(file)
        else:
            exts[ext] = [file]
    else:
        exts[None].append(file)

for ext in exts:
    newarr = shuffle(exts[ext])
    print(exts[ext], newarr)
    for i, file in enumerate(exts[ext]):
        copy_into(file, "tmp")
        copy_into(newarr[i], file)
        copy_into("tmp", newarr[i])
    try:
        os.remove("tmp")
    except:
        pass
