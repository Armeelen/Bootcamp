def make_shirt(size="large",text="I love Python"):
    size=input(str("Please input your size:"))
    if size=="Large":
        print("The size of the shirt is",size, "and the text is",text)
    elif size=="Medium":
        text="I love C++"
        print("The size of the shirt is",size, "and the text is", text)
    else:
        print("The size of the shirt is",size, "and the text is I love Javascripts")


make_shirt()