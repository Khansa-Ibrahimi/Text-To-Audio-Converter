from tkinter import filedialog, messagebox
from tkinter import *
#library to process pdfs
import PyPDF2
#library to process audio
import pyttsx3


#global variable to save the filepath
global filename
filename = None

def ask_file():
    '''Ask the user to select the source file. Informs the user that the file is selected.'''
    global filename
    filename = filedialog.askopenfilename()
    if filename:
        messagebox.showinfo('File Selected!', 'Choose what you want to do with the file.')
   

def make_audio_file():
    '''Goes through each page of the pdf and extracts the text. Then calls the save function'''
    #Check the selected file is a pdf
    if filename.endswith('.pdf'):
        #Initialize a PdfReader object to read the file
        pdf_reader = PyPDF2.PdfReader(filename)
        #using the .pages attribute to get the number of pages
        pdf_pages = len(pdf_reader.pages)
        print(pdf_pages)
        #going through each page of the pdf
        for num in range(0,pdf_pages):
            #the current page is stored in page variable
            page = pdf_reader.pages[num]
            #the text is extracted
            text = page.extract_text()
            #save the audio file
            save_audio_file(text, filename)
    #Sends a warning message if the select file is different from PDF file type
    else:
        messagebox.showwarning("Invalid File Type!", "The file should be a PDF.")
        
def save_audio_file(media, filename):
    '''Saves the audio file and sends an acknowledgement message to the user'''
    #Initialize the pyttsx3 text-to-speech engine
    player = pyttsx3.init()
    #Save the extracted text as an audio file with the same name as the source file
    player.save_to_file(media,f"{filename}.mp3")
    #Run the text-to-speech conversion
    player.runAndWait()
    #message box to show the user that the file has been saved
    messagebox.showinfo("DONE!",  "Your file has been saved in the same location as your source file.")

def make_text_file():
    """Implement a funtion to make a text file from a audio file"""

#setting up the initial screen
window = Tk()
window.title("Your AudioBook Maker")
window.config(padx=50, pady=50)

#Upload button 
upload_img = PhotoImage(file="images/upload.png")
#Has the function to open the dialog box to select the file
upload_button = Button(image=upload_img, highlightthickness=0, command=ask_file)
upload_button.grid(row=1, column=0, columnspan=2, pady=50)

#Convert to text-based file button
book_img = PhotoImage(file="images/book.png")
book_button = Button(image=book_img, highlightthickness=0, padx=20)
book_button.grid(row=2, column=0)

#Convert to a audio file button
headphone_image = PhotoImage(file="images/headphones.png")
headphone_button = Button(image=headphone_image, highlightthickness=0, padx=20, command=make_audio_file)
headphone_button.grid(row=2, column=1)

window.mainloop()





