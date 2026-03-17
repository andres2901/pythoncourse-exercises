class Mammals:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Dog', 'Panda', 'Opossum']
    
    def printMembers(self):
        print('Printing members of the Mammals class from subpackage harmless')
        for member in self.members:
            print('\t%s ' % member)
