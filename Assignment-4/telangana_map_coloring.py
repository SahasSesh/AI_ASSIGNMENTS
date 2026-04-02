# Telangana Map Coloring (Simplified CSP)

districts = [
    "Adilabad", "Nizamabad", "Karimnagar", "Warangal",
    "Khammam", "Nalgonda", "Mahabubnagar", "Medak", "Hyderabad"
]

neighbors = {
    "Adilabad": ["Nizamabad"],
    "Nizamabad": ["Adilabad", "Karimnagar", "Medak"],
    "Karimnagar": ["Nizamabad", "Warangal", "Medak"],
    "Warangal": ["Karimnagar", "Khammam"],
    "Khammam": ["Warangal", "Nalgonda"],
    "Nalgonda": ["Khammam", "Mahabubnagar"],
    "Mahabubnagar": ["Nalgonda", "Medak"],
    "Medak": ["Nizamabad", "Karimnagar", "Mahabubnagar", "Hyderabad"],
    "Hyderabad": ["Medak"]
}

colors = ['Red', 'Green', 'Blue', 'Yellow']


def is_valid(region, color, assignment):
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True


def backtrack(assignment):
    if len(assignment) == len(districts):
        return assignment

    for region in districts:
        if region not in assignment:
            for color in colors:
                if is_valid(region, color, assignment):
                    assignment[region] = color
                    result = backtrack(assignment)
                    if result:
                        return result
                    del assignment[region]
            return None


solution = backtrack({})
print("Telangana Map Coloring Solution:")
print(solution)
