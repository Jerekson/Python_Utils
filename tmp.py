# from little_projects.pwd_store import main as pwdGen
# from little_projects.pwd_store.main import PWD_generator

'''
newpwd = PWD_generator()
print(newpwd.get_new_pwd())
'''



from little_projects.pwd_store import PWD_generator, SQL_config

newpwd = PWD_generator.get_new_pwd("ask for new")
print(newpwd)

gestion = SQL_config.run("test")
print(gestion)