from functions.get_files_info import get_files_info, get_file_content

if __name__ == "__main__":
    # your test code here
    print(get_files_info("calculator", "."))

    print(get_files_info("calculator", "pkg"))

    print(get_files_info("calculator", "/bin"))

    print(get_files_info("calculator", "../"))

    print(get_file_content("calculator", "main.py"))

    print(get_file_content("calculator", "pkg/calculator.py"))

    print(get_file_content("calculator", "./bin/cat"))


