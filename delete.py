import os
import shutil
import sys

def main():
    if len(sys.argv) < 2:
        print("Please provide a file or folder! Example: delete test.txt")
        return

    target = sys.argv[1]

    # Base folder = folder where delete.py is located
    base_folder = os.path.dirname(os.path.abspath(__file__))

    # Trashbin in the same base folder
    trashbin = os.path.join(base_folder, "trashbin")

    # Create trashbin if it doesn't exist
    os.makedirs(trashbin, exist_ok=True)
    print("🟢 Trashbin is created")

    source = os.path.join(base_folder, target)

    try:
        shutil.move(source, trashbin)
        print(f"🟢 The file or folder '{target}' was moved to the trashbin")
    except FileNotFoundError:
        print(f"🔴 A file or folder named '{target}' was not found!")

if __name__ == "__main__":
    main()
