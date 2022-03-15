import pprint
Names=["Sayid","Moeen","Setareh"]
Roles=["Project Manager","Web Developer","Python Programmer"]

new={ "Hello "+Names[i]:["Role:" +Roles[i]] for i in range(3)}

pprint.pprint(new)
