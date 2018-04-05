import csv

golferList = open('../csv/golfer_names_sorted.csv', 'rU')
data14 = open('../csv/edited/2014_results.csv', 'rU')
data15 = open('../csv/edited/2015_results.csv', 'rU')
data16 = open('../csv/edited/2016_results.csv', 'rU')
data17 = open('../csv/edited/2017_results.csv', 'rU')
data18 = open('../csv/edited/2018_results.csv', 'rU')

def getpoints(line):
    if line[10] == 'CUT' or line[10] == 'WD' or line[10] == 'DQ':
        return 0
    elif int(line[10]) == 1:
        return 100
    elif int(line[10]) == 2:
        return 75
    elif int(line[10]) == 3:
        return 60
    elif int(line[10]) <= 5:
        return 40
    elif int(line[10]) <= 10:
        return 30
    elif int(line[10]) <= 25:
        return 20
    elif int(line[10]) <= 50:
        return 10
    elif int(line[10]) > 50:
        return 5
    else:
        return -10




fileList = [data14,data15,data16,data17,data18]
golferNameReader = csv.reader(golferList, dialect='excel')
golfers = []
for i, line in enumerate(golferNameReader):
    if len(line) > 0:
        golfers.append(line[0])
readerList = []
for file in fileList:
    reader = csv.reader(file, dialect='excel')
    readerList.append(reader)

nocut_results = [[] for i in range(len(golfers))]
cut_results = [[] for i in range(len(golfers))]
header = []

for reader in readerList:
    for i,line in enumerate(reader):
        if i == 0:
            header = line
            header.append('points')
        for i in range(len(golfers)):
            if line[9] == golfers[i]:
                points = getpoints(line)
                line.append(str(points))
                if points >= 0:
                    cut_results[i].append(line)
                if points > 0:
                    nocut_results[i].append(line)

# print(header)
# print(cut_results)

for i in range(len(golfers)):
    if len(nocut_results[i]) >= 11:
        nocut_filename = '../csv/data_nocut/golfers/' + golfers[i].replace(" ", "_").replace(".","")+'.csv'
        cut_filename = '../csv/data_cut/golfers/' + golfers[i].replace(" ", "_").replace(".","")+'.csv'

        with open(cut_filename,'wb') as file:
            wr = csv.writer(file, quoting=csv.QUOTE_ALL)
            wr.writerow(header)
            for line in cut_results[i]:
                wr.writerow(line)


        with open(nocut_filename,'wb') as file:
            wr = csv.writer(file, quoting=csv.QUOTE_ALL)
            wr.writerow(header)
            for line in nocut_results[i]:
                wr.writerow(line)



# for golfer in golfers:
#     golferClean = golfer.strip()
#     print(golferClean)
#     fileName = 'golfer_data/' + golfer.replace(" ", "_")
#     results = []
#     for i,line in enumerate(readerList[0]):
#         print('i')
#         if line[4] == 'Tiger Woods':
#             results.append(line)



    # for reader in readerList:
    #     for i,line in enumerate(reader):
    #         print (i)
    #         if line == golferClean:
    #             print(line)
