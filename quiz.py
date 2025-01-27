from tkinter import *

# define question dictionary
question = {
	"1 Which animal is known as the 'Ship of the Desert?": ['Camel', 'Giraffee', 'Leopard', 'Tortoise'],
	"2  How many days are there in a week?": ['2', '7', '5'],
	"3 Baby frog is known as.......": ['Cub', 'Tadpole', 'joey', 'kit'],
        "4 Name the component of blood that fights infection?": ['WBC','RBC','Plasma'],
        "5 What is the capital city of France?": ['Italy','Beijing','France'],
        "6 In which year did World War II end?": ['1945','1947','1942'],
        "7 Which country is known as the Land of the Rising Sun?": ['China','USA','UK','Japan'],
        "8 What is the smallest prime number?": ['3','1','2','4'],
        "9 What is the largest mammal in the world?": ['Dolphin','Elephant','Blue whale','Lion'],
        "10 Who is the author of “Harry Potter” series?": ['Harper Lee','Vincent van Gogh','Shakespeare','J.K Rowling']
                                                       
}
# answer list
ans = ['Camel', '7', 'Tadpole','WBC','France','1945','Japan','2','Blue Whale','J.K. Rowling']

current_question = 0


def start_quiz():
	start_button.forget()
	next_button.pack()
	next_question()


def next_question():
	global current_question
	if current_question < len(question):
		check_ans()
		user_ans.set('None')
		c_question = list(question.keys())[current_question]
		clear_frame()
		Label(f1, text=f"Question : {c_question}", padx=15,
			font="calibre 12 normal").pack(anchor=NW)
		for option in question[c_question]:
			Radiobutton(f1, text=option, variable=user_ans,
						value=option, padx=28).pack(anchor=NW)
		current_question += 1
	else:
		next_button.forget()
		check_ans()
		clear_frame()
		output = f"Your Score is {user_score.get()} out of {len(question)}"
		Label(f1, text=output, font="calibre 25 bold").pack()
		Label(f1, text="Thanks for Participating",
			font="calibre 18 bold").pack()


def check_ans():
	temp_ans = user_ans.get()
	if temp_ans != 'None' and temp_ans == ans[current_question-1]:
		user_score.set(user_score.get()+1)


def clear_frame():
	for widget in f1.winfo_children():
		widget.destroy()


if __name__ == "__main__":
	root = Tk()
	root.title("TRICKY QUIZ APP")
	root.geometry("850x520")
	root.minsize(800, 400)

	user_ans = StringVar()
	user_ans.set('None')
	user_score = IntVar()
	user_score.set(0)

	Label(root, text="Quiz App", 
		font="calibre 40 bold",
		relief=SUNKEN, background="cyan", 
		padx=10, pady=9).pack()
	Label(root, text="", font="calibre 10 bold").pack()
	start_button = Button(root, 
						text="Start Quiz",
						command=start_quiz, 
						font="calibre 17  bold")
	start_button.pack()

	f1 = Frame(root)
	f1.pack(side=TOP, fill=X)

	next_button = Button(root, text="Next Question",
						command=next_question, 
						font="calibre 17 bold")

	root.mainloop()
