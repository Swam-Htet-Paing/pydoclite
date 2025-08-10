import readline

def ascii_intro():
    chars = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']
    with open("pydoclite.py", "r") as f:
        content = f.read()
        print(type(content))
        print(content)


#keyword documentation class
class kwDoc:
    def __init__(self, name, description, example):
        self.name = name
        self.description = description
        self.example = example
    def printContent(self):
        print(f"\n{self.name}: {self.description}\n\nexample: \n\n{self.example}\n")
        
        
#main dictionary for storing content, all keywords of functions, objects are listed here as kwDoc() objects
#will be used in main for searching up answers
docs = {
    "print": kwDoc("print, a function", "prints something on the screen", "print('Hello world!')"),
    "range": kwDoc("range, a function", "generates a sequence of numbers", "for i in range(5): print(i)"),
    "len": kwDoc("len, a function", "returns number of items of an object (array, string etc.)", "a = [1,2,3]\nlen(a) #returns 3"),
    "while": kwDoc("while, a control flow statement","used for looping until a sepcified condition is False","i = 0\nwhile i<5:\n   i++ #exits when i is 5")
}


#auto complete function part, uses readline
def complete(text, state):
    #looks up matches whenever tab is pressed
    options = [kw for kw in docs if text in kw]
    if state < len(options):
        return options[state]
    else:
        return None
readline.set_completer(complete)
readline.parse_and_bind("tab: complete")


#this is the main funcion (duh)
def main():
    ascii_intro()
    print("type 'quit' to exit, press tab for auto completion")
    while True:
        text = input("Enter a keyword, class or a function name: ").strip()
        
        if text == "quit":
            print("Bye bye!")
            break
        
        content = docs.get(text)
        if content:
            content.printContent()
        else:
            print(f"No documentation found for {text}")
        

if __name__ == "__main__":
    main()
