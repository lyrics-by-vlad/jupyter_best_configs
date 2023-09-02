# The project is aimed at
Improve user experience when working with `.ipynb` files in Jupyter Notebook IDE as the most popular IDE in Data Science 🤟, and if you want the simpliest way to:
1. Automatically get clear `.py` file – script which would look much better then 'Download as Python' version from IDE (and would also be [RECONVERTABLE](https://github.com/lyrics-by-vlad/any_project_template/tree/main) back to `.ipynb`) – at every time you save your `.ipynb` file. 
> Usefully, e.g. when you want to run such a file from CLI / another script or to commit a version of it, etc.
2. [Optional usage] Empty outputs, execution_count and other metadata from `.ipynb` automatically right before the time you save it.
> Usefully, e.g. when you want to automatize launch and relaunch your notebooks on server or just to puplish/send it anywhere.
3. [Optional usage] Add initial pre-configured extensions for fresh installation of jupyter-contrib-nbextensions.
> For example, to see execution time for any cell of code, 'freeze' or 'block' cells, set initial cells, hide all cells of code, highlight selected words, watch live previews for MD-cells, minimize tracebacks, toogle line numbers and more very useful add-ons.
  
# Usage (tested on Linux and Windows)
At first, just clone or download this repository.  

1. To reach the first aim, just copy `jupyter_notebook_config.py` file (with replace if needed) into '.jupyter' directory (usually, you can find it in your home directory).
1. To reach the second point, you should just have `jupyter_pre_save_hook_trigger.json` file with the following content:
   ```
   {
       "permission_allowed": true
   }
   ``` 
   **nearby (in the same directory with) that notebooks which you allow to use this feature**.
   
1. To reach the third point, **you should have installed jupyter-contrib-nbextensions package in the working environment where jupyter-notebook is**, then copy (with replace if needed) 'nbconfig' directory and `jupyter_notebook_config.json` file into '.jupyter' directory.
