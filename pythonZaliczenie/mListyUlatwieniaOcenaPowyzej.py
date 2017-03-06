oceny = [4.5, 3.0, 4.5, 4.5, 4.0, 4.5, 5.0, 5.0, 4.5, 4.0]
oceny.sort(reverse=True)
print (oceny)
print ("-----------------------------------------")
print ([i for i in oceny if i>4.0] )