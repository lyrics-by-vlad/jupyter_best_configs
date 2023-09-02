import os
from subprocess import run
from sys import executable, platform, exit
from inspect import getsourcefile
from json import load
try:
    import jupytext
except ModuleNotFoundError:
    try:
        run(
            f'{executable} -m pip install jupytext', 
            executable=('/bin/bash' if 'linux' in platform else None), 
            shell=True, 
            check=True
        )
        print()
    except:
        exit(
            "\nPlease, install jupytext to your current environment with the following command \n\n"
            "                   pip install jupytext\n"
            "OR, for example, \n"
            "                   poetry add jupytext\n"
        )

c = get_config()

def pre_save(
    model, 
    path, 
    contents_manager
):
    
    """This is the pre-save hook function made for clearing .ipynb outputs before saving them"""
    
    if model['type'] != 'notebook':
        return
    
    main_cond_json = 'jupyter_pre_save_hook_trigger.json'
    # ^ should be always nearby saving notebook to allow the pre-save function
    
    path_to_this_script = os.path.normpath(getsourcefile(lambda: 0))
    separated_path_to_this_script = path_to_this_script.split(os.sep)
    root_path = os.sep.join(
        separated_path_to_this_script[:separated_path_to_this_script.index('.jupyter')]
    )
    
    path_to_this_notebook = os.path.join(root_path, path)
    this_notebook_dir, this_notebook_name = os.path.split(path_to_this_notebook)
    
    if main_cond_json in os.listdir(this_notebook_dir):
        
        with open(os.path.join(this_notebook_dir, main_cond_json)) as pre_save_hook_trigger:
            
            pre_save_hook_trigger = load(pre_save_hook_trigger)
            
            if 'permission_allowed' in pre_save_hook_trigger.keys() and (
               pre_save_hook_trigger['permission_allowed']):
                
                for cell in model['content']['cells']:
                    
                    if cell['cell_type'] != 'code':
                        continue
                    
                    cell['outputs'] = []
                    cell['execution_count'] = None
                    if 'metadata' in cell.keys():
                        if 'ExecuteTime' in cell['metadata']:
                            
                            del cell['metadata']['ExecuteTime']
                
                if 'metadata' in model['content'].keys():
                    if 'hide_input' in model['content']['metadata'].keys():
                        
                        model['content']['metadata']['hide_input'] = False

def post_save(
    model, 
    os_path, 
    contents_manager
):
    
    """This is the post-save hook function made for converting .ipynb files into .py scripts"""
    
    if model['type'] != 'notebook':
        return
    
    notebook_dir, notebook_name = os.path.split(os_path)
    
    run(
        f'{executable} -m jupytext --to py "{notebook_name}"', 
        executable=('/bin/bash' if 'linux' in platform else None), 
        shell=True, 
        check=True, 
        cwd=notebook_dir
    )
    
    script_dir, script_name = notebook_dir, notebook_name.replace('.ipynb', '.py')
    
    special_dir_for_scripts = os.path.join(notebook_dir, '.py')
    os.makedirs(special_dir_for_scripts, exist_ok=True)
    os.replace(
        os.path.join(script_dir, script_name), 
        os.path.join(special_dir_for_scripts, script_name)
    )

c.FileContentsManager.pre_save_hook = pre_save
c.FileContentsManager.post_save_hook = post_save
