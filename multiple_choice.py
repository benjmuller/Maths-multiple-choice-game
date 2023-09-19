"""
Created on Tue Sep 19 11:11:27 2023

@author: benmu
"""

from tkinter import *
from pylab import random as r
from sys import *

class window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.question = None
        self.text = None
        self.correct_answer(None)
        self.A_Button = None
        self.B_Button = None
        self.C_Button = None
        self.D_Button = None
        self.questions()
        self.temp = self.tempQ()
        self.buttons()
        self.place_question()
        self.master = master
        self.init_window()
        
    def init_window(self):
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)
        
######################################################### storing current Q&A's        
    def questions(self):
        information_list = []
        Questions = self.Get_Question('Question.txt')
        Answers = self.Get_Answer('Answer.txt')
        Possible_Answers = self.possible_answers('PossibleAnswers.txt')
        current_questions = self.choose_question(Questions)
        return [Questions,Answers,Possible_Answers,current_questions]
    
    def tempQ(self):
        self.temp = self.questions()
        return self.temp

######################################################## answering buttons       
    def buttons(self):
        if self.A_Button:
            self.A_Button.destroy()
        self.A_Button = Button(self, text=str(((self.temp[2])[(self.temp[3])][0])), command=self.Answer_A)
        self.A_Button.place(relx=0.5, rely=0.5, anchor=CENTER)
        if self.B_Button:
            self.B_Button.destroy()
        self.B_Button = Button(self, text=str(((self.temp[2])[(self.temp[3])][1])), command=self.Answer_B)
        self.B_Button.place(relx=0.5, rely=0.6, anchor=CENTER)
        if self.C_Button:
            self.C_Button.destroy()
        self.C_Button = Button(self, text=str(((self.temp[2])[(self.temp[3])][2])), command=self.Answer_C)
        self.C_Button.place(relx=0.5, rely=0.7, anchor=CENTER)
        if self.D_Button:
            self.D_Button.destroy()
        self.D_Button = Button(self, text=str(((self.temp[2])[(self.temp[3])][3])), command=self.Answer_D)
        self.D_Button.place(relx=0.5, rely=0.8, anchor=CENTER)
        Next_Question = Button(self, text='Next Question', command=self.new_question)
        Next_Question.place(relx=0.5, rely=0.4, anchor=CENTER)
        
######################################################## placing question on gui
    def place_question(self):
        if self.question:
            self.question.destroy()
        self.question = Label(self, text=(self.temp[0])[(self.temp[3])],wraplengt=350)
        self.question.pack()
        
######################################################## new question
    def new_question(self):
        self.tempQ()
        self.correct_answer(None)
        self.place_question()
        self.buttons()

######################################################## getting Q&A from files   
    def Get_Question(self,file):
        question_list = []
        question = open(file,encoding='utf-8')
        for line in question:
            question_list.append(line.strip('\n'))
        return question_list
            
    def Get_Answer(self,file):
        answer_list = []
        answer = open(file,encoding='utf-8')
        for line in answer:
            answer_list.append(line.strip('\n'))
        return answer_list        

######################################################## generating random question
    def choose_question(self,file):
        return int(r() * len(file))

######################################################## creating list of possible answers    
    def possible_answers(self,file):
        answers_list = []
        answers = open(file,encoding='utf-8')
        for line in answers:
            answers_list.append((line.strip('\n').split('&')))
        return answers_list

######################################################## checking answer
    def check_answer(self,answer):
        if answer == (self.temp[1])[self.temp[3]]:
            return True
        else:
            return False
        
######################################################## display answer       
    def correct_answer(self,result):
        if self.text:
            self.text.destroy()
        self.text = Label(self, text=result)
        self.text.pack()
 
######################################################## Answers
    def Answer_A(self):
        result = self.check_answer('A')
        if result == True:
            self.correct_answer('Correct')
        else:
            self.correct_answer('Incorrect')
    
    def Answer_B(self):
        result = self.check_answer('B')
        if result == True:
            self.correct_answer('Correct')
        else:
            self.correct_answer('Incorrect')
    
    def Answer_C(self):
        result = self.check_answer('C')
        if result == True:
            self.correct_answer('Correct')
        else:
            self.correct_answer('Incorrect')
    
    def Answer_D(self):
        result = self.check_answer('D')
        if result == True:
            self.correct_answer('Correct')
        else:
            self.correct_answer('Incorrect')
        
########################################################## Running window    

root = Tk()
root.geometry("400x300")

app = window(root)

root.mainloop()