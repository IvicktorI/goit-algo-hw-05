def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return 'No such name found'
        except IndexError:
            return 'Not found'
        except Exception as e:
            return f'Error: {e}'

    return inner

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact change."

@input_error
def phone(args,contacts):
    name=args[0]
    return f'{name}-{contacts[name]}'

@input_error
def show_all(contacts):
    from prettytable import PrettyTable

    table = PrettyTable()
    table.field_names = ["Name", "Phone"]
    for key in contacts:
        table.add_row([key,contacts[key]])

    str_out = str(table)

    return str_out


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case 'hello':
                print('How can I help you?')
            case 'add':
                print(add_contact(args,contacts))
            case 'change':
                print(change_contact(args,contacts))
            case 'phone':
                print(phone(args,contacts))
            case 'all':
                print(show_all(contacts))
            case 'close':
                print('Good bye!')
                break
            case 'exit':
                print('Good bye!')
                break
            case _:
                print('Invalid command.')


if __name__ == "__main__":
    main()