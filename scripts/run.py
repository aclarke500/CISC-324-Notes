# declare sections here, and the names will be extracted in the order they are declared
# so you can paste the concepts into chatGPT

sections = [ # copied and pasted from onQ
    # "Section 7.1.1",
    # "Section 7.1.2",
    # "Section 7.1.3",
    # "Section 7.1.3.1",
    # "Section 7.1.3.2",
    "Section 8.1",
    "Section 8.3.1",
    "Section 8.3.2",
    "Section 8.4",
]

# Chapter 7: Section 7.1.1, Section 7.1.2, Section 7.1.3- 7.1.3.1--7.1.3.2

# Chapter 8: Section 8.1, Section 8.3- 8.3.1--8.3.2, Section 8.4


 # remove section
sections_formatted = []

for s in sections:
  temp_str = ""
  for c in s:
    if c.isnumeric() or c == '.':
      temp_str += c
  sections_formatted.append(temp_str)

print (sections_formatted)


section_topics = []

total_lines = 54799 # hardcoded so we don't open and close file for this cunt
total_pages = 1278

def get_page_estimates(line_number):
  line_percent = line_number/total_lines
  page_est = round(line_percent*total_pages)
  return [page_est-10, page_est+10]

with open("text.txt", 'r') as file:
    line_number = 1
    while True:
        line = file.readline()
        if not line:
            break
        # probably section header
        if line[0].isnumeric() and (line[1] == '.'):
          for s in sections_formatted:
            if s in line:
              section_topics.append([s, line.strip(), get_page_estimates(line_number)])
              sections_formatted.remove(s)
              break

        line_number += 1


# print(section_topics)
for s in section_topics:
  print(s[1])

  # 375, 415 -> chapters 7 + 8