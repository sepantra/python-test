import pprint
names=["Sayid","Moeen","Setareh"]
roles=["Project Manager","Web Developer","Python Programmer"]

output={ "Hello "+names[i]:["Role:" +roles[i]] for i in range(3)}

pprint.pprint(output)
