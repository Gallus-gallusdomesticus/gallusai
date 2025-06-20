import os
from google.genai import types

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

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write file in the specified file path constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path needed to write the file from, relative to the working directory. If the subdirectory doesnt exist, create the subdirectory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content that is being written on the file. This schema should be listed after file_path"
            )
        },
    ),
)