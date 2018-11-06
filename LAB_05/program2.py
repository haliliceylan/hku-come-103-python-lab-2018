book_count = int(input("Number of Books has purchased this month:"))

if book_count == 0:
	point = 0
elif book_count == 2:
	point = 5
elif book_count == 4:
	point = 15
elif book_count == 6:
	point = 30
elif book_count >= 8:
	point = 60
else:
	point = 0
	
print("You earn",point,"points.")