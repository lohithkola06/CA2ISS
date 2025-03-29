def find_cube_pairs(target): #added colon to make function work
    solutions = []  # removed the ; at the end
    max_num = round(target ** (1/3))  # fixed 'targ' to 'target' and replaced '***' with '**'

    for a in range(1, max_num + 1):  # fixed 'ranges' to 'range'
        for b in range(a, max_num + 1):  # fixed 'ranges' to 'range'
            if a**3 + b**3 == target:  # fixed '***3' to '**3' and 'targ' to 'target'
                solutions.append((a, b))  # fixed 'sol.append' to 'solutions.append'

    return solutions  # fixed 'sol' to 'solutions'

pairs = find_cube_pairs(1729)  # removed the comma at the end
print("Valid cube pairs for 1729:") # fixed '1728' to '1729'

for a, b in pairs:  # fixed 'pair' to 'pairs'
    print(f"{a}³ + {b}³ = {a**3} + {b**3} = 1729")  # fixed '**2' to '**3' for proper cube values and # fixed '1728' to '1729'

print("""Submit your response here: https://forms.office.com/Pages/ResponsePage.aspx?id=vDsaA3zPK06W7IZ1VVQKHFzW4INMf2JMjyL9qPnLPbNUMFU2Tj1WjQyUlczSFNlOFBEWkxTQ0LFQS4u""")
