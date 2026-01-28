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
    
    
    #verify that all matches are stable
    def verify_matching(self, matching):
        #matching is a dict {hospital_id: student_id}

        #first check if every hospital and student is matched to exactly one
        h_matched = sorted(matching.keys())
        s_matched = sorted(matching.values())
        expected = list(range(1, self.n + 1))

        if h_matched != expected or s_matched != expected:
            return "INVALID: Matching is not a perfect bijection"
        
        #check if there are any blocking pairs
        #invert matching to look up student's current hospital easily
        student_match = {s: h for h, s in matching.items()}

        for h in range(1, self.n + 1):
            current_s = matching[h]

            #check if every student h prefers more than their current match
            for s_candidate in self.hospital_prefs[h-1]:
                if s_candidate == current_s:
                    break
                
                #h prefers s_candiate, does s_candidate prefer h?
                h_current_match = student_match[s_candidate]

                #use rank table for O(1) speed
                rank_new = self.ranks[s_candidate-1][h]
                rank_curr = self.ranks[s_candidate-1][h_current_match]

                if rank_new < rank_curr:
                    return f"UNSTABLE: Blocking pair ({h}, {s_candidate})"

        return "VALID STABLE"
        




            



