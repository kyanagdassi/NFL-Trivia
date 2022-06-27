import pandas as pd
#Pandas dataframe import
#https://dataindependent.com/pandas/import-pandas-as-pd-bring-pandas-to-python/
import random
#Random library
#https://www.cs.swarthmore.edu/~adanner/cs21/f09/randomlib.php#:~:text=To%20get%20access%20to%20the,get%20different%20(random)%20results.
import time
#Time library
#https://docs.python.org/3/library/time.html
import jellyfish
#How to import a library that can find the similarity between 2 strings
#https://pypi.org/project/jellyfish/
import matplotlib.pyplot as plt
#How to import a library that allows user to see plot
#https://stackoverflow.com/questions/30558087/is-from-matplotlib-import-pyplot-as-plt-import-matplotlib-pyplot-as-plt#:~:text=It%20is%20generally%20customary%20to,shorter%20but%20no%20less%20clear.
import functools
#How to enable use of higher order functions with functools library
#https://docs.python.org/3/library/functools.html
 

data = pd.read_csv('NFLplayers.csv')

for i in range(len(data)):
  if data['Player'][i][0]=='\n':
    data.loc[i,'Player']=data.loc[i,'Player'][1:]
    #How to access a group of columns and rows according to thelabel
    #https://docs.python.org/3/library/functools.html


'''
Originally, the code below was used to create a list that orders the colleges from most common to least common. However, this caused the runtime to be unreasonably long, so the resulting list (college_most_popular) was copied after runnign the code and assigned to college_most_popular.

college_list = data['College'].tolist()
college_most_popular = []
while len(college_list)>267:
  college_most_popular.append(mode(college_list))
  college_list = [x for x in college_list if x!=mode(college_list)]
#How to find the mode of a list
#https://www.geeksforgeeks.org/python-statistics-mode-function/
while len(college_list)>0:
  college_most_popular.append(college_list[0])
  college_list = college_list[1:]
'''

college_most_popular=['Alabama', 'Ohio State', 'LSU', 'Notre Dame', 'Georgia', 'Michigan', 'Florida', 'Iowa', 'Oklahoma', 'Penn State', 'Washington', 'Clemson', 'Texas A&M', 'Auburn', 'Stanford', 'Oregon', 'Texas', 'Florida State', 'Mississippi State', 'South Carolina', 'Tennessee', 'UCLA', 'Wisconsin', 'Miami', 'Pittsburgh', 'Temple', 'USC', 'Missouri', 'Arkansas', 'Nebraska', 'Utah', 'North Carolina', 'Michigan State', 'Mississippi', 'Virginia Tech', 'Houston', 'Kentucky', 'Baylor', 'Virginia', 'TCU', 'Maryland', 'West Virginia', 'California', 'Colorado', 'Oregon State', 'Cincinnati', 'Boston College', 'Northwestern', 'Duke', 'Texas Tech', 'Boise State', 'Syracuse', 'Purdue', 'Oklahoma State', 'Wake Forest', 'Vanderbilt', 'Illinois', 'Florida Atlantic', 'Tulane', 'Arizona State', 'Kansas State', 'BYU', 'UCF', 'Memphis', 'Minnesota', 'Utah State', 'Rutgers', 'Wyoming', 'Louisville', 'Louisiana Tech', 'San Diego State', 'Toledo', 'Arizona', 'North Carolina State', 'Indiana', 'North Dakota State', 'Miami (Fla.)', 'Fresno State', 'SMU', 'Southern Mississippi', 'Iowa State', 'Buffalo', 'Western Kentucky', 'Western Michigan', 'Georgia Tech', 'Old Dominion', 'N.C. State', 'Washington State', 'Colorado State', 'Appalachian State', 'Rice', 'Kansas', 'Marshall', 'Central Michigan', 'Northern Illinois', 'Illinois State', 'Southern Methodist', 'North Texas', 'Arkansas State', 'San Jose State', 'Middle Tennessee State', 'UAB', 'James Madison', 'Akron', 'Delaware', 'San Diego', 'Charlotte', 'East Carolina', 'Ferris State', 'Northern Iowa', 'South Florida', 'Louisiana-Lafayette', 'South Carolina State', 'Hawaii', 'Tennessee-Chattanooga', 'Connecticut', 'Eastern Washington', 'Georgia Southern', 'Southern Illinois', 'Stony Brook', 'Eastern Michigan', 'Louisiana', 'Eastern Kentucky', 'Texas-El Paso', 'South Alabama', 'Brigham Young', 'Army', 'Louisiana State', 'Central Florida', 'William & Mary', 'Texas Christian', 'Air Force', 'Wagner', 'Idaho', 'Harvard', 'NC State', 'Mars Hill', 'North Carolina A&T', 'Northern Colorado', 'South Dakota', 'Indiana State', 'Lindenwood', 'Wisconsin-Whitewater', 'Montana State', 'Boise', 'Findlay', 'Regina (Canada)', 'Western State Colorado', 'Indiana PA, University of', 'Bowling Green State', 'Bloomsburg', 'University of Toledo', 'Sioux Falls', 'Stetson University', 'Alabama-Birmingham', 'Western Washington University', 'The Citadel', 'North Carolina Central', 'Missouri Western', 'Valdosta State', 'Louisiana-Monroe', 'Middle Tennessee', 'Louisiana-Monroe', 'Western Illinois', 'University of South Florida', 'Pennsylvania', 'Missouri S&T', 'Central Arkansas', 'Nevada', 'New Mexico', 'Southeast Missouri State', 'University of St. Thomas', 'Alabama-Birmingham', 'Grambling State', 'UNLV', 'Princeton', 'Grambling State', 'Southern Utah State', 'Duquesne', 'Bemidji State University', 'Youngstown State', 'Miami (Ohio)', 'Western Carolina', 'Humboldt State', 'NC State', 'UNLV', 'Saginaw Valley State', 'Cal-Berkeley', 'Tennessee-Martin', 'Holy Cross', 'Samford', 'Maine', 'Northern Arizona', 'Missouri Southern State', 'University of Arkansas at Pine Bluff', 'UMass Amherst', 'Western Carolina', 'Fordham', 'West Alabama', 'Princeton', 'UTEP', 'New Mexico', 'New Mexico', 'Ashland', 'Fayetteville State University', 'South Dakota', 'Presbyterian', 'West Alabama', 'Navy', 'University of Windsor', 'Lenoir-Rhyne', 'Grand Valley', 'Navy', 'Florida International', 'Southeast Missouri State', 'Southern California', 'Miami (Ohio)', 'Pitt', 'Weber State', 'Wis.-Whitewater', 'Bowling Green', 'Jacksonville State', 'Troy', 'University of South Florida', 'Marian', 'Southern California', 'Stephen F. Austin St.', 'Austin Peay', 'Fort Hays State', 'Pennsylvania', 'UNLV', 'Murray State', 'Missouri Western', 'West Georgia', 'Wisconsin-Platteville', "St. John's (Minn.)", 'Canisius College', 'Yale', 'Laval', 'Merrimack College', 'Sam Houston State', 'Chattanooga', 'Eastern Illinois', 'Alabama State', 'Missouri Western State', 'Navy', 'Youngstown State', 'Central Arkansas', 'Texas State', 'Virginia State', 'Missouri State', 'Cal Poly-S.L.O.', 'Berry College', 'Sam Houston State', 'Grambling State', 'Texas-San Antonio', 'Florida International', 'Virginia Commonwealth', 'Coastal Carolina', 'South Dakota', 'Malone University', 'York (Canada)', 'Valdosta State', 'Florida International', 'Alberta (Canada)', 'Ball State', 'Massachusetts', 'Tarleton State', 'Albany State (Ga.)', 'Charleston', 'Southern California', 'Eastern Illinois', 'Tecnológico de Monterrey', 'Southern Arkansas', 'California-Berkeley', 'Central Arkansas', 'Georgia State', 'Louisiana-Monroe', 'Ole Miss', 'Marist', 'San Diego St.', 'University of British Columbia', 'McKendree', 'South Dakota State', 'Montreal', 'Frostburg State', 'Troy', 'Concordia College St. Paul', 'Brown', 'Azusa Pacific', 'South Dakota State', 'Cal Poly', 'Italy', 'Weber State', 'Maine', 'Tulsa', 'Sioux Falls', 'Ohio', 'Massachusetts', 'Morgan State', 'Austria', 'Southeastern Louisiana', 'Wisconsin-Milwaukee', 'Alcorn State', 'Indiana State', 'Ball State', 'Indiana State', 'Central Missouri', 'Augustana (S.D.)', 'Washburn', 'Minnesota State', 'Towson State', 'Georgia State', 'Minnesota State', 'Elon', 'West Georgia', 'Rhode Island', 'The Citadel', 'Furman', 'Yale', 'Tulsa', 'Princeton', 'Houston Baptist University', 'Dubuque', 'Western Illinois', 'Greenville', 'Tennessee State', 'Tulsa', 'Texas-San Antonio', 'East Central', 'University of South Florida', 'Bryant', 'Liberty', 'Ole Miss', 'Wayne St.', 'Norfolk State', 'Holy Cross', 'Kutztown', 'Southern Oregon', 'Portland State', 'Minnesota State', 'Monterrey Tech', 'Ohio', 'California (PA)', 'Tiffin', 'Texas State-San Marcos', 'West Georgia','Liberty', 'Texas State-San Marcos', 'UMass Amherst', 'Loyola University', 'Samford', 'University of Arkansas at Pine Bluff', 'Wesley', 'Simon Fraser (Canada)', 'Dartmouth', 'North Dakota', 'Albany', 'South Dakota State', 'New Mexico State', 'Coastal Carolina', 'North Carolina A&T', 'Weber State', 'Tusculum College', 'Washburn', 'Prairie View A&M', 'Charleston (WV)', 'California (PA)', 'Prairie View A&M', 'Ball State', 'UMass Amherst', 'Texas-San Antonio', 'Villanova', 'Villanova', 'Georgia State', 'Fordham', 'Manitoba (Canada)', 'Dayton', 'Assumption College', 'Saginaw Valley State', 'Nevada', 'Southern Cal', 'Western Ontario (Canada)', 'North Carolina A&T', 'Rhode Island', 'Ohio', 'FIU', 'Concordia (Minn.)', 'Northwestern State (LA)', 'Colorado State-Pueblo', 'Montana State', 'Southeastern Oklahoma State', 'Bowling Green', 'Limestone', 'Assumption', 'Hobart', 'Lindenwood', 'Troy']

def similar_letters(guess, solution):
  global name_similarity
  guess=guess.lower().split()[1]
  #How to split string by space
  #https://www.w3schools.com/python/ref_string_split.asp
  solution=solution.lower().split()[1]
  if game_mode=='easy':
    if num_guesses>1:
      counter=name_similarity
      name_similarity=[]
      for i in range(len(counter)):
        name_similarity.append(counter[i])
        #How to add elemnent to list
        #https://www.w3schools.com/python/ref_list_append.asp
    for i in range(len(guess)):
      if guess[i] in solution:
        for a in range(len(solution)-1):
          if solution[a]==guess[i] and name_similarity[a]=='_':
            name_similarity[a]=guess[i]
  else:
    counter=name_similarity
    name_similarity=[]
    for i in range(len(counter)):
      name_similarity.append(counter[i])
    for i in range(len(name_similarity)):
      if len(guess)-1>=i and solution[i]==guess[i]:
        name_similarity.insert(i, solution[i])
        del name_similarity[i+1]
  name_similarity=functools.reduce(lambda x,y:x+y, name_similarity)
  #How to enable use of higher order functions with functools library
  #https://docs.python.org/3/library/functools.html
  return(name_similarity)
  



def popularity_rating(player_index):
  experience_popularity = 0
  college_popularity = 0
  position_popularity = 0
  if data['Exp'][player_index]=='R':
    experience_popularity = 10
  else:
    if 5<int(data['Exp'][player_index])<=8:
      experience_popularity = 25
    elif 8<int(data['Exp'][player_index])<=12:
      experience_popularity = 20
    else:
      experience_popularity = 15
  college_first_quartile=int(0.25*len(college_most_popular))
  college_third_quartile=len(college_most_popular)-college_first_quartile
  if data['College'][player_index]!=data['College'][player_index]:
    college_popularity=0
  elif college_most_popular.index(data['College'][player_index])<college_first_quartile:
    college_popularity = 25
  elif college_first_quartile<college_most_popular.index(data['College'][player_index])<=college_third_quartile:
    college_popularity = 10
  else:
    college_popularity = 0
  if data['Pos'][player_index]=='QB' or data['Pos'][player_index]=='WR' or data['Pos'][player_index]=='RB':
    position_popularity = 50
  elif data['Pos'][player_index]=='TE' or data['Pos'][player_index]=='DE' or data['Pos'][player_index]=='K' or data['Pos'][player_index]=='CB' or data['Pos'][player_index]=='LB':
    position_popularity = 25
  else:
    position_popularity = 0
  return(experience_popularity+college_popularity+position_popularity)

for i in range(len(data)):
  data.loc[i,'Popularity']=popularity_rating(i)

for i in range(len(data)):
  if (data['Team'][i]=='Raiders') or (data['Team'][i]=='Chiefs') or (data['Team'][i]=='Broncos') or (data['Team'][i]== 'Chargers'):
    data.loc[i, 'Division'] = 'AFC Wes†.rt'
  elif (data['Team'][i]=='Browns') or (data['Team'][i]=='Steelers') or (data['Team'][i]=='Ravens') or (data['Team'][i]== 'Bengals'):
    data.loc[i, 'Division'] = 'AFC North'
  elif (data['Team'][i]=='Patriots') or (data['Team'][i]=='Jets') or (data['Team'][i]=='Dolphins') or (data['Team'][i]== 'Bills'):
    data.loc[i, 'Division'] = 'AFC East'
  elif (data['Team'][i]=='Texans') or (data['Team'][i]=='Jaguars') or (data['Team'][i]=='Colts') or (data['Team'][i]== 'Titans'):
    data.loc[i, 'Division'] = 'AFC South'
  elif (data['Team'][i]=='49ers') or (data['Team'][i]=='Seahawks') or (data['Team'][i]=='Rams') or (data['Team'][i]== 'Cardinals'):
    data.loc[i, 'Division'] = 'NFC West'
  elif (data['Team'][i]=='Packers') or (data['Team'][i]=='Vikings') or (data['Team'][i]=='Lions') or (data['Team'][i]== 'Bears'):
    data.loc[i, 'Division'] = 'NFC North'
  elif (data['Team'][i]=='Giants') or (data['Team'][i]=='Cowboys') or (data['Team'][i]=='Eagles') or (data['Team'][i]== 'Commanders'):
    data.loc[i, 'Division'] = 'NFC East'
  elif (data['Team'][i]=='Falcons') or (data['Team'][i]=='Bucs') or (data['Team'][i]=='Saints') or (data['Team'][i]== 'Panthers'):
    data.loc[i, 'Division'] = 'NFC South'





def verify_guess(guess):
  #How to make strings lowercase
  #https://www.programiz.com/python-programming/methods/string/lower
  for i in range(len(data)):
    if data['Player'][i].lower()==guess.lower():
      return(True)
  return(False)


def player_difficulty(player):
  player_index = data['Player'].tolist().index(player)
  difficulty = (100-data['Popularity'][player_index])//1
  return('The difficulty of the player was %f out of 100' %(difficulty))
  #How to use floor division in Python
  #https://www.codingem.com/python-floor-division/

def win_checker(guess_current):
  return(guess_current == player_solution.lower())



def similarity_score(guess):
  player_bio_similarity = str((division_checker(guess)+team_checker(guess)+college_checker(guess)+position_checker(guess)+number_checker(guess))*2)+'%'
  bio_similarity_list.append(player_bio_similarity)
  if similar_letters(guess,player_solution).count('_')==0:
    #How to count frequency of string in string
    #https://www.w3schools.com/python/ref_list_count.asp
    player_name_similarity='Last Name: '+similar_letters(guess,player_solution)+' (last name is correct!!)'
  else:
    player_name_similarity='Last Name: '+similar_letters(guess,player_solution)
  similarity_guesses.append(float(player_bio_similarity[:-1]))
  if game_mode=='easy':
    bio =['division','team','college','position','number']
    hint_topic=random.choice(bio)
    if (hint_topic=='number' and number_checker(guess)==0):
      while number_checker(guess)==0:
        hint_topic=random.choice(bio)
        #How to choose random element from a list
        #https://www.w3schools.com/python/ref_random_choice.asp
        
    if num_guesses>1 and team_checker(guess_total[-2])==10 and hint_topic=='division':
      bio.remove('division')
      #How to remove element from list in Python
      #https://www.programiz.com/python-programming/methods/list/remove
      hint_topic=random.choice(bio)
    if hint_topic=='division':
      if division_checker(guess)==10:
        hint='Hint! - Division: Correct!'
        print(hint)
      elif division_checker(guess)==5:
        hint='Hint! - The conference (%s) is correct, but the division is incorrect.' %(data['Division'][guess_current_index][:3])
        print(hint)
      else:
        hint='%s: Incorrect' %(data['Division'][guess_current_index])
        print(hint)
    elif hint_topic == 'team':
      if team_checker(guess)==10:
        hint='Hint! - %s: Correct!' %(data['Team'][solution_index])
        print(hint)
      else:
        hint='Hint! - %s: Incorrect' %(data['Team'][guess_current_index])
        print(hint)
    elif hint_topic=='college':
      if college_checker(guess)==10:
        hint='Hint! - %s: Correct' %(data['College'][solution_index])
        print(hint)
      else:
        hint='Hint! - %s: Incorrect' %(data['College'][guess_current_index])
        print(hint)
    elif hint_topic=='position':
      if position_checker(guess)==10:
        hint='Hint! - %s: Correct!' %(data['Pos'][solution_index])
        print(hint)
      else:
        hint='Hint! - %s: Incorrect' %(data['Pos'][guess_current_index])
        print(hint)
    else:
      if number_checker(guess)==10:
        hint='Hint! - Jersey Number %s: Correct' %(data['#'][solution_index])
        print(hint)
      elif number_checker(guess)==0:
        hint='%s does not have a jersey number.' %(guess)
        print(hint)
      elif data['#'][guess_current_index] > data['#'][solution_index]:
        hint='Hint! - Jersey Number %s: Too high!' %(data['#'][guess_current_index])
        print(hint)
      else:
        hint='Hint! - Jersey Number %s: Too low!' %(data['#'][guess_current_index])
        print(hint)
  
    hint_list.append(hint)
    if (guesses_given-num_guesses)==1:
      bio =['division','team','college','position','number']
      bio.remove(hint_topic)
      hint_topic=random.choice(bio)
      #How to remove element from list in Python
      #https://www.programiz.com/python-programming/methods/list/remove
      if (hint_topic=='number' and number_checker(guess)==0):
        while number_checker(guess)==0:
          hint_topic=random.choice(bio)
      if num_guesses>1 and team_checker(guess_total[-2])==10 and hint_topic=='division':
        bio.remove('division')
        hint_topic=random.choice(bio)
      if hint_topic=='division':
        if division_checker(guess)==10:
          hint='Hint! - Division: Correct!'
          print(hint)
        elif division_checker(guess)==5:
          hint='Hint! - The conference (%s) is correct, but the division is incorrect.' %(data['Division'][guess_current_index][:3])
          print(hint)
        else:
          hint='%s: Incorrect' %(data['Division'][guess_current_index])
          print(hint)
      elif hint_topic == 'team':
        if team_checker(guess)==10:
          hint='Hint! - %s: Correct!' %(data['Team'][solution_index])
          print(hint)
        else:
          hint='Hint! - %s: Incorrect' %(data['Team'][guess_current_index])
          print(hint)
      elif hint_topic=='college':
        if college_checker(guess)==10:
          hint='Hint! - %s: Correct' %(data['College'][solution_index])
          print(hint)
        else:
          hint='Hint! - %s: Incorrect' %(data['College'][guess_current_index])
          print(hint)
      elif hint_topic=='position':
        if position_checker(guess)==10:
          hint='Hint! - %s: Correct!' %(data['Pos'][solution_index])
          print(hint)
        else:
          hint='Hint! - %s: Incorrect' %(data['Pos'][guess_current_index])
          print(hint)
      else:
        if number_checker(guess)==10:
          hint='Hint! - %s: Correct' %(data['#'][solution_index])
          print(hint)
        elif number_checker(guess)==0:
          hint='%s does not have a jersey number.' %(guess)
          print(hint)
        elif data['#'][guess_current_index] > data['#'][solution_index]:
          hint='Hint! - %s: Too high!' %(data['#'][guess_current_index])
          print(hint)
        else:
          hint='Hint! - %s: Too low!' %(data['#'][guess_current_index])
          print(hint)
  return('\nBio Similarity: %s \nEach category has a range of values from 0 to 20.\nDivision: 0, 10, or 20\nTeam: 0 or 20\nCollege: 0 or 20\nPosition: 0 or 20\nJersey Number: 0 to 20\n\nFor name similarity, _ means that last name letter has not been guessed yet, but a letter means that letter has been guessed in the last name.\nName Similarity: %s' %(player_bio_similarity, player_name_similarity))
  #How to use string interpolation in Python
  #https://www.programiz.com/python-programming/string-interpolation

def plot_similarity(guesses_amount):
  guess_list=[]
  for i in range(guesses_amount):
    guess_list.append(i+1)
  plt.ion()
  #How to enable user input while plot is displayed
  #https://stackoverflow.com/questions/41763420/python-interactive-plot-with-user-input
  
  if num_guesses==1:
    plt.scatter(guess_list, similarity_guesses, color='blue')
    #How to plot scatter plot using matplotlib.pyplot in Python
    #https://www.geeksforgeeks.org/matplotlib-pyplot-scatter-in-python/#:~:text=scatter()%20in%20Python,-Last%20Updated%20%3A%2015&text=Matplotlib%20is%20a%20comprehensive%20library,D%20plots%20and%20many%20more.
  else:
    plt.scatter(guess_list, similarity_guesses, color='blue')
    #How to plot scatter plot using matplotlib.pyplot in Python
    #https://www.geeksforgeeks.org/matplotlib-pyplot-scatter-in-python/#:~:text=scatter()%20in%20Python,-Last%20Updated%20%3A%2015&text=Matplotlib%20is%20a%20comprehensive%20library,D%20plots%20and%20many%20more.
    plt.plot(guess_list, similarity_guesses, color='blue')
    #how to plot graph python
    #https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
  plt.title('Your Bio Similarity For Each Guess')
  #how to title graph in python
  #https://www.tutorialkart.com/matplotlib-tutorial/matplotlib-pyplot-title/#:~:text=To%20set%20title%20for%20plot%20in%20matplotlib%2C%20call%20title(),plot%20to%20%E2%80%9CSample%20Title%E2%80%9D.
  plt.xlabel('Guess Number')
  if guess_current.lower()==player_solution.lower() or num_guesses==guesses_given:
    plt.ylabel('Bio Similarity of Guess to %s' %(player_solution))
  else:
    plt.ylabel('Bio Similarity of Guess to Mystery Player')
  #How to label x and y axis for python plots/scatterplots
  #https://python-graph-gallery.com/4-add-title-and-axis-label
  if verify_guess(guess_total[-1]):
    plt.show()
    #How to display matplotlib plot to user using plt.show()
    #https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.pyplot.show.html
  else:
    print('The plot cannot be displayed because the latest guess is invalid.')
def division_checker(guess):
  if data['Division'][guess_current_index]==data['Division'][solution_index]:
    return(10)
  else:
    if data['Division'][guess_current_index][:3]==data['Division'][solution_index][:3]:
      return(5)
    return(0)

def team_checker(guess):
  if data['Team'][guess_current_index]==data['Team'][solution_index]:
    return(10)
  else:
    return(0)

def college_checker(guess):
  if data['College'][guess_current_index]==data['College'][solution_index]:
    return(10)
  else:
    return(0)

def position_checker(guess):
  if data['Pos'][guess_current_index]==data['Pos'][solution_index]:
    return(10)
  else:
    return(0)

def number_checker(guess):
  if data['#'][guess_current_index]!=data['#'][guess_current_index]:
    return(0)
  elif data['#'][guess_current_index]==data['#'][solution_index]:
    return(10)
  else:
    return(round((100-abs(int(data['#'][guess_current_index])-int(data['#'][solution_index])))*0.1,1))


def score_calculator(time_total, num_guesses):
  time_average= int((time_total//num_guesses))
  if time_average>50:
    time_score=5
  else:
      time_score=30-(0.5*time_average)
  total_score=(5/3)*time_score+0.5*float(similarity_guesses[-1])
  return('Your averaged %a seconds per guess. Your final score was %a out of 100.' %(time_average, total_score//1))
  #How to use floor division in Python
  #https://www.codingem.com/python-floor-division/


def game_central():
  global player_solution
  global guess_current
  global guess_current_index
  global similarity_guesses
  global bio_similarity_list
  global letters_similarity_list
  global time_total
  global solution_index
  global num_guesses
  global guesses_given
  global game_mode
  global guess_total
  global hint_list
  global name_similarity
  plt.clf()
  plt.cla()
  name_similarity=[]
  print('\nWelcome to NFL Trivia! In this game, you will have to guess the name of the NFL player, which is determined by the computer.\nRules:\n1. You will be given the bio similarity between the guess and the solution based on 5 categories.\nCategories: division, team, position, college, and jersey number.\nHigh similarity percentages mean that the bio of the guess is very similar to the bio of the solution.\n2. You will be given the correct letters of the last name of the solution.\n3. You will be awarded more points if you guess quickly.\n')
  game_mode = ''
  hint_list=[]
  while game_mode.lower()!='easy' and game_mode.lower()!='hard':
    game_mode = input("This game has 2 modes: easy or hard.\nWhich mode would you like to play? ") 
  game_mode=game_mode.lower()
  if game_mode=='hard':
    popularity_difficult = list(map(lambda x: (100-x)**3, data['Popularity'].tolist()))
    player_solution = random.choices(data['Player'].tolist(), weights=(popularity_difficult))[0]
    solution_index = data['Player'].tolist().index(player_solution)
    guesses_given = 4
    print('Welcome to hard mode! In this challenging mode, you will have only %f guesses.' %(guesses_given))
  if game_mode=='easy':
    popularity_easy = list(map(lambda x: x**3, data['Popularity'].tolist()))
    player_solution = random.choices(data['Player'].tolist(), weights=(popularity_easy))[0]
    #How to use weighted probabilty to differentiate the probability of choosing each item
    #https://www.geeksforgeeks.org/how-to-get-weighted-random-choice-in-python/
    solution_index = data['Player'].tolist().index(player_solution)
    guesses_given = 6
    print('Welcome to easy mode! In this mode, you will have %f guesses.' %(int(guesses_given)))
  
  if data['Player'].tolist().count(player_solution)>1 or data['#'][solution_index]!=data['#'][solution_index]:
    while data['Player'].tolist().count(player_solution)>1 or data['#'][solution_index]!=data['#'][solution_index]:
      player_solution = random.choices(data['Player'].tolist(), weights=(data['Popularity'].tolist()))
      solution_index = data['Player'].tolist().index(player_solution[0])
  
  player_solution = data['Player'][solution_index]
  num_guesses = 0
  guess_current=''
  guess_total = []
  #assigning division to players based on team
  
  similarity_guesses=[]
  bio_similarity_list=[]
  letters_similarity_list=[]
  time_total=0
  start_time=0
  end_time=0
  player_solution_last=player_solution.split()[-1]
  for i in range(len(player_solution_last)):
    name_similarity.append('_')
  while guess_current.lower()!=player_solution.lower() and num_guesses<guesses_given:
    start_time = time.time()
    #Including start timer that begins timing while the user is inputting guess. #https://stackoverflow.com/questions/56711424/how-can-i-count-time-in-python-3
    guess_current = input("Guess the name of the NFL player: ")
    end_time = time.time()
    time_total+=end_time-start_time
    #Including end timer that stops timer and extracts the net time.      #https://stackoverflow.com/questions/56711424/how-can-i-count-time-in-python-3
    guess_current=guess_current.lower()
    if verify_guess(guess_current)==False:
      while verify_guess(guess_current)==False:
        print(guess_current,' is not a current NFL player.')
        invalid_guess_list=list(map(lambda x:jellyfish.jaro_distance(guess_current,x.lower()),data['Player'].tolist()))
        #How to convert array to list using tolist function
        #https://www.javatpoint.com/numpy-array-tolist#:~:text=tolist()%2C%20used%20to%20convert,elements%20as%20a%20Python%20list.
        #How to make strings lowercase
        #https://www.programiz.com/python-programming/methods/string/lower
        #How to measure similarity between two strings using the jellyfish library to use jaro_distance
        #https://www.geeksforgeeks.org/jaro-and-jaro-winkler-similarity/
        max_value=max(invalid_guess_list)
        #How to find maximum value of list using max function
        #https://www.tutorialspoint.com/python/list_max.htm
        max_index = invalid_guess_list.index(max_value)
        misspelled_player=data['Player'][max_index].lower()
        guess_current=input('Did you mean to type %s? Type yes or no:  ' %(misspelled_player))
        #How to use string interpolation
        #https://www.programiz.com/python-programming/string-interpolation
        #User input assigned to variable
        #https://www.geeksforgeeks.org/taking-input-in-python/
        guess_current=guess_current.lower()
        if guess_current!="yes" and guess_current!='no':
          while guess_current!='yes' and guess_current!='no':
            guess_current=input('Did you mean to type %s? Type yes or no:  ' %(misspelled_player))
        if guess_current=='yes':
          guess_current=misspelled_player
        else:
          #How to find start and end time in python to find elapsed time using time library
          #https://stackoverflow.com/questions/7370801/how-to-measure-elapsed-time-in-python
          start_time=time.time()
          guess_current = input("Guess the name of the NFL player: ")
          end_time=time.time()
          guess_current = guess_current.lower()
      time_total+=end_time-start_time
    guess_total.append(guess_current)
    guess_current_index=0
    for i in range(len(data)):
      if data['Player'][i].lower()==guess_current.lower():
        guess_current_index=i
    num_guesses+=1
    if guess_current!=player_solution.lower():
      print(similarity_score(guess_current))
      print('You have %f guesses remaining.' %(int(guesses_given-num_guesses)))
    else:
      similarity_guesses.append(100)
    plot_similarity(num_guesses)
        
  
  if win_checker(guess_current):
    print('Congratulations! You guessed the player ', player_solution,' in ',len(guess_total), ' guesses.')
    print(score_calculator(time_total, num_guesses))
  else:
    print('You lost the game. The player was ',player_solution)
    print(score_calculator(time_total, num_guesses))
  print(player_difficulty(player_solution))
  plot_similarity(num_guesses)

game_central()
play_again=''
while play_again.lower()!='no':
  play_again=input('\nDo you want to play again?\nType in either yes or no to indicate whether or not you want to play again: ')
  play_again=play_again.lower()
  if play_again=='yes':
    game_central()
  elif play_again=='no':
    print('Thank you for playing NFL Trivia!')
  else:
    while play_again.lower()!='yes' and play_again.lower()!='no':
      play_again=input('\nDo you want to play again?\nType in either yes or no to indicate whether or not you want to play again: ')
    if play_again.lower()=='yes':
      game_central()
    else:
      print('Thank you for playing NFL Trivia!')