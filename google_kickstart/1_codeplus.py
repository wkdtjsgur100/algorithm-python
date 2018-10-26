import re
import datetime

N = ""
tu = []

while N != "END":
    N = input()
    fomt = [""]*3
    fomt[0] = re.findall(r"(\d+)/(\d+)/(\d+)", N)
    fomt[1] = re.findall(r"(\d+)년(\d+)월(\d+)일", N)
    fomt[2] = re.findall(r"(\d+)-(\d+)-(\d+)", N)

    for i in range(3):
        if fomt[i]:
            fomt[i][0] = list(fomt[i][0])
            if len(fomt[i][0][0]) == 2:
                fomt[i][0][0] = "20" + fomt[i][0][0]

            date_list = list(map(int, fomt[i][0]))
            tu.append(( datetime.datetime(date_list[0], date_list[1], date_list[2]), N))

for t in sorted(tu):
    print(t[1])
