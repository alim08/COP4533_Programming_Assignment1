import sys
from collections import deque

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
    
    #run hospital-proposing Gale-Shapley Algorithm
    def solve_match(self):
        free_hospitals = deque(range(1, self.n + 1))
        matches = {}

        #track which index in preference list each hospital is at
        proposals_made = {h: 0 for h in range(1, self.n + 1)}

        while free_hospitals:
            h = free_hospitals[0]
            #get next student to propose to
            pref_list_idx = proposals_made[h]

            #check to see if h has proposed to everyone
            if pref_list_idx >= self.n:
                free_hospitals.popleft()
                continue

            s = self.hospital_prefs[h-1][pref_list_idx]
            #advance pointer
            proposals_made[h] += 1 

            if s not in matches:
                matches[s] = h
                free_hospitals.popleft()
            else:
                current_h = matches[s]
                #check student preferences
                if self.ranks[s-1][h] < self.ranks[s-1][current_h]:
                    #student prefers new hospital, and will trade up
                    matches[s] = h
                    free_hospitals.popleft()
                    free_hospitals.append(current_h)
                else:
                    #student rejects, and the hospital remains free
                    pass
                    
        #invert matches to hospital -> student
        return {h: s for s, h in matches.items()}
    
    #helper function to read matching from input lines
    def read_matching(self, input_lines):
        proposed_matching = {}
        for line in input_lines:
            parts = line.strip().split()
            if len(parts) == 2:
                h, s = int(parts[0]), int(parts[1])
                proposed_matching[h] = s
        return proposed_matching
    


if __name__ == "__main__":
    solver = StableMatcher()

    def parse_prefs_from_tokens(token_iterator, target_solver):
        target_solver.n = int(next(token_iterator))
        target_solver.hospital_prefs = []
        target_solver.student_prefs = []
        target_solver.ranks = []

        for _ in range(target_solver.n):
            row = [int(next(token_iterator)) for _ in range(target_solver.n)]
            target_solver.hospital_prefs.append(row)

        for _ in range(target_solver.n):
            row = [int(next(token_iterator)) for _ in range(target_solver.n)]
            target_solver.student_prefs.append(row)
            rank_map = {h: r for r, h in enumerate(row)}
            target_solver.ranks.append(rank_map)

    try:
        mode = sys.argv[1] if len(sys.argv) > 1 else "match"

        if mode == "match":
            #read preferences from stdin
            tokens = sys.stdin.read().split()
            token_iterator = iter(tokens)
            parse_prefs_from_tokens(token_iterator, solver)

            result = solver.solve_match()
            output_lines = [f"{h} {result[h]}" for h in sorted(result.keys())]
            output_text = "\n".join(output_lines)

            if len(sys.argv) > 2:
                output_path = sys.argv[2]
                with open(output_path, "w") as f:
                    f.write(output_text + "\n")

            print(output_text)

        elif mode == "verify":
            #if files are provided, read prefs and matching separately to avoid concatenation issues.
            if len(sys.argv) > 3:
                prefs_path = sys.argv[2]
                matching_path = sys.argv[3]

                prefs_tokens = open(prefs_path, "r").read().split()
                parse_prefs_from_tokens(iter(prefs_tokens), solver)

                matching_tokens = open(matching_path, "r").read().split()
                token_iterator = iter(matching_tokens)
            else:
                #fallback: read all from stdin (requires a separator between files)
                tokens = sys.stdin.read().split()
                token_iterator = iter(tokens)
                parse_prefs_from_tokens(token_iterator, solver)

            proposed_matching = {}
            try:
                while True:
                    h = int(next(token_iterator))
                    s = int(next(token_iterator))
                    proposed_matching[h] = s
            except StopIteration:
                pass

            print(solver.verify_matching(proposed_matching))

    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")




            



