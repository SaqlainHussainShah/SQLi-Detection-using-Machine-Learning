import tkinter as tk
from tkinter import Text, Tk





######## Start of prediction




import keras
from keras.models import load_model
import pickle

mymodel = load_model('my_model.h5')
myvectorizer = pickle.load(open("vectorizer", 'rb'))







def clean_data(input_val):    

    input_val=input_val.replace('\n', '')
    input_val=input_val.replace('%20', ' ')
    input_val=input_val.replace('=', ' = ')
    input_val=input_val.replace('((', ' (( ')
    input_val=input_val.replace('))', ' )) ')
    input_val=input_val.replace('(', ' ( ')
    input_val=input_val.replace(')', ' ) ')
    input_val=input_val.replace('1 ', 'numeric')
    input_val=input_val.replace(' 1', 'numeric')
    input_val=input_val.replace("'1 ", "'numeric ")
    input_val=input_val.replace(" 1'", " numeric'")
    input_val=input_val.replace('1,', 'numeric,')
    input_val=input_val.replace(" 2 ", " numeric ")
    input_val=input_val.replace(' 3 ', ' numeric ')
    input_val=input_val.replace(' 3--', ' numeric--')
    input_val=input_val.replace(" 4 ", ' numeric ')
    input_val=input_val.replace(" 5 ", ' numeric ')
    input_val=input_val.replace(' 6 ', ' numeric ')
    input_val=input_val.replace(" 7 ", ' numeric ')
    input_val=input_val.replace(" 8 ", ' numeric ')
    input_val=input_val.replace('1234', ' numeric ')
    input_val=input_val.replace("22", ' numeric ')
    input_val=input_val.replace(" 8 ", ' numeric ')
    input_val=input_val.replace(" 200 ", ' numeric ')
    input_val=input_val.replace("23 ", ' numeric ')
    input_val=input_val.replace('"1', '"numeric')
    input_val=input_val.replace('1"', '"numeric')
    input_val=input_val.replace("7659", 'numeric')
    input_val=input_val.replace(" 37 ", ' numeric ')
    input_val=input_val.replace(" 45 ", ' numeric ')
    
    return input_val


def predict_sqli_attack(userData):
        


        input_val=userData



        input_val=clean_data(input_val)
        input_val=[input_val]



        input_val=myvectorizer.transform(input_val).toarray()

        result=mymodel.predict(input_val)


        if result>0.5:
                message="ALERT :: This can be SQL injection"
                w = tk.Message(window, text=message , width=400)
                w.pack()
        elif result<=0.5:
                message="It seems to be safe"
                w = tk.Message(window, text=message,   width=400)
                w.pack()









### end of prediction



####### start of gui




def OnClick():
        userData = text.get('1.0', tk.END)
        predict_sqli_attack(userData)



window = tk.Tk()

window.geometry("400x400")

label = tk.Label(text="Enter String to classify")
# entry=tk.Entry(fg="black", bg="silver", width=50)
button=tk.Button(text="Check", command=OnClick)
text = Text(window, height=20, width=40)

label.pack()
# entry.pack()
text.pack()
button.pack()


window.mainloop()




####### END