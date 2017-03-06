#for x in range(99, 0, -1):
#	print(str(x) + ' bottles of beer on the wall, ' + str(x) + ' bottles of beer.')
#	if (x-1 == 0):
#		print('Take one down and pass it around, no more bottles of beer on the wall.')
#	else:
#		print('Take one down and pass it around, ' + str(x-1) + ' bottles of beer on the wall.')
#	print('')
#print('No more bottles of beer on the wall, no more bottles of beer.')
#print('Go to the store and buy some more, 99 bottles of beer on the wall.')

def petle():
    for x in range (99, 0, -1):
        song = x, ' Bottles of Beer'
        print(song)
petle()