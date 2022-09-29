from tkinter import *
import pyodbc
from datetime import datetime

#GLOBAL DATA
today_date = datetime.today()

#SQL CoNNECTION
def read(conn):
	print("Read")
	cursor = conn.cursor()
	print("users: ")
	cursor.execute("select * from users;")
	for row in cursor:
		print(f'row = {row}')
	print()
	print("goals: ")
	cursor.execute("select * from goals;")
	for row in cursor:
		print(f'row = {row}')
	print()
	print("user_activity: ")
	cursor.execute("select * from user_activity;")
	for row in cursor:
		print(f'row = {row}')
	print()
def create(conn):
	print("Create")
	cursor = conn.cursor()
	cursor.execute(
		"insert into users values(2, 'johndoe@gmail.com', 'john_doe', 'john123' );"
		
		)
	conn.commit()
	read(conn)


conn = pyodbc.connect(
	"DRIVER={SQL Server};SERVER=ILANSPC;DATABASE=CalorieCounter;Trusted_Connection=yes;"

	)

#SHOW PAGE FUNCTION
def raise_frame(frame):
	frame.tkraise()

#BACK BUTTON FUNCTION
def place_back_button(frame, backframe):
	Button(frame, text = 'Back', font = ('Russo One', 14, 'bold'), bg = 'white', fg = 'blue', command= lambda: raise_frame(backframe)).place(relx = 0.5, rely = 0.9, anchor=CENTER)	


#ROOT WINDOW
root = Tk()
root.title('Calorie Counter')
icon = PhotoImage(file = 'C:\\Users\\ilane\\Documents\\Brookdale Fall 2021\\Software Capstone\\CalorieCounterPython\\caloriecountericon.png')
root.iconphoto(False, icon)
root.geometry('1000x640')
root.resizable(0,0)
root.config(bg = '#E46B27')

#FRAME DECLARATION
login_page = Frame(root, height=640, width=1000,bg = '#E46B27')
signup_page = Frame(root, height=640, width=1000,bg = '#E46B27')
setgoal_page = Frame(root, height=640, width=1000,bg = '#E46B27')
log_page = Frame(root, height=640, width=1000,bg = '#E46B27')
logmanually_page = Frame(root, height=640, width=1000,bg = '#E46B27')
nutritionguide_page = Frame(root, height=640, width=1000,bg = '#E46B27')

for frame in (login_page, signup_page, setgoal_page, log_page, logmanually_page, nutritionguide_page):
	frame.grid(row=0, column=0, sticky='news')

#MAIN LABEL FUNCTION
def main_label(frame):
	main_label =Label(frame, text ='Calorie Counter!', font = ('Russo One', 48, 'bold'), bg = '#E46B27')
	main_label.place(relx = 0.5, rely = 0.1, anchor=CENTER)	


#LOGIN PAGE
username = StringVar()
password = StringVar()

#LOGIN FUNCTIONS
def log_in():
	global active_id
	global active_username
	cursor = conn.cursor()
	cursor.execute("select * from users where Username = ? and Password_ = ?;",(username.get(), password.get()))
	row = cursor.fetchone()
	if row:
		print(row)
		active_id = row[0]
		active_username = row[2]
		Label(setgoal_page, text = 'Hello ' + active_username, font = ('Russo One', 20, 'bold'), bg = '#E46B27').place(relx = 0.5, rely = 0.2, anchor=CENTER)
		raise_frame(setgoal_page)
	else:
		screen1 = Toplevel(root)
		screen1.title('Warning')
		screen1.iconphoto(False, icon)
		screen1.geometry('400x220')
		screen1.resizable(0,0)
		screen1.config(bg = '#E46B27')
		Label(screen1, text='Invalid User/Pass',font=('Russo One', 20, 'bold'),pady=20,bg = '#E46B27' ).pack()
		Button(screen1, text='OK', command= lambda: delete(screen1)).pack()
		print('invalid user/pass')
	conn.commit()
	
	

#DETAILS
main_label(login_page)
Label(login_page, text = 'Login', font = ('Russo One', 26, 'bold'),bg = '#E46B27').place(relx = 0.5, rely = 0.2, anchor=CENTER)	
Label(login_page, text = 'Username:', font = ('Russo One', 14, 'bold'),bg = '#E46B27').place(relx = 0.5, rely = 0.3, anchor=CENTER)	
Entry(login_page, textvariable = username).place(relx = 0.5, rely = 0.35, anchor=CENTER)	
Label(login_page, text = 'Password:', font = ('Russo One', 14, 'bold'),bg = '#E46B27').place(relx = 0.5, rely = 0.45, anchor=CENTER)	
Entry(login_page, textvariable = password).place(relx = 0.5, rely = 0.5, anchor=CENTER)	
Button(login_page, text = 'Log In', width = 10, height = 1, command=lambda: log_in()).place(relx = 0.5, rely = 0.6, anchor=CENTER)	
Button(login_page, text = 'Or Sign Up', font = ('Russo One', 14, 'bold'), bg = 'white', fg = 'blue', command= lambda: raise_frame(signup_page)).place(relx = 0.5, rely = 0.7, anchor=CENTER)	


	
#SIGNUP PAGE
username1 = StringVar()
password1 = StringVar()
email1 = StringVar()

#SIGNUP FUNCTIONS
def delete(screen):
	screen.destroy()

def sign_up(email1, username1, password1):
	if email1.get() == '' or username1.get() == '' or password1.get() == '':
		screen1 = Toplevel(root)
		screen1.title('Warning')
		screen1.iconphoto(False, icon)
		screen1.geometry('400x220')
		screen1.resizable(0,0)
		screen1.config(bg = '#E46B27')
		Label(screen1, text='All fields required!',font=('Russo One', 20, 'bold'),pady=20,bg = '#E46B27' ).pack()
		Button(screen1, text='OK', command= lambda: delete(screen1)).pack()
	else:
		cursor = conn.cursor()
		cursor.execute("insert into users (Email, Username, Password_, IsGoalSet) values (?, ?, ?, 0);",(email1.get(), username1.get(), password1.get()))
		conn.commit()
		read(conn)
		raise_frame(login_page)

	
#DETAILS
main_label(signup_page)
Label(signup_page, text = 'Signup', font = ('Russo One', 20, 'bold'), bg = '#E46B27').place(relx = 0.5, rely = 0.2, anchor=CENTER)
Label(signup_page, text = 'E-mail:', font = ('Russo One', 14, 'bold'), bg = '#E46B27').place(relx = 0.5, rely =0.3, anchor=CENTER)
Entry(signup_page, textvariable = email1).place(relx = 0.5, rely = 0.35, anchor=CENTER)
Label(signup_page, text = 'Username:', font = ('Russo One', 14, 'bold'), bg = '#E46B27').place(relx = 0.5, rely = 0.4, anchor=CENTER)
Entry(signup_page, textvariable = username1).place(relx = 0.5, rely = 0.45, anchor=CENTER)
Label(signup_page, text = 'Password:', font = ('Russo One', 14, 'bold'), bg = '#E46B27').place(relx = 0.5, rely = 0.5, anchor=CENTER)
Entry(signup_page, textvariable = password1).place(relx = 0.5, rely = 0.55, anchor=CENTER)
Button(signup_page, text = 'Sign Up', width = 10, height = 1, command=lambda: sign_up(email1, username1, password1)).place(relx = 0.5, rely = 0.65, anchor=CENTER)
place_back_button(signup_page, login_page)


#SETGOAL PAGE
weight1 = IntVar() 
height1 = IntVar() 
goalweight1 = IntVar() 
clicked_activity = StringVar()
clicked_gender = StringVar()
clicked_length = StringVar()
cal_lim = 0


#SIGNUP FUNCTIONS
def get_calburnedperday(bmi, kg, gender_cor, act_cor):
	bmr = 0
	lfm = 0
	if gender_cor == 1:
		if bmi >= 10 and bmi <= 14:
			lfm = 1
		elif bmi > 14 and bmi <= 20:
			lfm = 0.95
		elif bmi > 20 and bmi <= 28:
			lfm = 0.9
		elif bmi > 28:
			lfm = 0.85
		bmr = kg * 24 * lfm
		print('kg')
		print(kg)
		print('lfm')
		print(lfm)
		print('bmr')
		print(bmr)
		calburnedperday = bmr * 1.55
		print('calburnedperday1')
		print(calburnedperday)
	elif gender_cor == 2:
		if bmi >= 14 and bmi <= 18:
			lfm = 1
		elif bmi > 18 and bmi <= 28:
			lfm = 0.95
		elif bmi > 28 and bmi <= 38:
			lfm = 0.9
		elif bmi > 38:
			lfm = 0.85
		bmr = kg * 0.9 * 24 * lfm
		calburnedperday = bmr * 1.1
		print('calburnedperday1')
		print(calburnedperday)
	if act_cor == 1:
		return calburnedperday
	elif act_cor == 2:
		calburnedperday = calburnedperday + (600 / 7)
		return calburnedperday
	elif act_cor == 3:
		calburnedperday = calburnedperday + 600
		print('calburnedperday2')
		print(calburnedperday)
		return calburnedperday




def calc_lim(weight1, goalweight1, height1, clicked_activity, clicked_gender, clicked_length):
	calburnedperday = 0
	weight = weight1.get()
	height = height1.get()
	goalweight = goalweight1.get()
	act_cor = 0
	gender_cor = 0
	length_cor = 0
	total_cal_burned = 0
	total_cal_needed_to_be_lost = 0
	cal_needed_to_be_lost_per_day = 0
	kg = weight * 0.453592
	meters_squared = (height * 2.54 * 0.01) * (height * 2.54 * 0.01)
	print('meters_squared')
	print(meters_squared)
	bmi = kg / meters_squared
	print('bmi')
	print(bmi)


	



	if clicked_activity.get() == 'Never':
		act_cor = 1
	elif clicked_activity.get() == 'Weekly':
		act_cor = 2
	elif clicked_activity.get() == 'Daily':
		act_cor = 3
	if clicked_gender.get() == 'Male':
		gender_cor = 1
	elif clicked_gender.get() == 'Female':
		gender_cor = 2
	if clicked_length.get() == '1 Month':
		length_cor = 1
	if clicked_length.get() == '3 Months':
		length_cor = 3
	if clicked_length.get() == '6 Months':
		length_cor = 6
	total_cal_burned = int(get_calburnedperday(bmi, kg, gender_cor, act_cor) or 0) * 30 * length_cor
	print('total_cal_burned')
	print(total_cal_burned)
	total_cal_needed_to_be_lost = (weight - goalweight) * 3500
	print('total_cal_needed_to_be_lost')
	print(total_cal_needed_to_be_lost)
	cal_needed_to_be_lost_per_day = total_cal_needed_to_be_lost / length_cor / 30
	print('cal_needed_to_be_lost_per_day')
	print(cal_needed_to_be_lost_per_day)
	cal_lim = int(get_calburnedperday(bmi, kg, gender_cor, act_cor) or 0) - cal_needed_to_be_lost_per_day
	print('calburnedperday')
	print(int(get_calburnedperday(bmi, kg, gender_cor, act_cor) or 0))
	print('cal_lim')
	print(cal_lim)



	if int(weight1.get()) == 0 or int(height1.get()) == 0 or int(goalweight1.get()) == 0 or act_cor == 0 or gender_cor == 0:
		screen1 = Toplevel(root)
		screen1.title('Warning')
		screen1.iconphoto(False, icon)
		screen1.geometry('400x220')
		screen1.resizable(0,0)
		screen1.config(bg = '#E46B27')
		Label(screen1, text='All fields required!',font=('Russo One', 20, 'bold'),pady=20,bg = '#E46B27' ).pack()
		Button(screen1, text='OK', command= lambda: delete(screen1)).pack()
	else:
		print(active_id)
		cursor = conn.cursor()
		cursor.execute("insert into goals (Userid, IsGoalSet, Height, Weight_, calorie_limit) values (?, 1, ?, ?, ?);",(active_id, height1.get(), weight1.get(), cal_lim))
		conn.commit()
		read(conn)
		Label(log_page, text = 'Daily Limit: ' + str(cal_lim), font = ('Russo One', 20, 'bold'), bg = '#E46B27').place(relx = 0.5, rely = 0.2, anchor=CENTER)
		raise_frame(log_page)

#DETAILS
main_label(setgoal_page)
Label(setgoal_page, text = 'Set Goal', font = ('Russo One', 20, 'bold'), bg = '#E46B27').place(relx = 0.5, rely = 0.3, anchor=CENTER)
Label(setgoal_page, text = 'Your Weight:', font = ('Russo One', 14, 'bold'), bg = '#E46B27').place(relx = 0.35, rely =0.4, anchor=CENTER)
Entry(setgoal_page, textvariable = weight1).place(relx = 0.35, rely = 0.45, anchor=CENTER)
Label(setgoal_page, text = 'Your Height:', font = ('Russo One', 14, 'bold'), bg = '#E46B27').place(relx = 0.35, rely = 0.55, anchor=CENTER)
Entry(setgoal_page, textvariable = height1).place(relx = 0.35, rely = 0.6, anchor=CENTER)
Label(setgoal_page, text = 'Your Goal Weight:', font = ('Russo One', 14, 'bold'), bg = '#E46B27').place(relx = 0.65, rely = 0.4, anchor=CENTER)
Entry(setgoal_page, textvariable = goalweight1).place(relx = 0.65, rely = 0.45, anchor=CENTER)
Label(setgoal_page, text = 'How often do you exercise?', font = ('Russo One', 14, 'bold'), bg = '#E46B27').place(relx = 0.65, rely = 0.55, anchor=CENTER)
Label(setgoal_page, text = 'Gender?', font = ('Russo One', 14, 'bold'), bg = '#E46B27').place(relx = 0.35, rely = 0.7, anchor=CENTER)
OptionMenu(setgoal_page, clicked_activity, "Never", "Weekly", "Daily" ).place(relx = 0.65, rely = 0.6, anchor=CENTER)
OptionMenu(setgoal_page, clicked_gender, "Male", "Female" ).place(relx = 0.35, rely = 0.75, anchor=CENTER)
Label(setgoal_page, text = 'When do you want to reach your goal?', font = ('Russo One', 14, 'bold'), bg = '#E46B27').place(relx = 0.65, rely = 0.7, anchor=CENTER)
OptionMenu(setgoal_page, clicked_length, "1 Month", "3 Months", "6 Months" ).place(relx = 0.65, rely = 0.75, anchor=CENTER)
Button(setgoal_page, text = 'Go!', width = 10, height = 1, command=lambda: calc_lim(weight1, goalweight1, height1, clicked_activity, clicked_gender, clicked_length)).place(relx = 0.65, rely = 0.85, anchor=CENTER)
place_back_button(setgoal_page, login_page)


#LOG PAGE 
#DETAILS
main_label(log_page)
you_have_eaten_label = Label(setgoal_page, text = 'You have eaten ' + str(cal_lim) + ' calories today', font = ('Russo One', 20, 'bold'), bg = '#E46B27')
you_can_eat_label = Label(setgoal_page, text = 'You can eat ' + str(cal_lim) + ' more calories today', font = ('Russo One', 20, 'bold'), bg = '#E46B27')


Button(log_page, text = 'Log', width = 20, height = 5, command=lambda: raise_frame(logmanually_page)).place(relx = 0.25, rely = 0.35, anchor=CENTER)
place_back_button(log_page, setgoal_page)
#LOG MANUALLY PAGE
food_name = StringVar()
calorie_amount = IntVar()
log_count = 0

#LOG FUNCTIONS
def log(calorie_amount, food_name):
	if log_count == 0:
		cursor = conn.cursor()
		cursor.execute("insert into user_activity (Userid, Amount1) values (?, ?);",(active_id, calorie_amount.get()))
		conn.commit()
		log_count += 1
	elif log_count == 1:
		cursor = conn.cursor()
		cursor.execute(
			"update user_activity set Amount2 = ? where Userid = ? and Date1 = ?;",(calorie_amount.get(), active_id, today_date)
				)
		conn.commit()
		log_count += 1
	elif log_count == 2:
		cursor = conn.cursor()
		cursor.execute(
			"update user_activity set Amount3 = ? where Userid = ? and Date1 = ?;",(calorie_amount.get(), active_id, today_date)
			)
		conn.commit()
		log_count = log_count + 1
	elif log_count == 3:
		cursor = conn.cursor()
		cursor.execute(
			"update user_activity set Amount4 = ? where Userid = ? and Date1 = ?;",(calorie_amount.get(), active_id, today_date)
			)
		conn.commit()
		log_count += 1
	elif log_count == 4:
		cursor = conn.cursor()
		cursor.execute(
			"update user_activity set Amount5 = ? where Userid = ? and Date1 = ?;",(calorie_amount.get(), active_id, today_date)
			)
		conn.commit()
		log_count += 1
	else:
		screen1 = Toplevel(root)
		screen1.title('Warning')
		screen1.iconphoto(False, icon)
		screen1.geometry('400x220')
		screen1.resizable(0,0)
		screen1.config(bg = '#E46B27')
		Label(screen1, text='Maximum 5 logs per day!',font=('Russo One', 20, 'bold'),pady=20,bg = '#E46B27' ).pack()
		Button(screen1, text='OK', command= lambda: delete(screen1)).pack()

	now = datetime.now()
	formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
	cursor = conn.cursor()
	cursor.execute("select * from user_activity where Date1 = ?;",(formatted_date))
	row = cursor.fetchone()


#DETAILS
main_label(logmanually_page)
Label(logmanually_page, text = 'Food Name', font = ('Russo One', 20, 'bold'), bg = '#E46B27').place(relx = 0.5, rely = 0.3, anchor=CENTER)
Entry(logmanually_page, textvariable = food_name).place(relx = 0.5, rely = 0.35, anchor=CENTER)
Label(logmanually_page, text = 'Amount of calories', font = ('Russo One', 20, 'bold'), bg = '#E46B27').place(relx = 0.5, rely = 0.45, anchor=CENTER)
Entry(logmanually_page, textvariable = calorie_amount).place(relx = 0.5, rely = 0.5, anchor=CENTER)
Button(logmanually_page, text = 'Go!', width = 10, height = 1).place(relx = 0.5, rely = 0.6, anchor=CENTER)
place_back_button(logmanually_page, log_page)

raise_frame(login_page)

root.mainloop()
conn.close()
