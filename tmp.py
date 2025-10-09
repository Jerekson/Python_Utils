from little_projects.pwd_store import PWD_generator,

newpwd = PWD_generator.get_new_pwd("ask for new")
print(newpwd)

gestion = SQL_config.run("test")
print(gestion)