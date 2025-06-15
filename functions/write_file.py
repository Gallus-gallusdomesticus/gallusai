import os

def write_file(working_directory, file_path, content):
    try:
        work_dir_abs=os.path.abspath(working_directory)

            
        if not os.path.isabs(file_path):
            dir_path = os.path.join(working_directory, file_path)
        else:
            dir_path = file_path

        dir_abs = os.path.abspath(dir_path)

        if dir_abs.startswith(work_dir_abs)==False:
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'

        dir_par=os.path.dirname(dir_abs)
        if os.path.exists(dir_par)==False:
            os.makedirs(dir_par)

    
        with open(dir_abs, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
                
    
    except Exception as e:
        return f"Error: {str(e)}"