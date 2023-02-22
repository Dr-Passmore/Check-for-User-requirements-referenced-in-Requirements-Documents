"""
The following code compares the list of user stories currently referenced in the Requirements document. The User Stories coloumn is copied into the .txt file. 

The range of user story referenced are in the format which start with US0 with a total of 85 User Stories. 

To enable the creation of the requirements document to cover all user stories, this script highlights those missing. 

In the completion of the requirements document this script also enables the excluded stories to be recorded and documented.
"""

#Initial list creation to compare content
list_of_user_stories = []
used_items = []
requirements = 0

#Creates the User requirements list in the same string format
for i in range(1, 86):
    if i < 10:
        i = f"US00{i}"
    else:    
        i = f"US0{i}"
    #Adds each item to the list of User Stories
    list_of_user_stories.append(i)

#Grabs the data in the userstories used text file
with open(r'userstories used.txt') as f:
    data = f.read()
#processes data splits the data by new line
cleaned_data = data.split('\n')
for i in cleaned_data:
    #splits the data based on " " to provide a list of items
    values = i.split()
    requirements += 1
    for j in values:
        #for each item found it is appended to list
        used_items.append(j)
#Removes duplicates in the list        
used_items = set(used_items)
#compares the two lists to check for any user stories not referenced in the document. 
remaining_user_requirements = [i for i in list(list_of_user_stories) if i not in used_items]

#Prints the % user stories that have not been used along with a final list of unreferenced stories
print(f"The percentage of user stories currently covered by the {requirements} requirements is {round((len(used_items))/(len(list_of_user_stories))*100, 1)}%. {(len(list_of_user_stories)) - (len(used_items))} user stories have not been referenced")
print(f"The user stories that have not been referenced are: {remaining_user_requirements}")