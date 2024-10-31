# BLT PPA Sorting Algorithm (sort_stack.py)

## Program Overview
This Python program assigns leaders to members for PPAs (Physical Performance Assessments), aiming to maximize diversity in assignments throughout a season. The goal is to ensure that leaders watch different members as often as possible.

### Inputs:
- **Leaders**: A list of BLT leaders.
- **Members**: A list of non-leader members. 
- **Total PPAs**: The total number of PPAs for the season.

Number of leaders and members changes every season. <b>Ensure you use numMembers and numLeaders variables</b> where applicable.

### Output:
The program generates assignments showing which leader is assigned to each member for every PPA. Additionally, it calculates a **variability score** to measure how diverse the assignments are (a lower score means more diversity).

## Task
Your task is to implement the `mainSort()` function in `sort_stack.py`. This function will:
1. Loop through each PPA and assign leaders to members.
2. Ensure leaders are not repeatedly assigned to the same members.
3. Select leaders with the fewest prior interactions with a member (or other leader) to ensure diverse assignments.
4. Ensure method is well documented to ensure this routine's longevity

The function could follow this basic structure:

```python
for num in range(numberOfPPAs):
    ...
    for team in groups.keys():
    ...
        for person in range(groups[team]):
        ...
            while matchFound == False:
            ...
```

## Assignment Rules
- Leaders should not be assigned to the same member or group more than necessary.
- Each leader-member assignment is tracked, with a number indicating how many times the leader has been assigned to that member (e.g., `[Leader 1, Member 5, 1]`).
- For each new assignment, the program selects the leader with the fewest previous interactions with the member out of the available leaders.
- <b>Every</b> leader must be assigned to someone for for each group. Doubling up on one person is fine as long as the previous rule is still adhered to

The method will cycle through each member and attempt to assign them to an available leader (a leader who hasnt already been assigned for a group and is not in the group). A number must be assigned with each connection starting at 0. Every time the member matches with a leader, that connection's assigned number is inremented by 1. for example, if `[Leader 1, Member 5, 1]` connection is made it would then be updated to `[Leader 1, Member 5, 2]`. The alorithm should seek to find the lowest number to make the assignment more diverse.
### Example:
Assigning Member 4 to a leader, we have:
```
[Leader 1, Member 4, 1]
[Leader 2, Member 4, 2]
[Leader 3, Member 4, 0] <- Unavailable
[Leader 4, Member 4, 3]
[Leader 5, Member 4, 1] <- Unavailable
[Leader 6, Member 4, 2]
```
In this case, the program should choose Leader 1, since they have the fewest interactions with Member 4 out of the available leaders.<br>

### Variability Score:
The `variability` score is perhaps the most important part of this program as it allows us to know how "diverse" and well-distributed the assigments are. This score is to be calculated by taking the mean of all the assigned numbers from every connection (Connections that occured 0 times are still included). [Leader 6, Member 4, `2`] <- this number. The goal is to run the program until we get the smallest `variability` score possible because this means the matches are more diverse.

## Output
The output should clearly show the assignments for each PPA, structured by group. I'll offer flexibility but the first itereation of this program used the following style to display the results:
```
PPA: 1
---------------------
Maroon 1:
    Leader 1 -> Member 3
    Leader 3 -> Member 2
    .
    .
    .
.
.
.

Gold 5:
    Leader 1 -> Member 38
    Leader 3 -> Leader 4
    .
    .
    .

PPA: 2
---------------------
.
.
.

Variability Score: 10.10
```
## Summary
- <b>Main Task:</b> Implement the mainSort() method to assign leaders to members in a diverse manner across multiple PPAs.
- <b>Key Output:</b> Display the assignments and calculate the variability score, aiming to minimize it for the most diverse assignments possible.
