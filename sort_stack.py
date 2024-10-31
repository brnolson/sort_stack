# UMMB Trombone PPA Leadership Assignment Manager.

#  ____    ___   ____  _____   ____  _____   _     ____  _  __
# / ___|  / _ \ |  _ \|_   _| / ___||_   _| / \   / ___|| |/ /
# \___ \ | | | || |_) | | |   \___ \  | |  / _ \ | |    | ' / 
#  ___) || |_| ||  _ <  | |    ___) | | | / ___ \| |___ | . \ 
# |____/  \___/ |_| \_\ |_|   |____/  |_|/_/   \_\\____||_|\_\
#                         ...like trombone pancakes, get it?                                                             

''' 
FOLLOW THESE STEPS TO USE:
1.) Edit the fields below with the current season's information.
2.) Run program with python environment (powershell, google colab, or other env).
3.) Screenshot or copy paste output (no data is saved by the script).

'''
##################################################################################
# EDIT THE FOLLOWING FIELDS:
##################################################################################

# Replace the number below to the total number of PPA's this season.
numberOfPPAs = 4

# Add each member of the BLT in quotations and a comma between.
# Be sure to add new fields and delete unused fields when needed.
# The program will automatically enumerate the section data.
leadershipTeam = {
    "Maroon Leader 1" : "Maroon 1",
    "Maroon Leader 2" : "Maroon 2",
    "Maroon Leader 3" : "Maroon 3",
    "Gold Leader 1" : "Gold 1",
    "Gold Leader 2" : "Gold 2",
    "Gold Leader 3" : "Gold 3",
}

# Replace each member in list with current seasons's trombonists.
# Ensure they are in line with their PPA group.
''' IF EVER THE AMOUNT OF PPA GROUPS CHANGE THE INTERNAL CODE WILL REQUIRE MODIFICATION '''
# Be sure to add new fields and delete unused fields when needed.
# The program will automatically enumerate the section data.
bandMemberList = {
    "Member 1" : "Maroon 1",
    "Member 2" : "Maroon 1",
    "Member 3" : "Maroon 1",
    "Member 4" : "Maroon 1",

    "Member 5" : "Maroon 2",
    "Member 6" : "Maroon 2",
    "Member 7" : "Maroon 2",
    "Member 8" : "Maroon 2",

    "Member 9" : "Maroon 3",
    "Member 10" : "Maroon 3",
    "Member 11" : "Maroon 3",
    "Member 12" : "Maroon 3",

    "Member 13" : "Maroon 4",
    "Member 14" : "Maroon 4",
    "Member 15" : "Maroon 4",
    "Member 16" : "Maroon 4",

    "Member 17" : "Maroon 5",
    "Member 18" : "Maroon 5",
    "Member 19" : "Maroon 5",
    "Member 20" : "Maroon 5",

    "Member 21" : "Gold 1",
    "Member 22" : "Gold 1",
    "Member 23" : "Gold 1",
    "Member 24" : "Gold 1",

    "Member 25" : "Gold 2",
    "Member 26" : "Gold 2",
    "Member 27" : "Gold 2",
    "Member 28" : "Gold 2",

    "Member 29" : "Gold 3",
    "Member 30" : "Gold 3",
    "Member 31" : "Gold 3",
    "Member 32" : "Gold 3",

    "Member 33" : "Gold 4",
    "Member 34" : "Gold 4",
    "Member 35" : "Gold 4",
    "Member 36" : "Gold 4",

    "Member 37" : "Gold 5",
    "Member 38" : "Gold 5",
    "Member 39" : "Gold 5",
    "Member 40" : "Gold 5",
}

##################################################################################
# STOP HERE!
# Now, run the program and try to get the smallest variability score possible.
##################################################################################

numLeaders = sum(1 for names in leadershipTeam)
numMembers = sum(1 for names in bandMemberList)
groups = {
    "Maroon 1" : list(bandMemberList.values()).count("Maroon 1"), 
    "Maroon 2" : list(bandMemberList.values()).count("Maroon 2"),
    "Maroon 3" : list(bandMemberList.values()).count("Maroon 3"),
    "Maroon 4" : list(bandMemberList.values()).count("Maroon 4"),
    "Maroon 5" : list(bandMemberList.values()).count("Maroon 5"),
    "Gold 1" : list(bandMemberList.values()).count("Gold 1"),
    "Gold 2" : list(bandMemberList.values()).count("Gold 2"),
    "Gold 3" : list(bandMemberList.values()).count("Gold 3"),
    "Gold 4" : list(bandMemberList.values()).count("Gold 4"),
    "Gold 5" : list(bandMemberList.values()).count("Gold 5"),
}

#TODO Implement mainSort according to README.md
def mainSort():
    print()
            
# main method.
if __name__ == "__main__":
    mainSort()