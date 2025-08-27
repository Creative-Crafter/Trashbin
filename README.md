# 🗑️ Simple Trashbin Tool

A lightweight cross-platform tool to safely move files and folders into a **trashbin** instead of deleting them immediately.  
Includes a command to empty the trashbin with confirmation — like a minimal recycle bin for your terminal.  

## 🚀 Features

- 📦 Move files or folders into a local `trashbin/` folder  
- 🔄 Works on **Windows**, **Linux**, and **Mac**  
- 🛡️ Confirmation prompt before clearing the trashbin  
- ⚡ Simple usage via `.bat` (Windows) or `.sh` (Linux/Mac) scripts  
- 🧹 Easily restore files manually from the `trashbin/` folder  

## 🕹️ Usage

### Move to Trashbin

| Platform       | Command example          |
|----------------|--------------------------|
| **Windows**    | `delete.bat test.txt`    |
| **Linux/Mac**  | `./delete.sh test.txt`   |

---

### Clear the Trashbin

| Platform       | Command example |
|----------------|-----------------|
| **Windows**    | `clear.bat`     |
| **Linux/Mac**  | `./clear.sh`    |

⚠️ When clearing, all files are **permanently deleted** after confirmation (`y/n`).  

Have fun! 🎉🗑️