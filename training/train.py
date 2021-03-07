import csv
import random

def prepare_data(class_a,class_b):
    """takes path to class_a and class_b txt files where each row is a single instance"""

    cA = set()
    cB = set()

    assortment = [cA, cB]
    paths = [class_a, class_b]
    names = [a.split('.txt')[0].split("/")[-1] for a in paths]

    print(names, paths)

    for count, path in enumerate(paths):
        with open(path, 'r',encoding='utf-8') as tempfile:
            for i in [a.strip() for a in tempfile.readlines()if a]:
                if count == 0:
                    cA.add(i)
                else:
                    cB.add(i)
            
    package = {"class_A":{"name":names[0], "data":list(cA)}, 
              "class_B":{"name":names[1], "data":list(cB)}}

    return package

def create_csv(classData, path='training_data.csv'):
    """Takes dict with classes outputs CSV file for Ludwig"""

    class_a = classData["class_A"]["data"]
    a_name = classData["class_A"]["name"]
    class_b = classData["class_B"]["data"]
    b_name = classData["class_B"]["name"]

    with open(path, newline='',mode='w',encoding='utf-8') as csvfile:
        fieldnames = ['video_title', 'class']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        index_a = [a for a in range(0, len(class_a))]
        index_b = [a for a in range(0, len(class_b))]
        for i in [index_a, index_b]:
            random.shuffle(i)
        missing = 0
        for count, i in enumerate(index_a):
            try:
                a_item = class_a[i]
                b_item = class_b[index_b[count]]
                writer.writerow({'video_title':a_item,'class':a_name})
                writer.writerow({'video_title':b_item,'class':b_name})
            except Exception as ee:
                missing+=1
        total = len(class_a)+len(class_b) - missing
        print("Example mismatch count: ", missing)
        print(f"CSV created with {total} unique examples")

data = prepare_data('../fake_guru.txt','../not_guru.txt')
create_csv(data)
