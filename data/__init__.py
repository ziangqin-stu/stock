import os


# paths
project_name = "stock"
curPath = os.path.abspath(os.path.dirname(__file__))
project_path = curPath[:curPath.find(project_name+"\\")+len(project_name+"\\")]
data_path = os.path.join(project_path, 'data')
core_path = os.path.join(project_path, 'core')
