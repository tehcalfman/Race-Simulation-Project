# A class for the runner
class Runner:

    def __init__(self,name,county,iden):
        self.name = name
        self.county = county
        self.iden = iden

    def __str__(self):
        return f"{self.name},{self.county},{self.iden}"

# A class for the results
class Result:
    def __init__(self,iden,time):
        self.iden = iden
        self.time = int(time)

    def minutes(self):
        minute = self.time // 60
        minutes = minute
        return minutes

    def __str__(self):
        return f"{self.iden}   {self.minutes()} min {self.time % 60} sec"


def create_race_list(file):
    # open the file
    openfile = open(file)
    # read said file
    readfile = openfile.read()
    # turn the string of readfile into a list
    templist = readfile.split("\n")
    return templist


def create_runners(file):
    # create a list to be used later
    runnerList = []
    # open the file
    openFile = open(file)
    # read said file
    readfile = openFile.read()
    # create a list of names by splitting the string on the enters
    templist = readfile.split("\n")
    # loop through the list and create a list of Runner classes
    for i in templist:
        # another temporary list
        tempvar = i.split(",")
        name = tempvar[0]
        z = tempvar[1].split("-")
        county = z[0]
        iden = tempvar[1]
        # making a runner of the runner class and adding it to the runner list
        runner = Runner(name,county,iden)
        runnerList.append(runner)
    return runnerList


def create_result(file):
    # a list to be used later
    resultList = []
    # open the file
    openFile = open(file)
    # read the file
    readfile = openFile.read()
    # create a list out of the contents of the file
    templist = readfile.split("\n")
    # loop through the list to create a list of result classes
    for i in templist:
        # if there is an empty line stop looping
        if i == "":
            break
        # a temporary list used for each result
        temporary = i.split(",")
        iden = temporary[0]
        time = temporary[1]
        # create an object of the result class
        result = Result(iden,time)
        # add said object to the list of results
        resultList.append(result)
    return resultList


def create_race():
    # Get the input of the new venue name
    raceVenue = input("Enter the race's venue: ")
    # Open the Races file in append mode
    raceFile = open("Races.txt", "a")
    # write the race venue to the file
    raceFile.write(f"\n{raceVenue}")
    # Create a list of all runners
    runnerList = create_runners("Runners.txt")
    # Create a file for the new race
    file = open(f"{raceVenue.lower()}.txt", "w")
    # Loop through the runner file, adding the runner's time, if the runner didn't attend their time is
    # 0 and their name isn't added
    for i in runnerList:
        print(i.name)
        time = int(input("Enter the runner's time in seconds(0 if they didn't attend): "))
        if time > 0:
            file.write(f"{i.iden},{time}\n")
    # confirm a new race was created
    print("Race Added")


def display_results():
    # Create a list of the races
    races = create_race_list("Races.txt")
    # Create a menu for the races
    for i in range(len(races)):
        print(f"{i + 1}: {races[i]}")
    # Allow the user to choose an option
    option = int(input("Choice > "))
    # Create a list of results for the selected choice
    results = create_result(f"{races[option - 1].lower()}.txt")
    # Print a title
    print(f"Results for {races[option - 1]}")
    print("=" * 20)
    # create variables for the best time and winner
    best_time = 999999999999999999999
    winner = "none"
    # loop through the results
    for i in results:
        # print out the results
        print(i.__str__())
        # if the time beats the current best time then make that the new best time
        if i.time < best_time:
            best_time = i.time
            winner = i.iden
    # print who won the race
    print(f"{winner} won the race")


def list_competitors():
    # create a list of runners
    runners = create_runners("Runners.txt")
    # print a title for the cork runners
    print(f"Cork Runners\n{'-' * len('Cork Runners')}")
    # loop through the runners list and print the name of any runners who's county is Cork
    for i in runners:
        if i.county == "CK":
            print(i.name)
    # print a title for the Kerry runners
    print(f"\nKerry Runners\n{'-'*len('Kerry Runners')}")
    # loop through the runners list and print the name of any runner who's county is Kerry
    for i in runners:
        if i.county == "KY":
            print(i.name)


def determine_winners():
    # crate a list of races
    races = create_race_list("Races.txt")
    # create the UI
    print(f"Venue{' ' * 13}Winner")
    print("=" * 24)
    # loop through the races
    for i in races:
        # create a list of results for the race
        results = create_result(f"{i.lower()}.txt")
        # create variables for winning time and the winner
        winningTime = 9999999999999
        winner = "none"
        # loop through the results comparing the time, if the time is lower than the current winner's time set their
        # time to the winner's time as well as the winner's name
        for x in results:
            if x.time < winningTime:
                winningTime = x.time
                winner = x.iden
        # print out the winner
        print(f"{i}         {winner}")


def competitor_times():
    # create a list of runners
    runners = create_runners("Runners.txt")
    # loop through and create a menu for the runners
    for i in range(len(runners)):
        print(f"{i + 1}. {runners[i].name}")
    # give the user a choice of menu items
    choice = int(input("Choice > "))
    # print the runner's name and id number
    print(f"{runners[choice - 1].name}\t({runners[choice - 1].iden})")
    print("=" * 32)
    # create a list of races
    races = create_race_list("Races.txt")
    # loop through the races
    for i in races:
        # create a list of results for the race
        results = create_result(f"{i.lower()}.txt")
        # create a list of races
        places = []
        # loop through the results and put the times in the places
        for z in results:
            places.append(z.time)
        # sort the list of results
        places.sort()
        # loop through results again
        for x in results:
            # if the id of the result is equal to the id of the runner
            if x.iden == runners[choice - 1].iden:
                # create a variable for the runner's place
                place = 0
                # loop through places
                for y in places:
                    # if the time of the runner is equal to the a time in places, then
                    # the person's place within the race is equal to the index of that place
                    if x.time == y:
                        place = places.index(y)
                # add 1 to the place as well as printing the time in minutes and seconds
                print(f"{i}\t{x.minutes()} min {x.time % 60} sec\t({place + 1} of {len(places)})")


def list_winners():
    # Print a title
    print("The following people have won at least one race:")
    print("=" * 48)
    # create a list of races
    races = create_race_list("Races.txt")
    # loop through the races
    for i in races:
        # create a list of runners and results for the respective race
        runners = create_runners("Runners.txt")
        results = create_result(f"{i.lower()}.txt")
        # create variables for the best time, the id of the winner and the winner's name
        best_time = 9999999999999
        winner_iden = "none"
        winner_name = "none"
        # loop through the results
        for x in results:
            # if the time is lower than the best time then the winner's identity is equal to the winner's identity
            # and the best time is the winner's time
            if x.time < best_time:
                winner_iden = x.iden
                best_time = x.time
        # loop through the list of runners
        for y in runners:
            # Equate the id of the winner to the id of a runner, the winner's name is the name of the person who's id
            # matches
            if winner_iden == y.iden:
                winner_name = y.name
        # print the name and the id of the winner
        print(f"{winner_name}\t({winner_iden})")

