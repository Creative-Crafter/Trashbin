import os
import shutil

def main():
    # Same trashbin location as in delete.py
    base_folder = os.path.dirname(os.path.abspath(__file__))
    trashbin = os.path.join(base_folder, "trashbin")

    if os.path.exists(trashbin):
        confirm = input("Do you really want to clear the trashbin? (y/n): ")
        if confirm.lower() in ["y", "yes"]:
            shutil.rmtree(trashbin)
            os.makedirs(trashbin)
            print("🟢 Trashbin cleared")
        else:
            print("❌ Cancelled.")
    else:
        print("🔴 Trashbin doesn't exist yet")

if __name__ == "__main__":
    main()
