#Python Program for Formatting of Strings

# Default order
a = "{} {} {}".format('Geeks', 'For', 'Life')
print(a)

# Positional Formatting
b = "{1} {0} {2}".format('Geeks', 'For', 'Life')
print(b)

# Keyword Formatting
String1 = "{l} {f} {g}".format(g='Geeks', f='For', l='Life')
print(String1)
