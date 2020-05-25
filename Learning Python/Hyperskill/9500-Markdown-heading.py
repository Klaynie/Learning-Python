def heading(header, level=1):
    if level < 1:
        return heading(header, level=1)
    if level > 6:
        return heading(header, level=6)
    return f'{"#" * level} {header}'

print(heading("A"))      # Returns "# A"
print(heading("A", 3))   # Returns "### A"
print(heading("A", 1))   # Returns "# A"
print(heading("A", 0))   # Returns "# A"
print(heading("A", 10))  # Returns "###### A"