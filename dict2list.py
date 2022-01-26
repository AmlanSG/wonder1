d = {'a': 10, 'b': 1, 'c': 22}
k = d.items()
print (k)
print (type(k))
t = list(d.items())
print (type(t))
print (t)
t.sort()
print (t)

w = {"house":"Haus", "cat":"", "red":"rot"}
items_view = w.items()
items = list(items_view)
print (items)

dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
countries = ["Italy", "Germany", "Spain", "USA"," Switzerland"]
Z1 = zip(countries, dishes)
print (Z1)
print (type(Z1))
#country_specialities = list(Z1)
#print country_specialities
country_specialities_dict = dict(Z1)
print(country_specialities_dict)
print (type(country_specialities_dict))
