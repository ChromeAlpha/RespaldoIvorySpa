input_file = "data.json"
output_file = "data_clean.json"

with open(input_file, "r", encoding="utf-8-sig") as f:  # utf-8-sig ignora el BOM
    content = f.read()

with open(output_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Archivo limpio guardado como", output_file)
