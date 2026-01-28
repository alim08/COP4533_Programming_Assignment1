import sys

#stable matching class
class StableMatcher:
    #constructor
    def __init__(self):
        self.n = 0
        self.hospital_prefs = []
        self.student_prefs = []
        self.ranks = []
    
    #read from input, parses n, hospital preferences, and student preferences.
    def parse_input(self):
        try:
            input_data = sys.stdin.read().split()
            
            iterator = iter(input_data)
            self.n = int(next(iterator))


            #read in hospital preferences
            for _ in range(self.n):
                prefs = [int(next(iterator)) for _ in range(self.n)]
                self.hospital_prefs.append(prefs)

            #read in student preferences and build rank table
            for _ in range(self.n):
                prefs = [int(next(iterator)) for _ in range(self.n)]
                self.student_prefs.append(prefs)

                rank_map = {hospital: r for r, hospital in enumerate(prefs)}
                self.ranks.append(rank_map)
        
        except StopIteration:
            pass

            



