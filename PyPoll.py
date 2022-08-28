# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Count total votes and grab candidate names.
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
    
    # Add the candidate name(s) to the candidate_options list.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
    # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
    
    with open(file_to_save, "w") as txt_file:
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        
        print(election_results, end="")

        txt_file.write(election_results)

        for candidate_name in candidate_options:
            votes = candidate_votes[candidate_name]
            vote_percentage = float(votes) / float (total_votes) * 100
            # print(f"{candidate_name} received {round(vote_percentage, 1)} of the vote.")
            # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            print(candidate_results)
            txt_file.write(candidate_results)
            if vote_percentage > winning_percentage and votes > winning_count:
                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate_name
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n"
        )
        print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)
