magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians(names):
    for name in names:
        print(names)

def make_great(names):
    for i in range(len(names)): 
        names[i] = names[i] + ",The Great"

make_great(magician_names)
show_magicians(magician_names)

