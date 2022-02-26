from logic.line_finder import LineFinder


class FileReader:
    name_to_data = {}

    def __init__(self, file_path):
        lines = LineFinder.get_lines(file_path)

        for line in lines:
            delimeter_start = line.index(":")

            name = line[:delimeter_start]
            data = line[delimeter_start + 1:]

            self.name_to_data[name] = data
    
    def get_number_list(self, item_name):
        """returns: List of Double; the list that has the line as the key"""

        data = self.name_to_data[item_name]

        # The first and last index don't matter
        current_item = ""
        number_list = []
        for ch in data[1:-1]:
            if ch == ",":
                number_list.append(int(current_item))
                current_item = ""
            
            else:
                current_item += ch
        number_list.append(int(current_item))
        return number_list
    
    def get_int(self, item_name):
        return int(self.name_to_data[item_name]])