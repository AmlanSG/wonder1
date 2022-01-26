person1_information = {'city': 'San Francisco','name': 'Sam3', 'name': 'Sam1','name': 'Sam2', "food": "shrimps"}
for key, val in person1_information.items():
    print("key is: %s" % key)
    print("value is: %s" % val)
    print("###########################")

knowledge = {"Frank": {"Perl","Ruby"}, "Monica": {"C", "C++"}}
knowledge2 = {"Guido": {"Python","Scala"}, "Frank": {"Perl", "Python"},"Ganga": {"ABC", "XYZ","MNO"}}
knowledge.update(knowledge2)
print knowledge

