# CalorieCounter


Calorie Counter Documentation
Introduction:
The Calorie Counter application is one to be used by any person trying to lose any weight. It takes in personal information, such as age and height, and responds with a calorie per day limit needed to achieve goal weight, entered by a user. A precise algorithm is used, based off said personal information, as well as the time the user wants to achieve their goal in, and how often they exercise. The user can log into the app every day, and input the foods they eat, along with the calories. Calorie Counter will keep track of the number of calories the user eats and will let them know how many more calories they can eat that day. If used every day, it will also tell they user their “streak”, or how many days in a row they have achieved their goal of staying under that limit.
-Python
-Microsoft SQL
-Tkinter Library
-pyodbc database connection


Global functions:
Read(conn):
This function prints all the information held in the database to the console. This information comes from the users, goals, and user_activity tables.
Raise_frame(frame):
This is a function that calls a tkinter function which displays the screen used as an argument.
Main_label(frame):
This function adds a main label, “Calorie Counter” to the page used as an argument. This function is called for every page.
Delete(screen):
This function terminates the process of a window, or a screen. This is used for warning screens, such as one to let the user know their username/ password is incorrect.

Login: 
The login page refers to a Microsoft SQL Server for its authentication process. This is how users log into their account. They can also click a button to go to sign up screen.
Function(s):
log_in():
	This function searches the database table, users, for a username and password that is entered. If an account has been registered with that username and password, it will redirect them to the set goal page if they have not set one yet, or the log page if they have. If the system did not find their username and password in the database, a window pops up warning them that the username or password is invalid.

Signup:
The signup page refers to a Microsoft SQL Server for it’s authentication process. This is how users register their account. 
Function(s):
Sign_up(email1, username1, password1):
	This function enters username, password, and email information as varchars into the users table of the Calorie Counter database. If any fields are left blank, a warning screen will appear notifying the user that they need to entire all fields.
Set Goal:
The set goal page takes in personal information from the user and calculates the daily calorie limit. This information includes weight, height, goal weight, how often they exercise, gender, and the amount of time to reach that goal weight.
Function(s):
Get_calburnedperday(bmi, kg, gender_cor, act_cor)
This function takes in a persons bmi, weight in kilograms, their gender, and the amount they exercise, and returns the amount of calories that person burns in one day. It uses basic metabolic rate (calories burned in a day at rest) as well as amount of exercise
Calc_lim(weight1, goalweight1, height1, clicked_activity, clicked_gender, clicked_length):
This function takes in the user’s weight, goal weight, height, amount of exercise, their gender, and the time that they want to achieve the goal in. It calls the get_calburnedperday function to create a strict calorie limit for a person to eat if they want to reach that goal in the desired time.
Log page:
This is sort of the main page of the application. This is where the user will see their calorie limit, their amount of calories eaten that day, as well as their streak. It has a button named ‘log’ that will redirect them to a page to log their food. No particular functions.
Log Manually page:
This is the page where users can log their food. It asks for a meal name, as well as a calorie amount for the food. It allows up to 5 meals logged per day
Function(s):
Log(calorie_amount, food_name)
This function sends the calorie amount and the food name to the database, so that the user can see it later. It also adds the calorie amount for the running total for that day, so that the user can see how many more calories they can eat that day.
 



