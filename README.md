# Election_Analysis

## Project_Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python | Visual Studio Code

## Summary
The analysis of the election shows that:
- There were 369,711 total votes cast.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Stockham received 23.0% of the vote and 85,213 total votes.
  - DeGette received 73.8% of the vote and 272,892 total votes.
  - Doane received 3.1% of the vote and 11,606 total votes.
- The winner of the election was:
  - Diana DeGette, who received 73.8% of the vote and 272,892 total votes.
  
 ## Challenge Overview
 ### 1. Overview of Election Audit
 After previously calculating and displaying the voting breakdown by candidate, we also wanted to determine the number and percentage of votes by county.
 
 ### 2. Election-Audit Results
 - This congressional district saw 369,711 total votes cast.
 - Denver dominated the voting, accounting for nearly 83% of all ballots cast.
 - Denver county contributed almost eight times more votes than the next-closest county in the district (Jefferson).
 ![Election Results by County](/county_vote_breakdown.png)
 - There was a single candidate who dominated the voting almost as thoroughly as Denver did on the county side.
 ![Election Results by Candidate](/votes_by_candidate.png)
 - Diana DeGette received 272,892 votes (74%); that's better than three times more than her closest competitor, Charles Casper Stockham (85,213 | 23.0%).
 ## Challenge Summary
 Perhaps the best news for our elections team is that this script can be reused for essentially any future election. By simply reading in a similarly-constructed CSV file (ballot IDs, counties, candidates), we should be able to assess voting results in any scenario. Modifications to the script largely depend on the different types of elections that may be under examination, but adjustments could be made to account for additional values (e.g. a state column in a national popular vote) or candidate results could be broken down further by county to show if specific municipalities supported certain candidates to differing degrees.
