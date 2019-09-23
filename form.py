print("Sammy has {} balloons.".format(5))

s = 10
print("Sammy has {} balloons.".format(s))

g = "Sammy loves {} {}." #2 {} placeholders
print(g.format("open-source", "software"))

g = "Sammy loves {} {} and has {} {}." #4 {} placeholders
print(g.format("open-source", "software","5","ballons"))


g = "Sammy loves {2} {1} and has {0} {1}." #4 {} placeholders
print(g.format("open-source", "software","5"))

print("Sammy the {a} {0} a {0}.".format("shark", "made", a = "pull request"))

print("Sammy ate {0:f} percent of a {1}!".format(75, "pizza"))
print("Sammy ate {0:.2f} percent of a {1}!".format(75, "pizza"))

print("Sammy has {0:4} red {1:16}!".format('A', 5))
print("Sammy has {0:^4} red {1:4}!".format(5, "balloons"))
print("Sammy has {0:<4} red {1:4}!".format(5, "balloons"))
print("Sammy has {0:>4} red {1:4}!".format(5, "balloons"))

print("{:1^20s}".format("Sammy"))

for i in range(3,13):
    print(i, i*i, i*i*i)
    
for i in range(3,13):
	print("{:3d} {:4d} {:5d}".format(i, i*i, i*i*i))












