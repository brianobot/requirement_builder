import os
from string import whitespace

cwd = os.getcwd()

def clean_whitespaces(file):
    """ Remove all whitespace lines from a file"""
    cleaned_data = []
    with open(file, 'r') as data:
        data.seek(0)
        for line in data.readlines():
            if line not in whitespace:
                cleaned_data.append(line)
    with open(file, 'w') as new_file:
        new_file.writelines(cleaned_data)

def clean_duplicates(file):
    """ Remove all duplicate lines from a file"""
    with open(file, 'r') as data:
        lines = data.readlines()
        print(f'Lines = {lines}')
        lines_set = set(lines)
        print(f'Lines Set = {lines_set}')
    with open(file, 'w+') as new_file:
        new_file.writelines(list(lines_set))
        print(new_file.readlines())
                
def main(requirement_file):
    """ recursively walks through all directories from the current directory and
        copy the content of all requirements.txt file into the requirements.txt
        file at the initial top directory     
    """ 
    try:
        main_requirement_file = open(requirement_file, 'r+') #try to read the file
    except:
        main_requirement_file = open(requirement_file, 'w') #if not possible create it

    for path, _, filenames in os.walk(cwd):
        # exclude the current directory from the search
        if 'requirements.txt' in filenames and path != cwd:
            with open(f'{path}/{requirement_file}', 'r') as file:
                main_requirement_file.writelines(file.readlines() + ['\n'])


if __name__ == "__main__":
    requirement_file='requirements.txt'
    main(requirement_file)
    print('Current directory = ', os.getcwd())
    clean_whitespaces(requirement_file)
    clean_duplicates(requirement_file)
