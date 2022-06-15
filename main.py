import task1
import task2


def example_task1():
    print()
    print("~~~Input example for task 1~~~")
    print("Input example for Windows - D:\Projects\year\month\day\day\hour\minute")
    print("Input example for MacOS - /Users/mac/Desktop/tmp/year/month/week/day")
    print()


def example_task2():
    print()
    print("~~~Input example for task 2~~~")
    print("Input example for title format = MVF")
    print("Input example for text format = A")
    print("Input example for file path = D:\Projects\python_test_task\our_file.txt")
    print()


def info_task_2_types_message():
    print()
    print("Message type: \n"
          "E - error \n"
          "W - warning \n"
          "I - information message\n")


def task_1_description():
    print('Input data: - a string containing the full path of the directory \n'
          'to be created. For example, r"C:\\catalog1\\catalog2\\catalog3". \n'
          'For example, if catalog1 exists and catalog2 and catalog3 are then \n'
          'they must be created.')
    print('Return value: - the result of the function execution in the bool format\n'
          '(True if the directory path was created successfully or False if the\n'
          'creation failed) or in int format, there may be more options,\n'
          'for example: 0 - successful, -1 - incorrect string format, and so on.')
    print('Prepare also the module that calls this procedure. For example, when \n'
          'running this module, the message is displayed: "Enter the name of the directory",\n'
          'after this message the user enters the full path and press Enter and get a message\n'
          'either that the directory was created successfully or that it failed.')
    print("Additional requirements:Don't use os.makedirs function, use only os.makedir")


def task_2_description():
    print('There is a file containing the output of some program. This file may contain\n'
          ' messages in the following format:')
    print('<beginning of line or one or more spaces after beginning of line>\n'
          '<Header><one or more space characters>message text <end of line character>\n'
          'or end of file Header format: MVFxxxxx<message type>. x is a number from 0 to 9.\n'
          'Message type: E - error, W - warning, I - information message.')
    print('Message example: '
          'MVF01095I FOUND RECORD ...any text\n'
          'MVF02345W ANY WARNING ...any text\n'
          'MVF22234E ALL NOTHING WORK\n'
          'You need to prepare a procedure to search for all messages or messages of a specific type.')
    print('Input data:'
          '- name of the file with program data;\n'
          '- message type we are looking for:\n'
          ' "E" (errors), "W" (warnings), "I" (info), "A" ( all messages, can be used as default value)')
    print('output:'
          '- a list of messages, each element of which contains the following information:'
          'he headline of the message;'
          'message type;'
          'offset in bytes of the beginning of the message from the beginning of the file;'
          'Message text.')
    print("For example, for the example above, the output will be like this (list of dictionaries):"
          "[ {'msg': 'MVF01095I', 'type': 'I', 'offset': 102, 'text': 'FOUND RECORD'},"
          "{'msg': 'MVF02345W', 'type': 'W', 'offset': 232, 'text': 'ANY WARNING'},"
          "{'msg': 'MVF22234E', 'type': 'E', 'offset': 302, 'text': 'ALL NOTHING WORK'}]")
    print('Prepare also a module that calls this procedure with a simple console interface in the\n'
          'form of "enter file name" and "enter message type"\n ')
    info_task_2_types_message()


def menu():
    print()
    print("1 - print description of task 1")
    print("2 - print description of task 2")
    print("3 - print description of message types for task 2")
    print("4 - run task 1")
    print("5 - run task 2")
    print("0 - exit program")
    print()


def main():
    print("Hello!\nTo continue, please, choose what you want to do")

    while True:
        menu()
        choice = int(input("Input number: "))
        if choice == 1:
            task_1_description()
        elif choice == 2:
            task_2_description()
        elif choice == 3:
            info_task_2_types_message()
        elif choice == 4:
            example_task1()
            path = input("Input path to create - ")
            task1.task1_create_full_path_of_directories(path)
        elif choice == 5:
            info_task_2_types_message()
            example_task2()
            title_format = input("Input title format - ")
            text_format = input("Input text format - ")
            file_path = input("Input file path - ")
            print(task2.task2(title_format, text_format, file_path))
        elif choice > 5 or (choice < 1 and choice != 0):
            print("\nPlease, enter a number from 1 to 5.")
        else:
            print("\nThank you! Hope to see you again:)")
            break


main()