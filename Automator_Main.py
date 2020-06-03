import os
import os.path
import Automator_Class


foldername = "Scripts"
html_base = """
    <!DOCTYPE html>\n
    <html>\n
    <head>\n
      <title>\n
         The Monk Diamond Discovery\n
      </title>\n
    </head>\n
    <body>\n
      <p>This is a test webpage, I will use it to copy the html tags, cause I'm
      too lazy to code it myself.</p>\n
    </body>\n
    </html>
"""

def create_folder():
    if os.path.exists(foldername):
        print("file exists")
        return
    else:
        print("file is created")
        os.mkdir(foldername)

create_folder()

def main():
    filechoice = input("Choose the type of file base you want to initialize. html")
    auto = Automator_Class.Automate(foldername, filechoice)
    auto.paste(html_base)

main()
    

