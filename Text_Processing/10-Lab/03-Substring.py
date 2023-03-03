string_to_match = input()
research_string = input()

while string_to_match in research_string:
    research_string = research_string.replace(string_to_match, "")

print(research_string)
