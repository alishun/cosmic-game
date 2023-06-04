import os
import msvcrt

def print_scene(scene):
    current_dir = os.getcwd()
    parent_dir = os.path.dirname(current_dir)
    sibling_dir = os.path.join(parent_dir, 'assets')
    file_path = os.path.join(sibling_dir, scene)
    with open(file_path, "r") as file:
        for line in file:
            print(line.rstrip())

def run():
    print_scene('welcome.txt')
    while True:
        char = msvcrt.getch().decode('utf-8')
        if char == 'q' or char == 'Q':
            return
        elif char == 'e' or char == 'E':
            break
    print_scene('setup.txt')
    while True:
        char = msvcrt.getch().decode('utf-8')
        if char == 'c' or char == 'C':
            break

    
    

if __name__ == "__main__":
    run()