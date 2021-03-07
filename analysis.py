import csv
from collections import Counter
# Use this to publish predictions to Github

testing_data = "kaggle_data/Youtube_Videos_USA.csv"

class_probabilities = "results/class_probability.csv"

# with open(class_probabilities, mode="r", encoding="utf-8") as infile:
#     reader = csv.reader(infile):
#     for line in reader:
#         print(line)

all_channels = []

with open(testing_data, newline='',encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for count, row in enumerate(reader):
        video_title = row['video_title']
        clas = ''
        channel = row['channel']
        all_channels.append({"video_title":video_title, "class":"fake_guru", "channel":channel})




matches = []

with open(class_probabilities, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for count, row in enumerate(reader):
        try:
            if row:
                value = float(row[0])
                if value > 0.99992222:
                    matches.append([count, value])
        except IndexError as ie:
            print(ee)
    print("Total Matches:",len(matches))


potential_fake_gurus = []

for a in matches:
    try:
        potential_fake_gurus.append([all_channels[a[0]],a[1]])
    except Exception as ee:
        print(ee)

#potential_fake_gurus = 

channels = {}

#with open('potential_fake_gurus.txt','w', encoding='utf-8') as outfile:

for guru in potential_fake_gurus:
        #title = guru[0]["video_title"]
    channel = guru[0]["channel"]
    value = guru[1]
    try:
        channels[channel].append(value)
    except KeyError as ke:
        channels[channel] = [value]
    # line = f"{title};{channel};{value}\n"
    # outfile.write(line)


for channel, score in channels.items():
    print(channel, sum(score)/len(score))