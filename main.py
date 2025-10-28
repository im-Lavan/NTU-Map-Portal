# import statements.
# import folium statement to access map in python.
# import browser to open our map in our default web browser.
import folium
import webbrowser


# Defining functions I used in my code
# for printing eligibility message.
def eligibility_message():
    print("\nHi", stu_name, ", you are eligible to access this site.")


# for printing error message on ID or Name is incorrect.
def id_check():
    print("\nPlease Check your name or Student ID again!")


# for printing error message on Building name.
def error_message():
    print("\nMake sure that building name is correct!")


# Building names will be callable from here for suggestion
def call_building_names():
    for separate_buildings in building_names:
        print(separate_buildings)


# error message will show if building name is wrong.
# expecting input from the user to give assistance to them.
# if they want whole building names will be list out.
# after assistance, they can input building names again.
def suggestion_call():
    error_message()
    user_statement = input("You wanna know the details about the buildings name? [yes] or [No]: ").upper()

    if user_statement == "YES":
        call_building_names()
        map_entry()

    elif user_statement == "NO":
        exit()

    else:
        print("You can use [Yes] or [No] only!!!")
        suggestion_call()


# for getting entry from the user.
# you can use any of the buildings names in NTU clifton campus. if you don't know
# the building name accurately you can use a name as you know, it will suggest you according to your input.
def map_entry():
    if stu_name and stu_id:
        current_point = input("Where are you now? ").upper()
        destination_point = input("Where you wanted to go? ").upper()

    # check that inputted current building in the dictionary
    current_building = None
    for c_building in buildings_coordinates:
        if c_building["name"] == current_point:
            current_building = c_building

    # check that inputted destination building in the dictionary
    destination_building = None
    for d_building in buildings_coordinates:
        if d_building["name"] == destination_point:
            destination_building = d_building

    # if those buildings_coordinates in the dictionary map will trigger
    if current_building and destination_building:
        my_map = folium.Map(location=current_building["coords"], zoom_start=15)

        # current building will be shown with "A" on the starting of the building name.
        folium.Marker(location=current_building["coords"], popup=f'A:{current_point}',
                      icon=folium.Icon(color='orange')).add_to(my_map)

        # current building will be shown with "B" on the starting of the building name.
        folium.Marker(location=destination_building["coords"], popup=f'B:{destination_point}',
                      icon=folium.Icon(color='orange')).add_to(my_map)

        # connecting 2 points by a straight line.
        folium.PolyLine(locations=[destination_building["coords"], current_building["coords"]], color="blue").add_to(
            my_map)

        # assigning the map in "map.html" file and assign that into temp_path.
        temp_path = 'map.html'

        # updates will be added on "map.html"
        my_map.save(temp_path)

        # created map will open our default browser.
        webbrowser.open(temp_path)
        exit()

    # it is a suggestion block
    # if the user not knowing the destination name clearly it will suggest some according to their entries.
    elif not current_building or not destination_building:

        # creating empty strings to assigning the first 3 letters of the users input.
        c_point_suggestions = ""
        d_point_suggestions = ""

        # getting the first 3 letters of the current point value.
        x = 0
        for c_building_letters in current_point:
            if x <= 2:
                c_point_suggestions += c_building_letters
                x += 1

        # getting the first 3 letters of the destination point value.
        y = 0
        for d_building_letters in destination_point:
            if y <= 2:
                d_point_suggestions += d_building_letters
                y += 1

        # creating empty lists to assign the top 5 building suggestions.
        c_top_suggestions = []
        d_top_suggestions = []

        # if any buildings_coordinates related to the users entry that will be appended
        for c_building_name in building_names:
            if c_point_suggestions in c_building_name and len(c_top_suggestions) < 10:
                c_top_suggestions.append(c_building_name)

        # if any buildings_coordinates related to the users entry that will be appended
        for d_building_name in building_names:
            if d_point_suggestions in d_building_name and len(d_top_suggestions) < 10:
                d_top_suggestions.append(d_building_name)

        # if current point have any suggestions, then will be listed here.
        if c_top_suggestions:
            if current_point not in c_top_suggestions:
                print("\nYou mean by '", current_point, "'is:\n")
                for suggestion_for_c in c_top_suggestions:
                    print(suggestion_for_c)
                map_entry()

        # if suppose can't be able to find any buildings_coordinates according to your input, error message will
        # trigger. users will be offered to get the whole places names in NTU if they get the building or point name
        # from there then they can enter the building details without exiting from the program.
        else:
            print("\nNo Matches found for '", current_point, "'")
            suggestion_call()

        # if destination point have any suggestions, then will be listed here.
        if d_top_suggestions:
            if destination_point not in d_top_suggestions:
                print("\nYou mean by '", destination_point, "'is:\n")
                for suggestion_for_d in d_top_suggestions:
                    print(suggestion_for_d)
                map_entry()

        # if suppose can't be able to find any buildings_coordinates according to your input, error message will
        # trigger. users will be offered to get the whole places names in NTU if they get the building or point name
        # from there then they can enter the building details without exiting from the program.
        else:
            print("\nNo Matches found for '", destination_point, "'")
            suggestion_call()


# for printing suggestion building name.
building_names = ["\nDH LAWRENCE ",
                  "HEALTH AND ALLIED PROFESSION CENTRE ",
                  "CLIFTON LIBRARY",
                  "CLIFTON TEACHING BUILDING",
                  "CENTRE FOR EFFECTIVE LEARNING IN SCIENCE",
                  "JOHN CLARE LECTURE THEATRE",
                  "ADA BYRON KING",
                  "INTERDISCIPLINARY SCIENCE AND TECHNOLOGY CENTRE",
                  "MEDICAL TECHNOLOGIES INNOVATION FACULTY",
                  "ROSALIND FRANKLIN",
                  "ENGINEERING AND INSTITUTE FOR DIGITAL INNOVATION",
                  "INTERDISCIPLINARY BIOMEDICAL RESEARCH CENTRE",
                  "I-SMART",
                  "ERASMUS DARWIN",
                  "MARY ANN EVANS",
                  "NEW HALL BLOCK",
                  "MAIN BUS ENTRANCE",
                  "THE GATE HOUSE",
                  "BASEMENT BAR",
                  "NTSU STORE",
                  "ACTIVITIES HQ",
                  "STUDENT SUPPORT SERVICE",
                  "EMERGENCY SECURITY CALL POINT",
                  "MAINTENANCE",
                  "CLIFTON SPORTS HUB",
                  "CLIFTON TENNIS CENTRE",
                  "THE CLUB HOUSE",
                  "HOCKEY PITCH",
                  "3G PITCH",
                  "PITCH 1",
                  "PITCH 2",
                  "PITCH 3",
                  "PITCH 4",
                  "PITCH 5",
                  "STUDENT SERVICE CENTER",
                  "REFECTORY",
                  "PAVILION",
                  "GLOBAL LOUNGE",
                  "ENTRANCE"
                  "ISTEC"
                  ]
# adding building names and coordinates in dictionary.
buildings_coordinates = [
    {"name": "DH LAWRENCE", "coords": (52.911943, -1.184030)},
    {"name": "HEALTH AND ALLIED PROFESSION CENTRE", "coords": (52.912776, -1.184054)},
    {"name": "CLIFTON LIBRARY", "coords": (52.912122, -1.186838)},
    {"name": "CLIFTON TEACHING BUILDING", "coords": (52.911557, -1.186303)},
    {"name": "CENTER FOR EFFECTIVE LEARNING IN SCIENCE", "coords": (52.911116, -1.186707)},
    {"name": "JOHN CLARE LECTURE THEATRE", "coords": (52.911504, -1.185412)},
    {"name": "ADA BYRON KING", "coords": (52.911156, -1.185066)},
    {"name": "INTERDISCIPLINARY SCIENCE AND TECHNOLOGY CENTRE", "coords": (52.910926, -1.184469)},
    {"name": "MEDICAL TECHNOLOGIES INNOVATION FACULTY", "coords": (52.910422, -1.185156)},
    {"name": "ROSALIND FRANKLIN", "coords": (52.910585, -1.185658)},
    {"name": "ENGINEERING AND INSTITUTE FOR DIGITAL INNOVATION", "coords": (52.910772, -1.186082)},
    {"name": "INTERDISCIPLINARY SCIENCE AND TECHNOLOGY CENTRE", "coords": (52.91099953061445, -1.1843069718737258)},
    {"name": "ISTEC", "coords": (52.91099953061445, -1.1843069718737258)},
    {"name": "i-SMART", "coords": (52.910407, -1.186522)},
    {"name": "ERASMUS DARWIN", "coords": (52.909950, -1.186977)},
    {"name": "MARY ANN EVANS", "coords": (52.911551, -1.184312)},
    {"name": "MAE", "coords": (52.911551, -1.184312)},
    {"name": "GLOBAL LOUNGE", "coords": (52.911551, -1.184312)},
    {"name": "NEW HALL BLOCK", "coords": (52.912485, -1.186172)},
    {"name": "MAIN BUS ENTRANCE", "coords": (52.911803, -1.181698)},
    {"name": "ENTRANCE", "coords": (52.911803, -1.181698)},
    {"name": "THE GATE HOUSE", "coords": (52.912334, -1.182915)},
    {"name": "BASEMENT BAR", "coords": (52.912119, -1.183383)},
    {"name": "NTSU STORE", "coords": (52.912249, -1.183948)},
    {"name": "ACTIVITIES HQ", "coords": (52.912102, -1.184199)},
    {"name": "STUDENT SUPPORT SERVICE", "coords": (52.912610, -1.184627)},
    {"name": "EMERGENCY SECURITY CALL POINT", "coords": (52.913382, -1.184564)},
    {"name": "MAINTENANCE", "coords": (52.912866, -1.185263)},
    {"name": "CLIFTON SPORTS HUB", "coords": (52.911261, -1.187772)},
    {"name": "CLIFTON TENNIS CENTRE", "coords": (52.911763, -1.188594)},
    {"name": "THE CLUB HOUSE", "coords": (52.912166, -1.188135)},
    {"name": "HOCKEY PITCH", "coords": (52.912205, -1.189021)},
    {"name": "3G PITCH", "coords": (52.911668, -1.190194)},
    {"name": "PITCH 1", "coords": (52.909932, -1.184730)},
    {"name": "PITCH 2", "coords": (52.910625, -1.188515)},
    {"name": "PITCH 3", "coords": (52.914204, -1.184711)},
    {"name": "PITCH 4", "coords": (52.913010, -1.182248)},
    {"name": "PITCH 5", "coords": (52.912559, -1.181551)},
    {"name": "STUDENT SERVICE CENTRE", "coords": (52.911826, -1.184689)},
    {"name": "REFECTORY", "coords": (52.912288, -1.185282)},
    {"name": "PAVILION", "coords": (52.912129, -1.185911)}

]

# welcoming user to this program.
print("\nWelcome to NTU Map Portal.")
print("You can able to access this if you are a member of NTU by using your Student ID. \n")

# open a file in append mode as "student ID.txt"
f1 = open("Student ID.txt", "a")

# if nothing in the file "Name","student ID" will print as a titles.
if f1.tell() == 0:
    f1.write(f"{'Name':<20} {'Student ID':<12}\n")

# it will run till they input their Name and Student ID correctly.
# getting input from user to check and save to file.
# change the input to whole uppercase to reduce errors and make the checking section easy.
# Name can't contain any numbers in it.
# student ID should start with "N" or "T" , it should contain 8 characters only and also "N" or "T" should be on the top.
while True:
    stu_name = input("Enter your Name: ").upper()
    stu_id = input("Enter your student ID: ").upper()

    # Users can't input any digits while they input their name.
    # then it will show error message after they input their student ID
    if any(char.isdigit() for char in stu_name):
        id_check()

    # it is student ID check
    # if the ID not containing "N" or "T" it will show an ID check error message.
    # if the student ID not start with "N" or "T" it will show an ID check error message.
    # if the data will correct then "map_entry" function will call.
    elif ("N" in stu_id[0] or "T" in stu_id[0]) and len(stu_id) == 8:
        eligibility_message()
        f1.write(f"{stu_name:<20} {stu_id:<12}\n")
        map_entry()

    # if you are not enter your details correctly ID Check error message will trigger here
    else:
        id_check()

# created file will close here
f1.close()
