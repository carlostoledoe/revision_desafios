def crear_archivo(template):
    with open('index.html', 'w') as f:
        return f.write(template)