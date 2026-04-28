import os

from mini_eda.parser import parse_logic_file
from mini_eda.verilog_exporter import generate_verilog_module
from mini_eda.file_utils import write_text_file


for file_name in os.listdir("circuits"):
    if file_name.endswith(".logic"):
        input_file_path = os.path.join("circuits", file_name)

        module_name = file_name.replace(".logic", "")

        output_file_path = os.path.join("outputs", module_name + ".v")

        circuit = parse_logic_file(input_file_path)

        verilog_code = generate_verilog_module(module_name, circuit)

        write_text_file(output_file_path, verilog_code)

        print("Generated Verilog file:")
        print(output_file_path)