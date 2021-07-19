'''Datastructures storing grouped data that has a relationship with each other
order in the data is determined by order in the list
List = []
inbetween is items seperated by comma
https://docs.python.org/3/tutorial/datastructures.html
'''

states = ["Delware", "California", "etc"]#list of US states
print(states[1])#printing items from a list
best_state = states[2]#pulling items from a list
bestest_state = states[-1]#pulling items from a list
states[1] = "New York"# Changing element in a list
states.append("new state")#adding to the end the list
states.extend(["keithland", "Queenieland","Johnland"])#extending list with additional list