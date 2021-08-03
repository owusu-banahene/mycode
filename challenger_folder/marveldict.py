#!/usr/bin/env python3
marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"She-Hulk":
  {"real name": "jennifer walters",
  "powers": "super strength & intelligence",
  "archenemy": "Titania"}
             }

char_name = input(" Which character do you want to know about? (Starlord,Mystique,She-Hulk)")

stats = input(" What statistic do you want to know about? (real name, powers, archenemy)")
if str(marvelchars.get(char_name.capitalize()))=="None":
    print(f"Sorry, {char_name} is not in the dictionary of marvel characters")
else:
    if char_name == "real name":
        char_name = char_name.capitalize()
        value = marvelchars.get(char_name).get(stats).capitalize()
        print(f"{char_name}'s {stats} is {value}")
    else:
        print(f"{char_name}'s {stats} is {marvelchars[char_name.capitalize()][stats]}")

