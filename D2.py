capitals = {"Springfield":"Illinois", "Augusta":"Maine", "Boston":
"Massachusetts", "Lansing":"Michigan", "Albany":"New York",
"Olympia":"Washington", "Toronto":"Ontario","New Delhi": "Delhi", "New Delhi":"NCR"}
# Key : Value
# City : State
var1 = capitals.pop("New Delhi")
print var1
print type(var1)
var = capitals.popitem()
print var
print type(var)
print capitals