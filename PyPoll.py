# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes.
# 3. The percentage of votes each dandidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Add our dependencies
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load=os.path.join("Resources","election_results.csv")

# Assign a variable to save the file to a path 
file_to_save=os.path.join("analysis","election_analysis.txt")

# Initialize vote count
total_votes=0
# Declare a new list
candidate_options=[]

# Declare a new dictionary to store vote count by candidate
candidate_votes={}

# Winning Candidate and Winning Count Tracker
winning_candidate=""  #variable to hold string value
winning_count=0
winning_percentage=0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    
    # To do: read analyze data here
    # Read the file object with the reader function.
    file_reader=csv.reader(election_data)

    # Read and print the header row.
    headers=next(file_reader)
  
    # Print each row in the .csv file
    for row in file_reader:
        # 1. Tally total vote count (adds one each time loop through the rows)
        total_votes+=1
        
        # 2. Print the candidate name from each row.
        candidate_name=row[2]

        # Only add each unique appearance of candidate names.
        if candidate_name not in candidate_options:
            # Add candidate names to candidate list
            candidate_options.append(candidate_name)

            #Track candidates' vote counts
            candidate_votes[candidate_name]=0
   
        # 3. Add a vote to each candidates' count.
        candidate_votes[candidate_name]+=1

    # 4. Print the total votes
    #print("Total Votes is", total_votes)

    # Print the candidate list.
    #print("The candidates are: ",candidate_options)

    # Print candidate dictionary
    #print(candidate_votes)

# 3. Determine the percentage of votes for each candidate.
for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate
    votes=candidate_votes[candidate_name]

    # Calculate percentage
    vote_percentage=float(votes) / float(total_votes) *100

    if (votes>winning_count) and vote_percentage>winning_percentage:
        winning_count=votes
        winning_percentage=vote_percentage
        winning_candidate=candidate_name

    # Print the candidate name and percentage of votes.
    #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
    print(f"{candidate_name}: {vote_percentage:.1f}% {votes:,}\n")

winning_candidate_summary=(
    f"-----------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-----------------------\n")

print(winning_candidate_summary)





