import configparser
config = configparser.RawConfigParser()
config.read('.\IntelligentViewing_MSI.properties')

print(config)