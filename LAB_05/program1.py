rectangle_a_length = int(input("Enter length A: "))
rectangle_a_width = int(input("Enter width A: "))
rectangle_b_length = int(input("Enter length B: "))
rectangle_b_width = int(input("Enter width B: "))
rectangle_a_area = rectangle_a_length * rectangle_a_width
rectangle_b_area = rectangle_b_length * rectangle_b_width
print('Area A:',format(rectangle_a_area,"d"))
print('Area B:',format(rectangle_b_area,"d"))

if rectangle_a_area > rectangle_b_area:
	print("Area A is greater than Area B.")
elif rectangle_a_area < rectangle_b_area:
	print("Area B is greater than Area A.")
else:
	print("Both of them are Equal.")
	
