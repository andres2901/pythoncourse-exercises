class Birds:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Finch', 'Macaw', 'Duck']
 
    def printMembers(self):
        print('Printing members of the Birds class from subpackage harmless')
        for member in self.members:
            print('\t%s ' % member)
