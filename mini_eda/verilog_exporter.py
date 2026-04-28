def generate_assign_statement(gate):
    gate_type = gate["type"]
    gate_inputs = gate["inputs"]
    gate_output = gate["output"]

    if gate_type == "AND":
        expression = " & ".join(gate_inputs)

    elif gate_type == "OR":
        expression = " | ".join(gate_inputs)

    elif gate_type == "XOR":
        expression = " ^ ".join(gate_inputs)

    elif gate_type == "NOT":
        expression = "~" + gate_inputs[0]

    elif gate_type == "NAND":
        expression = "~(" + " & ".join(gate_inputs) + ")"

    elif gate_type == "NOR":
        expression = "~(" + " | ".join(gate_inputs) + ")"

    else:
        expression = "UNKNOWN_GATE"

    verilog_line = f"assign {gate_output} = {expression};"

    return verilog_line


def generate_verilog_module(module_name, circuit):
    verilog_lines = []

    verilog_lines.append(f"module {module_name}(")

    port_lines = []

    for input_signal in circuit["inputs"]:
        port_lines.append(f"    input {input_signal}")

    for output_signal in circuit["outputs"]:
        port_lines.append(f"    output {output_signal}")

    for index in range(len(port_lines)):
        if index == len(port_lines) - 1:
            verilog_lines.append(port_lines[index])
        else:
            verilog_lines.append(port_lines[index] + ",")

    verilog_lines.append(");")
    verilog_lines.append("")

    for gate in circuit["gates"]:
        assign_statement = generate_assign_statement(gate)
        verilog_lines.append(assign_statement)

    verilog_lines.append("")
    verilog_lines.append("endmodule")

    verilog_text = "\n".join(verilog_lines)

    return verilog_text