import os

def get_files_info(working_directory, directory=None):
    try:
        work_dir_abs=os.path.abspath(working_directory)
        
        if directory is None:
            directory="."
        
        if not os.path.isabs(directory):
            dir_path = os.path.join(working_directory, directory)
        else:
            dir_path = directory
        dir_abs = os.path.abspath(dir_path)


        if dir_abs.startswith(work_dir_abs)==False:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if os.path.isdir(dir_abs)==False:
            return f'Error: "{directory}" is not a directory'
        
        list_direct=os.listdir(dir_abs)

        lines=[]
        for dir in list_direct:
            joined_path=os.path.join(dir_abs, dir)
            is_dir=os.path.isdir(joined_path)
            size=os.path.getsize(joined_path)
            
            lines.append(f"- {dir}: file_size={size}, is_dir={is_dir}")

        return "\n".join(lines)
    
    except Exception as e:
        return f"Error: {str(e)}"

def get_file_content(working_directory, file_path):

    try:
        work_dir_abs=os.path.abspath(working_directory)

            
        if not os.path.isabs(file_path):
            dir_path = os.path.join(working_directory, file_path)
        else:
            dir_path = file_path

        dir_abs = os.path.abspath(dir_path)

        if dir_abs.startswith(work_dir_abs)==False:
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'

        if os.path.isfile(dir_abs)==False:
            f'Error: File not found or is not a regular file: "{file_path}"'

        Max_char=10000
        with open(dir_abs, "r") as f:
            file_content_string = f.read(Max_char)
            file_content_left = f.read(1)

            if file_content_left == "":
                return file_content_string
                
            else:
                return f'{file_content_string} [...File "{file_path}" truncated at 10000 characters]'
                
    
    except Exception as e:
        return f"Error: {str(e)}"
        


    
    
    
    
