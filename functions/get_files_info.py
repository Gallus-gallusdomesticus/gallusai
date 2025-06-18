import os
from google.genai import types

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

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

        


    
    
    
    
