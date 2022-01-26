from copy import deepcopy
trainings = {"course1": {"title": "Python Training Course for Beginners",
                             "location": "Frankfurt",
                             "trainer": "Steve G. Snake"},
                 "course2": {"title": "Intermediate Python Training",
                             "location": "Berlin",
                             "trainer": "Ella M. Charming"},
                 "course3": {"title": "Python Text Processing Course",
                             "location": "Kolkata",
                             "trainer": "Monica A. Snowdon"}
                 }

trainings3 = deepcopy(trainings)
trainings2 = trainings.copy()
trainings["course2"]["title"] = "Perl Training Course for Beginners"
print("Trainins2 Print",trainings2)
trainings = {"course1": {"title": "Python Training Course for Beginners",
                             "location": "Frankfurt",
                             "trainer": "Steve G. Snake"},
                 "course2": {"title": "Intermediate Python Training",
                             "location": "Berlin",
                             "trainer": "Ella M. Charming"},
                 "course3": {"title": "Python Text Processing Course",
                             "location": "Kolkata",
                             "trainer": "Monica A. Snowdon"}
                 }
trainings2 = trainings.copy()
trainings["course2"] = {"title": "Perl Seminar for Beginners",
                            "location": "Ulm",
                            "trainer": "James D. Morgan"}
print(trainings2["course2"])
print trainings3