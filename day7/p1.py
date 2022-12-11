from linux import Linux, File, Dir

advent = []
file_system = Linux()

with open("advent.txt", "r", encoding="utf-8") as file:
    for line in file.readlines():
        advent.append(line.strip())

# converting command line text into required objects
i = 0
while i < len(advent):
    if advent[i].startswith("$"):  # command
        command, *args = advent[i].replace("$", "".strip()).split()
        # print(command, args, file_system.current_path, file_system.current_dir)
        # print(file_system.pretty_print(file_system.home))
        match command:
            case "cd":
                file_system.cd(args[0])
            case "ls":
                j = i + 1
                while j < len(advent) and not advent[j].startswith("$"):
                    blob_info, blob_name = advent[j].split()
                    if blob_info == "dir":
                        new_dir = Dir(blob_name)
                        file_system.create_blob(new_dir)
                    else:
                        new_file = File(blob_name, int(blob_info))
                        file_system.create_blob(new_file)
                    j += 1
                i = j - 1
            case _:
                pass

    i += 1

print(file_system.pretty_print(file_system.home))
# print(len(file_system.home))
