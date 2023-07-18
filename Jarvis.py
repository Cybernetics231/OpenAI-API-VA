import os 
import openai
import speech_recognition as sr
import random
import subprocess
openai.api_key = "INSERT YOUR OWN API KEY HERE"




import pyttsx3
engine = pyttsx3.init() # object creation

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
#print (rate)                        #printing current voice rate
engine.setProperty('rate', 210)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
#print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female






r = sr.Recognizer()

##First initialize command





def listen():
    with sr.Microphone() as source:
        os.system('cls') ##Clears output
        print("Say something!")
        audio = r.adjust_for_ambient_noise(source)
        captured_audio = r.listen(source)
        
        ##Speech Check
    
    try:

        print("Google Speech Recognition thinks you said " + r.recognize_google(captured_audio))


    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand captured_audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    
    return captured_audio


def create_file(pyortxt):
    
    name_response_list = ["What do we feel like naming this? Use your head for once and think of something clever", "What are we naming this thing? Oh god, I shouldn't have asked you that question.", "What do we want to name this? Hurry up I don't have all day","choose a name for the file. Come on schnell I got places to be", "Pick a name for the file. You are capable of doing that aren't you?"]
    namekey = random.randint(0,3)
    
    
    engine.say(name_response_list[namekey])
    engine.runAndWait()
    engine.stop()
    
    name = r.recognize_google(listen())
    
    name.replace(" ", "")
    
    if pyortxt == 1:
        print(f"File generation successful: {name}.txt")
        
        
        file_creation = open(f"{name}.txt", "x")
        
        
    if pyortxt == 0:
        
        print(f"File generation successful: {name}.py")
        file_creation = open(f"{name}.py", "x")
    
    
    return name
        
        
def consult_gpt_program(file_name):
    engine.say("What do you want this program to do?")
    engine.runAndWait()
    engine.stop()
    
    code_request = r.recognize_google(listen())
    

    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": code_request.lower() + ". write it in python, but just give me the code, do not put any comments"}])

    #print(chat_completion.choices[0].message.content)
    
    f = open(f"{file_name}.py", "a")
    f.write(chat_completion.choices[0].message.content)
    f.close()
    
    
    finished_response_list = ["The dark deed you requested is done sir", "Job's done, now where is my pay?", "wait what was I supposed to do again? Just kidding it is done", "Finished. That'll be 300 dollars.", "Maybe you should try doing this yourself, anyways its done"]
    finished_response_key = random.randint(0,4)
    engine.say(finished_response_list[finished_response_key])
    engine.runAndWait()
    engine.stop()
    
    return None


def consult_gpt_write(file_name):
    
    engine.say("Ok you lazy bastard, what do you want me to write?")
    engine.runAndWait()
    engine.stop()
    
    code_request = r.recognize_google(listen())
    

    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": code_request.lower()}])

    #print(chat_completion.choices[0].message.content)
    
    f = open(f"{file_name}.txt", "a")
    f.write(chat_completion.choices[0].message.content)
    f.close()
    
    
    finished_response_list = ["The dark deed you requested is done sir", "Job's done", "wait what was I supposed to do again? Just kidding it is done", "Finished", "Maybe you should try doing this yourself, anyways its done"]
    finished_response_key = random.randint(0,4)
    engine.say(finished_response_list[finished_response_key])
    engine.runAndWait()
    engine.stop()
    
    
    return None
        
        
        
        
        
def write_check():
    engine.say("Do you want me to write something in the file?")
    engine.runAndWait()
    engine.stop()
                
    write_or_no = r.recognize_google(listen())
    
    
    if "yes" in write_or_no.lower():
        return 0
    
    else:
        engine.say("Alright then")
        engine.runAndWait()
        engine.stop()
        return 1
    



def greeting():
    
    
    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Greet me but do it sarcastically. Do not refer to yourself. Use no more than 20 words"}])
    
    return chat_completion.choices[0].message.content
        
        
        
        
        
        
while(True):

    print("AI STARTED")

    greeting_identifier = r.recognize_google(listen()) ###Provisional variable declaration to lowercase the greeting_identifier. 

    print(greeting_identifier.lower())
    #opening_word_list = ["hey jarvis", "jarvis can you", "jarvis i need", "jarvis will you"] ##Small list of possible greeting phrases

    if "jarvis" in greeting_identifier.lower():
        gpt_response=greeting()
        
        greeting_list = [gpt_response, "Oh no it's you again, what do you want?", "How may I be of assistance?", "sure let me just drop everything to help you out, what do you want?", "What can the magnificent jarvis do for you?", "for the love of god I hope this is your last request, what do you want?", "What do you want this time?"]
        greeting_key = random.randint(0,6)
        
        engine.say(greeting_list[greeting_key])
        engine.runAndWait()
        engine.stop()
        
        
        print("Speak")
        
        
        
        ##Listen for 2nd command
    
        command = r.recognize_google(listen())
        print("You said:" + command.lower())
        print("Thinking")
        
        
        
        
        
        
        

        
        create_file_list = ["create a file", "need a file", "generate a file", "create me a file", "programming file", "write me a file", "generate me a file"]
        
        
        if any(word in command.lower() for word in create_file_list):
            
            
            engine.say("What kind of format? Python or Text?")
            engine.runAndWait()
            engine.stop()
            
            
            
            format = r.recognize_google(listen())
            
            print("You said:" + format.lower())
            print("Thinking")
            
            if "text" in format:
                print("text file")
                text_file_name = create_file(1)
                engine.say("Text File Created")
                engine.runAndWait()
                engine.stop()
                checking = write_check()
                
                if checking == 0:
                    consult_gpt_write(text_file_name)
                else:
                    pass
                
                
            if "python" in format:
                print("python file")
                python_file_name = create_file(0)
                engine.say(f"Python File Created")
                engine.runAndWait()
                engine.stop()
                checking = write_check()
                
                if checking == 0:
                    consult_gpt_program(python_file_name)
                else:
                    pass
                    

            
        create_program_list =["need a programming file", "need a program", "create me a program", "make me a program", "need a python file", "need a python program", "create a program", "generate a program"]            
        if any(word in command.lower() for word in create_program_list):
            print("python file")
            python_file_name = create_file(0)
            engine.say(f"Python File Created")
            engine.runAndWait()
            engine.stop()
            consult_gpt_program(python_file_name)
            

        
            
            

        
        
        
        
        
        
        
        
        

        
        launch_cad_list = ["open autocad", "open p.3d", "open cad", "launch autocad", "launch p.3d", "launch cad", "open up cad", "open up autocad", "open up p.3d"]
        if any(word in command.lower() for word in launch_cad_list ):
            subprocess.call(['C:\\Users\\pacle\\Desktop\\PLANT3DBATCH.exe'])
            engine.say("launching auto cad")
            engine.runAndWait()
            engine.stop()

        
        if command.lower() == "exit":
            break
        
        
        
        
        
        
        
        Misc = ["Misc", "what", "tell", "teach", "can"]
        
        ###GENERAL INQUIRY###
        ###USE OPENAI API###
        if any(word in command.lower() for word in Misc ):
            chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": command.lower()}])

            print(chat_completion.choices[0].message.content)
                
            engine.say(chat_completion.choices[0].message.content) ####Code to generate text to speech
            engine.runAndWait()
            engine.stop()

    
    
    
    
    
    
    
    
 
    
    
    
    





"""
chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": command.lower()}])

# print the chat completion
print(chat_completion.choices[0].message.content)




#engine.say("Hello World!")
engine.say(chat_completion.choices[0].message.content)
engine.runAndWait()
engine.stop()
"""

