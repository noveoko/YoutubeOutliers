!head -2 /content/results/class_predictions.csv
!head -2 /content/results/class_probabilities.csv
!head -2 /content/results/class_probability.csv
!head -2 /content/Youtube_Videos_USA.csv

files = glob.glob("/content/results/**.csv")

def get_items(path):
  with open(path,'r',encoding='utf-8') as infile:
    return [a.strip() for a in infile.readlines()]

data = [get_items(a) for a in files]

channels = {}

predictions = data[0]
probs = data[1]
prob = data[2]

with open("/content/Youtube_Videos_USA.csv") as outfile:
  category = []
  reader = csv.DictReader(outfile)
  for count, line in enumerate(reader):
    class_name =  predictions[count]
    #probs = probs[count]
    class_prob =  prob[count]
    #----------------------------------------------------------
    title = line["video_title"]
    #cls = line["class"]
    channel = line["channel"].lower()
    if not channel in channels.keys():
      #add key
      channels[channel] = {"titles":[],"not_guru":[],"fake_guru":[]}
    channels[channel]["titles"].append(title)
    channels[channel][class_name].append(float(class_prob))
    
#print(channels.keys(), len(channels.keys()))

def diff_it(list_of_nums):
  assert type(list_of_nums)
  try:
    return sum(list_of_nums)/10
  except Exception as ee:
    print(ee)
    return 0


threshold = 3

with open('potential_fake_gurus.txt','w',encoding='utf-8') as outfile:
  outfile.write("name;score;class")
  for name, data in channels.items():
    predicted_class = None
    value = 0
    thresh = False
    #titles, not_guru, fake_guru
    class_a = data["not_guru"]
    class_b = data["fake_guru"]
    if class_a:
      if len(class_a) > threshold:
        thresh = True
      prob_a = diff_it(class_a)
    if class_b:
      if len(class_b) > threshold:
        thresh = True
      prob_b = diff_it(class_b)
    if prob_a > prob_b:
      predicted_class = "not_guru"
      value = prob_a
    else:
      predicted_class = "fake_guru"
      value = prob_b
    if predicted_class == 'fake_guru' and value > 0.9 and thresh == True:
      outfile.write(f"{name};{value};{predicted_class}\n")

with open('guru_results.txt','w',encoding='utf-8') as outfile:
  for i in range(0, len(data[0])):
    stuff = []
    for x in range(0,len(data)):
      stuff.append(data[x][i].strip())
    outfile.write(' '.join(stuff)+"\n")

