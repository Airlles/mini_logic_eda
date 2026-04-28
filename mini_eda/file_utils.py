def write_text_file(output_path, text):
    with open(output_path, "w") as output_file:
        output_file.write(text)