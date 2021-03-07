with open('potential_fake_gurus.txt','r',encoding='utf-8') as infile:
    names = []
    for name in infile.readlines():
        name, score, clss = name.split(";")
        names.append([score, name,clss])

with open('sorted.md','w',encoding='utf-8') as outfile:
    for n in sorted(names, reverse=True):
        line = f"* {','.join(n[0:2])}\n"
        outfile.write(line)