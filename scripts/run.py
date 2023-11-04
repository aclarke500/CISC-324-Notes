# declare sections here, and the names will be extracted in the order they are declared
# so you can paste the concepts into chatGPT

# Sections 10.1, 10.2 (10.2.1, 10.2.3,)
# Sections 10.4 (10.4.1--10.4.4, 10.4.6,)
sections = [
 "Section 10",
  "Section 10.1",
  "Section 10.2",
  "Section 10.2.1",
  "Section 10.2.2",
  "Section 10.2.3",
  "Section 10.4",
  "Section 10.4.1",
  "Section 10.4.2",
  "Section 10.4.3",
  "Section 10.4.4",
  "Section 10.4.6",
    "Section 8.1",
    "Section 8.3.1",
    "Section 8.3.2",
    "Section 8.4",
]


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

def begins_with_correct_heading(line, section):
  if len(section) > len(line):
    return False
  
  for i in range(len(section)):
    if not section[i] == line[i]:
      return False
    
  return True

def remove_page_number(line):
  # returns substring with all characters before page number
  return_string = ''
  section_number_ended = False
  page_number_started = False
  for char in line:
    if not (section_number_ended and (char.isdigit() or char == '.')):
      section_number_ended = True
    if section_number_ended and char.isdigit():
      page_number_started = True

    if not page_number_started:
      return_string+=char



try:
  with open("text.txt", 'r') as file:
      line_number = 1
      while True:
          line = file.readline()
          if not line:
              break
          # probably section header
          if line[0].isnumeric() and (line[1] == '.'):
            for s in sections_formatted:
              if begins_with_correct_heading(line, s):
                section_topics.append([s, line.strip(), get_page_estimates(line_number)])
                sections_formatted.remove(s)
                break

          line_number += 1
except:

  with open("scripts/text.txt", 'r') as file:
      line_number = 1
      while True:
          line = file.readline()
          if not line:
              break
          # probably section header
          if line[0].isnumeric() and (line[1] == '.'):
            for s in sections_formatted:
              if begins_with_correct_heading(line, s):
                section_topics.append([s, line.strip(), get_page_estimates(line_number)])
                sections_formatted.remove(s)
                break

          line_number += 1



# print(section_topics)
for s in section_topics:
  print(s[1])

  # 375, 415 -> chapters 7 + 8