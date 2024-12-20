class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

def find_oldest_cat(cats):
    oldest_cat = cats[0]
    for cat in cats:
        if cat.age > oldest_cat.age:
            oldest_cat=cat
    return oldest_cat

cat1 = Cat("Tom", 5)
cat2 = Cat("Jerry", 7)

cats = [cat1, cat2]

oldest_cat = find_oldest_cat(cats)

print(f"the oldest cat is {oldest_cat.name}")
