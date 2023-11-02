Before you run the code
MAke sure you have python installed on your PC
open cmd in this voting system folder
run `python Automated Voting Syatem.py`

README

This code implements a simple automated voting system using Python. The system consists of three main classes:

Voter: A class representing a voter. It has the following attributes:
name: The voter's name.
id_number: The voter's identification number.
voted: A boolean indicating whether the voter has voted.
Candidate: A class representing a candidate. It has the following attributes:
name: The candidate's name.
party: The candidate's political party.
vote_count: The number of votes the candidate has received.
AutomatedVotingSystem: A class representing the automated voting system. It has the following attributes:
voters: A list of all voters registered in the system.
candidates: A list of all candidates running in the election.
The AutomatedVotingSystem class provides three main methods:

verify_voter(): This method takes a voter's identification number and returns the voter object if the voter is registered in the system and has not yet voted. Otherwise, it returns None.
cast_vote(): This method takes a voter object and a candidate object and casts a vote for the candidate on behalf of the voter.
get_results(): This method returns a dictionary mapping the names of the candidates to the number of votes they have received.
To use the automated voting system, you first need to create a list of voters and a list of candidates. Then, you can create an AutomatedVotingSystem object with the lists of voters and candidates as arguments.

Next, you can iterate over the list of voters and cast a vote for each voter using the cast_vote() method. Finally, you can get the results of the election using the get_results() method.