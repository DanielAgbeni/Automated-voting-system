import random

class Voter:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number
        self.voted = False

class Candidate:
    def __init__(self, name, party):
        self.name = name
        self.party = party
        self.vote_count = 0

class AutomatedVotingSystem:
    def __init__(self, voters, candidates):
        self.voters = voters
        self.candidates = candidates

    def verify_voter(self, id_number):
        for voter in self.voters:
            if voter.id_number == id_number and not voter.voted:
                return voter
        return None

    def cast_vote(self, voter, candidate):
        voter.voted = True
        candidate.vote_count += 1

    def get_results(self):
        results = {}
        for candidate in self.candidates:
            results[candidate.name] = candidate.vote_count
        return results

# Create a list of voters
voters = [
    Voter("Alice", 1234567890),
    Voter("Bob", 9876543210),
    Voter("Carol", 2987654321),
    Voter("David", 3987654321),
    Voter("Eve", 4987654321),
    Voter("Frank", 5987654321),
    Voter("Grace", 6987654321),
    Voter("Henry", 7987654321),
    Voter("Irene", 8987654321),
    Voter("Daniel", 9876354321),    
    Voter("Nathan", 6507324321),
    Voter("John", 7657864321),
]


# Create a list of candidates
candidates = [
    Candidate("John Doe", "Democrat"),
    Candidate("Jane Doe", "Republican"),
]

# Create an automated voting system
voting_system = AutomatedVotingSystem(voters, candidates)

# Iterate over the list of voters and cast a vote for each voter.
for i in range(9):
    voting_system.cast_vote(voters[i], candidates[0])

for i in range(9, 12):
    voting_system.cast_vote(voters[i], candidates[1])

# Get the results of the election.
results = voting_system.get_results()

# Print the results.
for candidate, vote_count in results.items():
    print(f"{candidate}: {vote_count}")

