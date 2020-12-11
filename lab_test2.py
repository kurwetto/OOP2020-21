# Object Oriented Programming
# TU856 & TU858
# Semester 1, 2020-21
# B. Schoen-Phelan
# 11-12-2020

# Lab test 2
# Michal Korneluk C19434762
# TU 858

class Document:
    """
    Class to handle file management for file writing.
    Class Document receives the file name at initialisation.
    """

    def file_writing(self):
        file_writing = {}

    def __init__(self, file_name):
        self.characters = []
        self.cursor = 0
        self.filename = file_name

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

        #Try and exception for def delete
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

        #Try and Exception for def save
        try:
            fo = open(self.filename, "w", encoding='utf-8')
            fo.write(''.join(self.characters))
            print(f"Your file {self.filename} has "f"been created.\nPlease check.\n")
        except Exception as e:
            print("Caught this error: %s" % e.__class__.__name__)

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
        maximum_value = 12
        if steps > maximum_value:    # if statement for maximum value & steps
            print("Number too big")
        else:
            self.cursor -= steps

# getters and setters

@property
def get_characters(self):
    return self.__characters

@property
def get_cursor(self):
    return self.__cursor


def set_characters(self, a):
    self.__characters = a


def set_cursor(self, a):
    self.__cursor = a

# initialising an object and using the class
doc = Document("lab_t2.txt")
characters = 'fake mews'
maximum_value = 3 # to make if statement work

for letter in characters:
    doc.insert(letter)
    maximum_value += 1 # increment ++

doc.backward(18)
doc.delete()
doc.insert('n')
doc.save()
