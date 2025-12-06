import os

def print_directory_contents(path="."):
    try:
        entries = os.listdir(path)
        print(f"Contents of directory '{path}':")
        for entry in entries:
            print(entry)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    # Agar aap kisi specific directory ka path dena chahte hain:
    # dir_path = "/path/to/directory"
    # print_directory_contents(dir_path)

    # Warna, current directory ka content print karega:
    print_directory_contents()
