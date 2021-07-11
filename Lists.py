friends = ["Kevin", "Creed", "Jim", "Michael", "Dwight", "Angela", "Pam"]
print(friends)
print(friends[0])
print(friends[3])
print(friends[1:])
print(friends[1:3])
print(friends[1:5])
print(friends[-1])
friends[1] = "Karen"
print(friends[1])

# Functions with lists
lucky_numbers = [4, 7, 69, 420, 23]
friends = ["Kevin", "Creed", "Jim", "Michael", "Dwight", "Angela", "Pam"]

print(friends)
friends.extend(lucky_numbers)
print(friends)
friends.append("Karen")
print(friends)
friends.insert(1, "Kelly")
print(friends)
friends.remove("Jim")
print(friends)
friends.clear()
print(friends)
friends = ["Kevin", "Creed", "Jim", "Michael", "Dwight", "Angela", "Pam"]
friends.pop() # removes the last element from the list
print(friends)
friends = ["Kevin", "Creed", "Jim","Jim",  "Michael", "Dwight", "Angela", "Pam"]
print(friends.count("Jim"))
friends.sort()
print(friends)
friends.pop(3)
print(friends)
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)
friends2=lucky_numbers.copy()
print(friends2) 