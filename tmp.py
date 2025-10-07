# from little_projects.pwd_store import main as pwdGen
from little_projects.pwd_store.main import PWD_generator

newpwd = PWD_generator()
print(newpwd.get_new_pwd())