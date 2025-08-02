all_contacts = []
def main(comand):

    def hallo():
        print('Hallo, how can I help you?')

    def add_contact(comand_input):
        text = comand_input.strip().split(' ')
        name = text[1]
        contact = text[2]
        done_cont = {name: contact}
        all_contacts.append(done_cont)
        print('Contact added.')

    def change_contact(comand_input):
        text = comand_input.strip().split(' ')
        name = text[1]
        for i in range(len(all_contacts)):
            if name in all_contacts[i]:
                all_contacts[i][name] = text[2]
                print("Contact changed.")
                return
            else:
                print("Contact not found.")

    def show_phone(comand_input):
        text = comand_input.strip().split(' ')
        name = text[1]
        for i in range(len(all_contacts)):
            if name in all_contacts[i]:
                print(i[name])
                return
            else: 
                print("Phone not found")

    def show_all():
        print(all_contacts)

    def close():
        print("Good bye!")

    action = comand.strip().split(' ')[0]
    if action in ('hallo', 'Hallo', 'Hi', 'hi'):
        hallo()
    elif action in ('add', 'Add'):
        add_contact(comand)
    elif action in ('change', 'Change'):
        change_contact(comand)
    elif action in ('phone', 'Phone'):
        show_phone(comand)
    elif action in ('all', 'All'):
        show_all()
    elif action in ('close', 'exit', 'Close', 'Exit'):
        close()
        return False
    else:
        print('Plese, enter another command')
    return True

while True:
    command = input(">>> ")
    if not main(command):
        break

            
        