# This file performs the following functions:
# 1. Picks two input files from the user specified location
# 2. Compares the two files where-in first file would be input binary file and second file would be the binary file to patch data
# 3. Later allow user to specify offset and length of the data to be patched would be equal to the length of the second input file
# 4. Writes the patched data to the output file specified by user.


class Main:
    def __init__(self):
        self.input_file_1 = ""
        self.input_file_2 = ""
        self.output_file = ""
        self.offset = 0

    def get_input_files(self):
        self.input_file_1 = input("Enter the first input file: ")
        self.input_file_2 = input("Enter the second input file: ")
        self.output_file = input("Enter the output file: ")

    def get_offset(self):
        self.offset = int(input("Enter the offset: "))

    def read_input_files(self):
        with open(self.input_file_1, "rb") as file_1:
            file_1_data = file_1.read()
        with open(self.input_file_2, "rb") as file_2:
            file_2_data = file_2.read()
        return file_1_data, file_2_data

    def write_output_file(self, file_1_data, file_2_data):
        """
        This function writes the patched data to the output file at offset self.offset
        """
        with open(self.output_file, "wb") as file_3:
            self.get_offset()
            file_3.write(file_1_data[:self.offset])
            file_3.write(file_2_data)
            file_3.write(file_1_data[self.offset + len(file_2_data):])

    def main(self):
        self.get_input_files()
        file_1_data, file_2_data = self.read_input_files()
        self.write_output_file(file_1_data, file_2_data)


if __name__ == "__main__":
    main = Main()
    main.main()
    print("Done")
