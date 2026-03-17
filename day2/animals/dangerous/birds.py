class Birds:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Ostrich', 'Emu', 'Eagle']
 
    def printMembers(self):
        print('Printing members of the Birds class from subpackage dangerous')
        for member in self.members:
            print('\t%s ' % member)
