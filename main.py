# better for many functions:
# from  functions import get_todos, write_todos
# better for few functions:
import functions
import time

now = time.strftime("%b, %d, %Y, %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add') or user_action.startswith('new'):
        todo = user_action[4:] + "\n"

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()

        # new_todos = []
        # for item in todos:
            # new_item = item.strip("\n")
            # new_todos.append(new_item)

        # new_todos = [item.strip("\n") for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
             number = int(user_action[5:])

             todos = functions.get_todos()

             number = number - 1
             new_todo = input("Enter a new todo: ") + "\n"
             todos[number] = new_todo

             functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid")
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith('complete'):
        try:
             number = int(user_action[9:])

             todos = functions.get_todos()

             index = number - 1
             todo_to_remove = todos[index].strip("\n")

             todos.pop(index)

             functions.write_todos(todos)

             print(f"Congrats! Todo '{todo_to_remove}' has been completed.")
        except ValueError:
            print("Your command is not valid")
        except IndexError:
            print("There is no item with that number")
        continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Invalid command.")
print("Goodbye for now!")