# Getting Movie Name, Director Name, Year using FOR Loop
[movie, dir_name, year] = [input() for _ in range(3)]

# Printing Output using f'' (format string)
print(f'{movie} (dir. {dir_name}) came out in {year}')