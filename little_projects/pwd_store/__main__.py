from .pwd_store import PWD_generator, SQL_config

print("auto start __main__")

newpwd = PWD_generator.get_new_pwd("ask for new")
print(newpwd)

gestion = SQL_config.run("test")
print(gestion)
