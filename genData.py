
if __name__ == "__main__":
    fileToScrape = input("File to scrape: ")

    events = {}

    fo = open(str(fileToScrape), 'r')
    allDat = fo.readlines()
    fo.close()

    allDatClean = []

    for i in allDat:
        toApp = []
        temp = i.split(" ")
        for j in temp:
            if(j):
                lowered = j.lower()
                toApp.append(lowered)

        allDatClean.append(toApp)

    #for i in allDatClean:    
     #   print(i)

    ev = 0
    thisEvent = []
    for i in allDatClean:
        if(i[0] == 'event'):
            print()
            print()
            print()
            print()
            print("Hello")
            #print(i)
            
            print(thisEvent)
            events.update( {ev : thisEvent} )
            ev += 1
            thisEvent.clear()

        thisEvent.append(i)

    print(events)
