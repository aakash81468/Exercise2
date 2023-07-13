def group_teams(seating_order):
    grouping = []
    current_team = seating_order[0]
    count = 1

    for i in range(1, len(seating_order)):
        if seating_order[i] == current_team:
            count += 1
        else:
            grouping.append((current_team, count))
            current_team = seating_order[i]
            count = 1

    grouping.append((current_team, count))

    return grouping

# Example 
seating_order = "GGGGSSHHHGGRRRRRSSSHHHHH"
grouped_teams = group_teams(seating_order)
print(grouped_teams)