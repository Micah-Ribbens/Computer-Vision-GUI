from logic.file_reader import FileReader

file_reader = FileReader("json.txt")

centers = file_reader.get_number_list("ObjectCenter")
lengths = file_reader.get_number_list("ObjectWidth")
heights = file_reader.get_number_list("ObjectHeight")

line1 = "test_number1.all_objects:["
line2 = "test_number1.objects_of_interest:["

for x in range(len(heights)):
    height = heights[x]
    length = lengths[x]
    x_center = centers[x * 2]
    y_center = centers[x * 2 + 1]


    x_coordinate = x_center - (length / 2)
    y_coordinate = y_center - (height / 2)

    line1 += f"{x_coordinate},{y_coordinate},{length},{height},"
    line2 += f"{x_coordinate},{y_coordinate},{length},{height},"

file = open("data.txt", "w+")
file.write(f"number_of_tests:1\n{line1}]\n{line2}]")

