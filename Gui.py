import tkinter as tk
from PIL import Image,ImageTk
from translate import Translator
import speech_recognition as sr
import pyaudio
import tkinter as tk
from PIL import Image,ImageTk
import threading as td

#---------------------VARIABLES------------------------
langlist = ["en-US","te-IN","ta-IN","hi-IN"]
dixnary = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','when', 'chair', 'you', 'waves','confident', 'word', 'beautiful', 'we', 'work','what time','agree', 'close', 'accident', 'which', 'rich', 'above', 'change', 'this', 'knife', 'accept', 'three', 'seven', 'j', 'us', 'q', 't', 'your', 'poor', 'among', 'back', 'nice', 'husband', 'thin', 'children', 'jealous', 'country', 'happy', 'eight', 'hour', 'five', 'amount', 'how big', 'investment', 'two', 'thirteen', 'book', 'h', 'hospital', 'horizontal', 'action', 'chess', 's', 'b', 'those', 'science', 'cinema', 'chemistry', 'who', 'how many', 'bird', 'l', 'o', 'call', 'busy', 'afternoon', 'cat', 'y', 'karate', 'e', 'apple', 'chennai', 'hungry', 'history', 'whose', 'p', 'can', 'inauguaration', 'ten', 'yourself', 'my', 'loud', 'dance', 'big', 'increase', 'know', 'animal', 'at', 'job', 'hope', 'f', 'then', 'ugly', 'house', 'cough', 'illiterate', 'cry', 'sad', 'x', 'z', 'between', 'bedroom', 'what', 'four', 'n', 'clock', 'expensive', 'hut', 'g', 'hours', 'hotel', 'hyderabad', 'm', 'c', 'divide', 'kilogram', 'holiday', 'angry', 'v', 'about', 'brother', 'junior', 'six', 'deaf', 'nine', 'clean', 'idly', 'a', 'bad', 'banana', 'after', 'd', 'parent', 'bangalore', 'subtract', 'car', 'how much', 'bathroom', 'carry', 'house fly', 'home', 'break', 'boy', 'cold', 'quiet', 'hole', 'mean', 'where', 'hindi', 'kilograms', 'i', 'dancing', 'horse', 'cash', 'now', 'surname', 'why', 'all', 'april', 'again', 'yesterday', 'time', 'one', 'eleven', 'twelve', 'herself', 'cheap', 'love', 'alone', 'hurt', 'blind', 'flat', 'ball', 'tomorrow', 'like', 'k', 'r', 'august', 'agriculture', 'u', 'age', 'advantage', 'multiply', 'hop', 'act', 'thick','loud','quiet','happy','sad','beautiful','ugly','deaf','blind','nice','rich','poor','thick','thin','expensive','cheap','flat','curved',
'male','tight','loose','high','low','soft','deep','shallow','dirty','strong','dead','alive','heavy','light','long','short','tall','wide','big','small','slow','fast','hot','warm','cool','new',
'brown','dog','fox','handicapped','hardworking','hate','he','head','hear','hearing','health','heart','heavier','helicopter','heir','hen','jump','over','thankyou','wait','zoo','walk','want','warm','warn','washbasin','wastage','warning','waste','watch','water','watermelon','weak','wedding','week','weigh','weight','welcome','wet','west','whale',
'what','which','where','whistle','white','wholesale','wife','will','win','wish','name','won','without','wool','woman','word','world','wound','write','wrong','x-ray',
'x','y','z','yellow','your','yourself','z','zebra crossing','zebra','zebras','zone']


textout = ''
imagesL = []
counter = -1
app = tk.Tk()
app.geometry("610x600")
app.title("Tkinter images")

langcounter = 0
langbuttonlabel = langlist[0]
frameS = []

gifFrameCnt = -1

delay = 0
#--------------------------------------------------------------

#-------------------FUNCTIONS----------------------------------
def getgif():

    global frameS,delay

    gif = Image.open(imagesL[counter])

    nf = gif.n_frames

    for r in range(0,nf):
        gif.seek(r)
        frameS.append(gif.copy())
    
    delay = gif.info['duration']
    fwdgif()


def fwdgif():

    global gifFrameCnt, cf

    if gifFrameCnt >= len(frameS):
        gifFrameCnt = -1
        fwdgif()
    else:
        gifFrameCnt +=1

    cf = ImageTk.PhotoImage(frameS[gifFrameCnt])
    imagelabel.config(image=cf)
    app.after(delay,fwdgif)



def srout():

    global textout
    try:
        listener = sr.Recognizer()
        with sr.Microphone() as ip_src:
            print("listening...")
            vi = listener.listen(ip_src,phrase_time_limit=3)
            text = listener.recognize_google(vi,language=langlist[langcounter])
            
        if langlist[langcounter] == "en-US":
            textout = text
        else:
            tl = Translator(to_lang="en-us",from_lang=langlist[langcounter])
            vague = tl.translate(text)

            textout = vague
    except:
        print(Exception)
    
    



def imshow():
    global counter
    global textout
    global imagesL
    global dixnary
    
    blank = 'images/blank.jpg'

    words = textout.split(" ")

    imagesL.clear()

    for i in range(len(words)): 
        if words[i].lower() in dixnary:
            link = 'gif/'+words[i].lower()+'.gif'
            imagesL.append(link)
        else:
            for j in range(len(words[i])):
                link = 'alpha/'+words[i][j].upper()+'.jpg'
                image = ImageTk.PhotoImage(Image.open(link).resize((600,350)))
                imagesL.append(link)

        image = ImageTk.PhotoImage(Image.open(blank).resize((600,350)))
        imagesL.append(blank)
    
    print(imagesL)

def previmage():
    global counter
    if counter < len(imagesL):
        counter -= 1
    else:
        counter = 0
    
    letter = imagesL[counter][-3:]
    
    if letter == "gif":
        getgif()
    else :
        frameS.clear()
        im = ImageTk.PhotoImage(Image.open(imagesL[counter]).resize((600,350)))
        imagelabel.configure(image=im)
        imagelabel.image = im


def nextimage():
    global counter
    if counter < len(imagesL):
        counter += 1
    else:
        counter = 0
    
    letter = imagesL[counter][-3:]
    let2 = imagesL[counter+1][-3:]

    if letter == "gif":
        getgif()
    else :
        frameS.clear()
        im = ImageTk.PhotoImage(Image.open(imagesL[counter]).resize((400,300)))
        imagelabel.configure(image=im)
        imagelabel.image = im

def changelang():
    global langcounter
    if langcounter < len(langlist):
        langcounter += 1
    else:
        langcounter = 0

    langbuttonlabel = langlist[langcounter]
    langlabel.config(text=langlist[langcounter])


#------------------------------GUI----------------------------------------->

imagelabel = tk.Label(app)
infolabel = tk.Label(app,text=textout,font="Helvetica,15")
speechbutton = tk.Button(app,text="speech",bg="#4681f4",fg="white",font="Helvetica,15",width=20,height=2,command=srout)
loadbutton = tk.Button(app,text="load",width=20,height=2,bg="#5783db",font="Helvetica,15",fg="white",command=imshow)
nextimagebutton = tk.Button(app,text="next image",width=20,height=2,font="Helvetica,15",bg="#4681f4",fg="white",command=nextimage)
backimagebutton = tk.Button(app,text="previous image",width=20,height=2,bg="#5783db",font="Helvetica,15",fg="white",command= previmage)
#langbutton = tk.Button(app,text="changelang",width=20,height=2,bg="orange",fg="white",command=changelang,font="Helvetica,15")
#langlabel = tk.Label(app,text=langlist[langcounter],width=20,height=2,bg="orange",fg="white",font="Helvetica,15")

imagelabel.place(x=0,y=10)
infolabel.place(x=65,y=10)
speechbutton.place(x=115,y=10)
loadbutton.place(x=165,y= 10)
nextimagebutton.place(x=215,y=10)
backimagebutton.place(x=265,y=10)
#langbutton.place(x=315,y=10)
#langlabel.place(x=315,y=50)

imagelabel.pack()
infolabel.pack()
speechbutton.pack(padx=3,pady=3)
loadbutton.pack(pady=3,padx=3)
nextimagebutton.pack(pady=3,padx=3)
backimagebutton.pack(padx=3,pady=3)
#langbutton.pack(padx=3,pady=3)
#langlabel.pack(padx=3,pady=3)

td.Thread(target=getgif).start()
app.mainloop()