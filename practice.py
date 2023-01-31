

from database import add_entry, get_entries, create_table

menu = '''
Please Select one of the following options:
1) Add new entry for today.
2) View entries.
3) Exit.

Your selection: 
'''
print('Welcome to the programming diary!')
create_table()

def prompt_new_entry():
  add_entry(input('What have you learned today? '), input('Enter the date: '))

def view_entries(entries):
  for entry in entries:
      print(f"\n{entry['date']}\n{entry['content']}\n")

# NON-WALRUS
# while user_input != '3':
#   user_input = input(menu)

# WALRUS
while (user_input := input(menu)) != '3':
  if user_input == '1':
    prompt_new_entry()
  elif user_input == '2':
    view_entries(get_entries())
  else:
    print('Invalid option, please try again!')

