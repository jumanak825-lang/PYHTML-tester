from string import Template
t=Template("$name is the $job of the $company")
s=t.substitute(name="Steve Jobs",job="CEO",company="Apple")
print(s)