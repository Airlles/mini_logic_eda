def parse_signal_list(logic_line, section_label):
    raw_signal_text = logic_line.replace(section_label, "")
    signal_names = raw_signal_text.split(",")

    clean_signal_names = []

    for signal_name in signal_names:
        clean_signal_names.append(signal_name.strip())

    return clean_signal_names


def parse_gate_line(logic_line):
    gate_tokens = logic_line.split()

    arrow_index = gate_tokens.index("->")

    gate = {
        "name": gate_tokens[1],
        "type": gate_tokens[2],
        "inputs": gate_tokens[3:arrow_index],
        "output": gate_tokens[arrow_index + 1]
    }

    return gate


def parse_logic_file(file_path):
    input_signals = []
    gates = []
    output_signals = []

    with open(file_path, "r") as logic_file:
        logic_file_lines = logic_file.readlines()

    for logic_line in logic_file_lines:
        logic_line = logic_line.strip()

        if logic_line == "":
            continue

        if logic_line.startswith("IN:"):
            input_signals = parse_signal_list(logic_line, "IN:")

        elif logic_line.startswith("GATE"):
            gate = parse_gate_line(logic_line)
            gates.append(gate)

        elif logic_line.startswith("OUT:"):
            output_signals = parse_signal_list(logic_line, "OUT:")

    parsed_circuit = {
        "inputs": input_signals,
        "gates": gates,
        "outputs": output_signals
    }

    return parsed_circuit