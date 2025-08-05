import os
import shutil

def organize_folder(folder_path):
    if not os.path.isdir(folder_path):
        print("Provided path is not a directory.")
        return

    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)

        # skip directories
        if os.path.isdir(item_path):
            continue

        # get extension (without the dot), fallback to "unknown"
        _, ext = os.path.splitext(item)
        ext = ext[1:].lower() if ext else "unknown"

        target_folder = os.path.join(folder_path, ext if ext else "unknown")
        os.makedirs(target_folder, exist_ok=True)

        dest_path = os.path.join(target_folder, item)

        # handle name collision
        counter = 1
        base_name, extension = os.path.splitext(item)
        while os.path.exists(dest_path):
            new_name = f"{base_name}({counter}){extension}"
            dest_path = os.path.join(target_folder, new_name)
            counter += 1

        shutil.move(item_path, dest_path)
        print(f"Moved '{item}' → '{ext}/'")

def main():
    print("File Organizer")
    path = input("Enter folder path to organize (leave empty for current folder): ").strip()
    if not path:
        path = os.getcwd()
    organize_folder(path)
    print("Done.")

if __name__ == "__main__":
    main()
