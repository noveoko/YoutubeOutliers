import glob

files = glob.glob("video_lists/**.txt")


with open('not_gurus_titles.txt','w',encoding='utf-8') as outfile:
    files = glob.glob("video_lists/**.txt")
    unique_titles = set()
    for file in files:
        with open(file, 'r',encoding='utf-8') as infile:
            for count, line in enumerate(infile.readlines()):
                if count%2!=0 and 'views' in line:
                    pass
                else:
                    title = " ".join(line.split(";")[1:])
                    unique_titles.add(title)

    for line in unique_titles:
        words = line.split(" ")
        if words[-1] != 'views':
            outfile.write(f"{line.strip()}\n")


with open('fake_gurus_titles.txt','w',encoding='utf-8') as outfile:
    files = glob.glob("fakegurus/**.txt")
    unique_titles = set()
    for file in files:
        with open(file, 'r',encoding='utf-8') as infile:
            for count, line in enumerate(infile.readlines()):
                if line:
                    title = line.split("https://")[0].strip()
                    unique_titles.add(title)
    for title in unique_titles:
        outfile.write(f"{title}\n")