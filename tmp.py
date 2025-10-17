from little_projects.pwd_store import PWD_generator, SQL_config, logging_setup

newpwd = PWD_generator.get_new_pwd("ask for new")
print(newpwd)

gestion = SQL_config.run("test")
print(gestion)
print(logging_setup())