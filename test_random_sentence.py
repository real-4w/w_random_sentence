import secrets

names=["This", "That", "It"]
extras=["surely", "probably", "likely","definately", "absolutely", ""]
verbs=["was","is","looks","seems", "could be", "might be", "should be", "looks like it will be"]
nouns=["cool","exciting","pretty cool","awesome","pretty exicting", "funky", "usefull", "mighty good"]
infinitives = [".", ", for no apparent reason.", ", because I say so."]

s_nouns = ["A dude", "My mom", "The king", "Some guy", "A cat with rabies", "A sloth", "Your homie", "This cool guy my gardener met yesterday", "Superman"]
p_nouns = ["These dudes", "Both of my moms", "All the kings of the world", "Some guys", "All of a cattery's cats", "The multitude of sloths living under your bed", "Your homies", "Like, these, like, all these people", "Supermen"]
s_verbs = ["eats", "kicks", "gives", "treats", "meets with", "creates", "hacks", "configures", "spies on", "retards", "meows on", "flees from", "tries to automate", "explodes"]
p_verbs = ["eat", "kick", "give", "treat", "meet with", "create", "hack", "configure", "spy on", "retard", "meow on", "flee from", "try to automate", "explode"]
#infinitives = ["to make a pie.", "for no apparent reason.", "because the sky is green.", "for a disease.", "to be able to make toast explode.", "to know more about archeology."]


for i in range(3):
    print(f"{secrets.choice(names)} {secrets.choice(extras)} {secrets.choice(verbs)} {secrets.choice(nouns)}{secrets.choice(infinitives)}")
    #print(f"{secrets.choice(s_nouns)} {secrets.choice(s_verbs)} {secrets.choice(s_nouns).lower()} {secrets.choice(p_nouns).lower()}, {secrets.choice(infinitives)}")