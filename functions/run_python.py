import subprocess
import os
from google.genai import types

def run_python_file(working_directory, file_path):
    
    try:
        work_dir_abs=os.path.abspath(working_directory)
                
        if not os.path.isabs(file_path):
            dir_path = os.path.join(working_directory, file_path)
        else:
            dir_path = file_path

        dir_abs = os.path.abspath(dir_path)

        if dir_abs.startswith(work_dir_abs)==False:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory.'

        if os.path.isfile(dir_abs)==False:
            return f'Error: File "{file_path}" not found.'
        
        if dir_abs.endswith(".py")==False:
            return f'Error: "{file_path}" is not a Python file.'
        
        process=subprocess.run(["python3",dir_abs], timeout=30,capture_output=True)
        
        if process.stdout==b'' and process.stderr==b'':
            return "No output produced."

        stdout=process.stdout.decode().rstrip('\n')
        stderr=process.stderr.decode().rstrip('\n')

        output_string = f'STDOUT:{stdout}\nSTDERR:{stderr}'
        if process.returncode!=0:
            output_string=output_string + f'\nProcess exited with code {process.returncode}'
        

        return output_string

    except Exception as e:
        return f"Error: {str(e)}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run python file in the file path, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The python file path needed to run the python file from, relative to the working directory.",
            ),
        },
    ),
)

    


    
