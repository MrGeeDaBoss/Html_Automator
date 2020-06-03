
class Automate():
    def __init__(self, MainFile, filetype):
        self.filetype = filetype
        self.MainFile = MainFile
         
    def paste(self, text):
        with open(self.MainFile+"/Base.html", 'w') as f:
            f.write(text)
