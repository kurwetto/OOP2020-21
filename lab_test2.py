# Object Oriented Programming
# TU856 & TU858
# Semester 1, 2020-21
# B. Schoen-Phelan
# 11-12-2020

# Lab test 2
# Michal Korneluk C19434762
# Tu 858

class Document:
    """
    Class to handle file management for file writing.
    Class Document receives the file name at initialisation.
    """

    def __init__(self, file_name):
        self.characters = []
        self.cursor = 0
        self.filename = file_name
        try:
            fo = open(file_name, "r")
        except Exception as e:
            file_writing = False
            print("Caught this error: %s" % e.__class__.__name__)

    def insert(self, character):
        """
        Method inserts a character at the current
        cursor position.
        Argument:
        ---------
        character : str
        the character to insert

        returns: no return
        -------
        """
        self.characters.insert(self.cursor, character)
        self.cursor += 1



    def delete(self):
        """
        Method deletes a character from the current
        cursor position.
        Arguments: none
        Returns: none
        """
        try:
            del self.characters[self.cursor]
        except Exception as e:
            print("Caught this error: %s" % e.__class__.__name__)

    def save(self):
        """
        Method saves all characters in the characters list
        to a file.
        Arguments: none
        Returns: none
        """
        with open(self.filename, 'w') as f:
            f.write(''.join(self.characters))

        print(f"Your file {self.filename} has "
              f"been created.\nPlease check.\n")

    def forward(self, steps):
        """
        Method fowards to a particular position in
        characters [].
        Arguments:
        ----------
        steps: int
            The amount of steps the cursor should be
            pushed forward by

        Returns: none.
        """
        self.cursor += steps

    def backward(self, steps):
        """
        Method backward moves the cursor position to
        that specific location in the characters list.
        Arguments:
        ----------
        steps : int
            The amount of steps to go back

        Returns: none
        """
        max_value = 12
        if steps > max_value:
            print("The number is too big")
        else:
            self.cursor -= steps



# initialising an object and using the class
doc = Document("lab_t2.txt")
characters = 'fake mews'
max_value = 3

for letter in characters:
    doc.insert(letter)
    max_value += 1
    print(max_value)

doc.backward(18)
doc.delete()
doc.insert('n')
doc.save()
