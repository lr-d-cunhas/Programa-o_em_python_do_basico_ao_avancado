from importlib import metadata

print(metadata.version('pip'))

metadados_pip = metadata.metadata('pip')

print(list(metadados_pip))

print(metadados_pip['Project-URL'])

# Quantidade de arquivos no arquivo / pacote que você quer verificar
print(len(metadata.files('pip')))

print(metadata.requires('pip'))
