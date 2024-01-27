def main():
    print("A simple script!")


print("This command will be executed every time this module is imported!")

if __name__ == "__main__":
    # execute if this script was run by: python simple_script.py
    # don't execute if the script was imported as a module: import simple_script
    print("This command will be excuted just if the script was run as a script!")
    main()
