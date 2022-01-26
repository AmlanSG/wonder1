capitals = {"Springfield":"Illinois", "Augusta":"Maine", "Boston":
"Massachusetts", "Lansing":"Michigan", "Albany":"New York",
"Olympia":"Washington", "Toronto":"Ontario"}
# Key : Value
var1 = capitals.pop("Kolkata")
print var1
print type(var1)
var = capitals.popitem()
print var
print type(var)
print capitals

proj_language = {"proj1":"Python", "proj2":"Perl", "proj3":"Java"}
print proj_language["proj1"]
print proj_language.get("proj2")
print proj_language.get("proj4")
print proj_language.get("proj4", "C++")

person1_information = {'city': 'San Francisco', 'name': 'Sam', "food": "shrimps"}
for k, v in person1_information.items():
    print("key is: %s" % k)
    print("value is: %s" % v)
    print("###########################")

    trainings = {"course1": {"title": "Python Training Course for Beginners",
                             "location": "Frankfurt",
                             "trainer": "Steve G. Snake"},
                 "course2": {"title": "Intermediate Python Training",
                             "location": "Berlin",
                             "trainer": "Ella M. Charming"},
                 "course3": {"title": "Python Text Processing Course",
                             "location": "München",
                             "trainer": "Monica A. Snowdon"}
                 }
    trainings2 = trainings.copy()
    trainings["course2"]["title"] = "Perl Training Course for Beginners"
    print(trainings2)
    trainings = {"course1": {"title": "Python Training Course for Beginners",
                             "location": "Frankfurt",
                             "trainer": "Steve G. Snake"},
                 "course2": {"title": "Intermediate Python Training",
                             "location": "Berlin",
                             "trainer": "Ella M. Charming"},
                 "course3": {"title": "Python Text Processing Course",
                             "location": "München",
                             "trainer": "Monica A. Snowdon"}
                 }
    trainings2 = trainings.copy()
    trainings["course2"] = {"title": "Perl Seminar for Beginners",
                            "location": "Ulm",
                            "trainer": "James D. Morgan"}
    print(trainings2["course2"])

    knowledge = {"Frank": {"Perl"}, "Monica": {"C", "C++"}}
    knowledge2 = {"Guido": {"Python"}, "Frank": {"Perl", "Python"}}
    knowledge.update(knowledge2)


