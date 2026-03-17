class Mammals:
    def __init__(self):
        """Constructor for this class."""
        # Create some member animals
        self.members = ["Tiger", "Lion", "Hippopotamus"]

    def printMembers(self):
        print("Printing members of the Mammals class from subpackage dangerous")
        for member in self.members:
            print("\t%s " % member)
