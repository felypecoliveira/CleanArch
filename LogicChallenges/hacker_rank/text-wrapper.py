def wrap(string, max_width):
    string_wraped = ""
    for i in range(0, len(string), max_width):
        string_wraped += string[i:i + max_width] + "\n"
    return string_wraped


resultado = wrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4)

print(resultado)
