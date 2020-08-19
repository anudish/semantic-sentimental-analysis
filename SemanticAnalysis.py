import csv, math

NumberOfFiles = 500
countCanada = 0
countUniversity = 0
countDal = 0
countHalifax = 0
countBusiness = 0
documentCanadaCount = 0
documentDalCount = 0
documentHalifaxCount = 0
documentBusinessCount = 0
documentUniversityCount = 0
documentCanadaWord = []

filepath = "APItextfiles\\"

for i in range(500):
    countCanada = 0
    countUniversity = 0
    countDal = 0
    countHalifax = 0
    countBusiness = 0

    name = filepath + "newsData_" + str(i) + ".txt"
    with open(name, 'r', encoding='utf-8') as newsData:
        news = newsData.readline()
        newsWords = news.split(" ")
        newsWords = [x.lower() for x in newsWords]
        for word in range(len(newsWords)):
            if(newsWords[word]=='canada'):
                countCanada = countCanada + 1
            if(newsWords[word]=='university'):
                countUniversity = countUniversity + 1
            if(newsWords[word]=='halifax'):
                countHalifax = countHalifax + 1
            if(newsWords[word]=='business'):
                countBusiness = countBusiness + 1
            if (word < len(newsWords) and newsWords[word] == 'dalhousie' and newsWords[word + 1] == 'university'):
                countDal = countDal + 1
        if(countCanada>0):
            documentCanadaCount = documentCanadaCount + 1
            detailsOfCanada = str(len(newsWords)) + ","+str(i)+","+str(countCanada)
            documentCanadaWord.append(detailsOfCanada)
        if(countBusiness>0):
            documentBusinessCount = documentBusinessCount + 1
        if(countDal>0):
            documentDalCount = documentDalCount + 1
        if(countHalifax>0):
            documentHalifaxCount = documentHalifaxCount + 1
        if(countUniversity>0):
            documentUniversityCount = documentUniversityCount + 1

with open('SemanticAnalysis.csv','w') as outputFile:
    writer = csv.writer(outputFile)
    writer.writerow(['Total documents',NumberOfFiles])
    writer.writerow(
        ['Search Query', 'Document Containing Term(df)', 'Total documents(N)/number of  documents  term  appeared (df)',
         'Log10(N/df)'])
    ndfCanada = str(NumberOfFiles) + "/" + str(documentCanadaCount)
    ndfUniversity = str(NumberOfFiles) + "/" + str(documentUniversityCount)
    ndfHalifax = str(NumberOfFiles) + "/" + str(documentHalifaxCount)
    ndfDal = str(NumberOfFiles) + "/" + str(documentDalCount)
    ndfBusiness = str(NumberOfFiles) + "/"+ str(documentBusinessCount)

    if(documentCanadaCount == 0):
        occurenceCanada = 'infinity'
        writer.writerow(['Canada', documentCanadaCount, ndfCanada, 'log10(infinity)'])
    elif(documentCanadaCount > 0):
        occurenceCanada = NumberOfFiles / documentCanadaCount
        writer.writerow(['Canada', documentCanadaCount, ndfCanada, str(round(math.log10(occurenceCanada), 2))])

    if(documentUniversityCount==0):
        occurenceUniversity ='infinity'
        writer.writerow(['University', documentUniversityCount, ndfUniversity,'log10(infinity)'])

    elif(documentUniversityCount>0):
        occurenceUniversity = NumberOfFiles / documentUniversityCount
        writer.writerow(
            ['University', documentUniversityCount, ndfUniversity, str(round(math.log10(occurenceUniversity),2))])

    if(documentDalCount==0):
        occurenceDal = 'infinity'
        writer.writerow(['Dalhousie University', documentDalCount, ndfDal, 'log10(infinity)' ])
    elif(documentDalCount>0):
        occurenceDal = NumberOfFiles / documentDalCount
        writer.writerow(['Dalhousie University',documentDalCount,ndfDal,str(round(math.log10(occurenceDal),2))])

    if(documentHalifaxCount==0):
        occurenceHalifax = 'infinity'
        writer.writerow(['Halifax', documentHalifaxCount, ndfHalifax, 'log10(infinity)'])

    elif(documentHalifaxCount>0):
        occurenceHalifax = NumberOfFiles / documentHalifaxCount
        writer.writerow(['Halifax', documentHalifaxCount, ndfHalifax, str(round(math.log10(occurenceHalifax), 2))])

    if(documentBusinessCount==0):
        occurenceBusiness = 'infinity'
        writer.writerow(['Business', documentBusinessCount, ndfHalifax, 'logn10(infinity)'])

    elif(documentBusinessCount>0):
        occurenceBusiness = NumberOfFiles / documentBusinessCount
        writer.writerow(['Business', documentBusinessCount, ndfBusiness, str(round(math.log10(occurenceBusiness), 2))])

    maximumFrequency = 0
    articleNumber = ''

with open('SemanticAnalysis2.csv','w') as outputFile:
    writer = csv.writer(outputFile)
    writer.writerow(['Term','Canada'])
    writer.writerow(['Canada appeared in ' + str(documentCanadaCount) + ' documents', 'Total words(m)', 'Frequency(f)'])
    for i in range(documentCanadaCount):
        articleDetails = documentCanadaWord[i].split(",")
        writer.writerow(["Article #"+ articleDetails[1],articleDetails[0],articleDetails[2]])
        relativeFrequency = int(articleDetails[2])/int(articleDetails[0])

        if(relativeFrequency>maximumFrequency):
            maximumFrequency = relativeFrequency
            articleNumber = articleDetails[0]

    articleFileName = filepath+"newsData_"+str(articleNumber)+".txt"
    print(articleFileName)

    with open(articleFileName,'r',encoding="utf-8") as articleData:
        articewithMaximumFrequency = (articleData.readline())
        print(articewithMaximumFrequency)