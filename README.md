# Python Based Mini EDA Tool for Gate Level Simulation and Verilog Generation

A small educational EDA style tool written in Python that parses custom gate level `.logic` files, builds an internal circuit representation, generates synthesizable Verilog, simulates truth tables, and reports simplified timing information for combinational digital circuits.

This project was built to connect digital logic, Verilog RTL, parsing, simulation, timing analysis, and hardware automation into one practical workflow.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Main Flow](#main-flow)
3. [Why I Built This](#why-i-built-this)
4. [Features](#features)
5. [Supported Gates](#supported-gates)
6. [Example Input File](#example-input-file)
7. [Generated Verilog Example](#generated-verilog-example)
8. [Generated Truth Table Example](#generated-truth-table-example)
9. [Generated Timing Report Example](#generated-timing-report-example)
10. [Toy Delay Library](#toy-delay-library)
11. [Project Structure](#project-structure)
12. [File Descriptions](#file-descriptions)
13. [Installation](#installation)
14. [Usage](#usage)
15. [Example Parser Output](#example-parser-output)
16. [.logic File Format](#logic-file-format)
17. [Design Decisions](#design-decisions)
18. [Error Checking](#error-checking)
19. [Testing](#testing)
20. [Example Circuits](#example-circuits)
21. [What This Project Demonstrates](#what-this-project-demonstrates)
22. [What This Project Is Not](#what-this-project-is-not)
23. [Limitations](#limitations)
24. [Future Roadmap](#future-roadmap)
25. [Skills Used](#skills-used)
26. [Author](#author)

---

## Project Overview

Modern digital design tools read circuit descriptions, analyze connectivity, generate or transform hardware representations, verify behavior, and report timing information. This project recreates a small educational version of that flow.

The tool reads a simple text based circuit format:

```text
IN: A, B

GATE X1 XOR A B -> SUM
GATE A1 AND A B -> CARRY

OUT: SUM, CARRY
```

Then it produces structured circuit data, generated Verilog, truth table output, and a simplified timing report.

---

## Main Flow

```text
.logic file
    ↓
Python parser
    ↓
Internal circuit representation
    ↓
Verilog generator
    ↓
Logic simulator
    ↓
Truth table generator
    ↓
Timing reporter
```

---

## Why I Built This

I built this project to strengthen my understanding of hardware design automation, digital logic, Verilog generation, circuit representation, and debugging workflows used in silicon design environments.

The goal was not to build a real commercial synthesis tool. The goal was to build a small but complete educational EDA style pipeline that shows how a circuit can be parsed, represented, translated, simulated, checked, and analyzed.

This project helped me practice:

1. Python file parsing
2. Gate level circuit representation
3. Verilog RTL generation
4. Truth table based verification
5. Simplified timing analysis
6. Parser validation and debugging
7. Hardware focused software design
8. Clean project documentation and testing

---

## Features

| Feature | Status | Description |
|---|---:|---|
| Custom `.logic` input format | Complete | Reads simple gate level circuit descriptions |
| Parser | Complete | Extracts inputs, gates, gate inputs, gate outputs, and output signals |
| Internal circuit representation | Complete | Stores circuits using Python dictionaries and structured data |
| Verilog generation | Complete | Generates synthesizable Verilog modules |
| Logic simulation | Complete | Evaluates circuit outputs for a given input combination |
| Truth table generation | Complete | Generates all possible input combinations and output values |
| Simplified timing analysis | Complete | Assigns toy gate delays and reports critical output paths |
| Error checking | Complete | Detects invalid gates, missing arrows, malformed lines, and bad connectivity |
| CLI support | Complete | Runs parser, Verilog generation, truth table, and timing from the terminal |
| pytest tests | Complete | Tests parser, exporter, simulator, and timing behavior |

---

## Supported Gates

| Gate | Description | Verilog Operator |
|---|---|---|
| AND | Logic AND | `&` |
| OR | Logic OR | `|` |
| XOR | Logic XOR | `^` |
| NOT | Logic inversion | `~` |
| NAND | Inverted AND | `~(...)` |
| NOR | Inverted OR | `~(...)` |
| MUX | 2 to 1 multiplexer | `sel ? b : a` |

---

## Example Input File

File:

```text
circuits/half_adder.logic
```

Content:

```text
IN: A, B

GATE X1 XOR A B -> SUM
GATE A1 AND A B -> CARRY

OUT: SUM, CARRY
```

This describes a half adder.

The XOR gate generates the sum output.

The AND gate generates the carry output.

---

## Generated Verilog Example

The tool generates:

```verilog
module half_adder(
    input A,
    input B,
    output SUM,
    output CARRY
);

assign SUM = A ^ B;
assign CARRY = A & B;

endmodule
```

---

## Generated Truth Table Example

```text
A B | SUM CARRY
0 0 | 0   0
0 1 | 1   0
1 0 | 1   0
1 1 | 0   1
```

---

## Generated Timing Report Example

```text
Timing Report

Output: SUM
Critical path: A -> X1 -> SUM
Delay: 4 units

Output: CARRY
Critical path: A -> A1 -> CARRY
Delay: 3 units

Worst output: SUM
Critical delay: 4 units
```

The timing numbers are not real standard cell timing numbers. They come from a simplified gate delay model used for educational timing analysis.

---

## Toy Delay Library

| Gate | Delay |
|---|---:|
| NOT | 1 unit |
| NAND | 2 units |
| NOR | 2 units |
| AND | 3 units |
| OR | 3 units |
| XOR | 4 units |
| MUX | 5 units |

---

## Project Structure

```text
mini_logic_eda/
│
├── circuits/
│   ├── half_adder.logic
│   ├── full_adder.logic
│   └── mux2.logic
│
├── mini_eda/
│   ├── __init__.py
│   ├── circuit.py
│   ├── parser.py
│   ├── verilog_exporter.py
│   ├── simulator.py
│   ├── truth_table.py
│   ├── timing.py
│   ├── errors.py
│   └── cli.py
│
├── tests/
│   ├── test_parser.py
│   ├── test_verilog_exporter.py
│   ├── test_simulator.py
│   ├── test_truth_table.py
│   └── test_timing.py
│
├── outputs/
│   ├── half_adder.v
│   ├── half_adder_truth_table.txt
│   ├── half_adder_timing.txt
│   └── debug_summary.txt
│
├── README.md
├── requirements.txt
└── main.py
```

---

## File Descriptions

| File | Purpose |
|---|---|
| `circuits/half_adder.logic` | Example half adder circuit |
| `circuits/full_adder.logic` | Example full adder circuit |
| `circuits/mux2.logic` | Example 2 to 1 mux circuit |
| `mini_eda/parser.py` | Parses `.logic` files into structured circuit data |
| `mini_eda/circuit.py` | Defines circuit and gate representation |
| `mini_eda/verilog_exporter.py` | Generates synthesizable Verilog |
| `mini_eda/simulator.py` | Simulates logic behavior for one input case |
| `mini_eda/truth_table.py` | Generates full truth tables |
| `mini_eda/timing.py` | Performs simplified critical path timing analysis |
| `mini_eda/errors.py` | Handles parser and validation errors |
| `mini_eda/cli.py` | Handles command line options |
| `tests/` | Contains pytest regression tests |
| `outputs/` | Stores generated Verilog, truth tables, and timing reports |
| `main.py` | Main program entry point |

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/mini_logic_eda.git
cd mini_logic_eda
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

For v0.1, the only required dependency may be:

```text
pytest
```

---

## Usage

Run all outputs for a circuit:

```bash
python main.py circuits/half_adder.logic --all
```

Generate Verilog only:

```bash
python main.py circuits/half_adder.logic --verilog
```

Generate a truth table only:

```bash
python main.py circuits/half_adder.logic --truth-table
```

Generate a timing report only:

```bash
python main.py circuits/half_adder.logic --timing
```

Parse and print circuit structure:

```bash
python main.py circuits/half_adder.logic --parse
```

---

## Example Parser Output

```text
Inputs: ['A', 'B']

Gates:
{'name': 'X1', 'type': 'XOR', 'inputs': ['A', 'B'], 'output': 'SUM'}
{'name': 'A1', 'type': 'AND', 'inputs': ['A', 'B'], 'output': 'CARRY'}

Outputs: ['SUM', 'CARRY']
```

---

## .logic File Format

The `.logic` format is intentionally simple.

A circuit has three main sections:

```text
IN: input1, input2, input3

GATE gate_name gate_type input1 input2 -> output

OUT: output1, output2
```

Example:

```text
IN: A, B, CIN

GATE X1 XOR A B -> XOR_AB
GATE X2 XOR XOR_AB CIN -> SUM
GATE A1 AND A B -> CARRY_AB
GATE A2 AND XOR_AB CIN -> CARRY_CIN
GATE O1 OR CARRY_AB CARRY_CIN -> COUT

OUT: SUM, COUT
```

---

## Design Decisions

### Simple Text Format

The project uses a custom `.logic` format to keep the first version focused on the parsing, simulation, and generation engine.

### Gate Level Representation

Each gate is represented internally with:

```python
{
    "name": "X1",
    "type": "XOR",
    "inputs": ["A", "B"],
    "output": "SUM"
}
```

This makes it easier to pass the same circuit data into the Verilog exporter, simulator, truth table generator, and timing analyzer.

### Combinational Only

v0.1 supports combinational circuits only. Sequential elements such as flip flops, registers, and finite state machines are planned for a future version.

### Simplified Timing

The timing analyzer uses assigned toy delay values for each gate type. This is not real static timing analysis, but it demonstrates arrival time calculation, critical path thinking, and timing report generation.

---

## Error Checking

The parser and validation logic check for common circuit input issues.

Examples include:

| Error Type | Example |
|---|---|
| Unknown gate type | `GATE G1 BRO A B -> Y` |
| Missing arrow | `GATE G1 AND A B Y` |
| Missing output | `GATE G1 AND A B ->` |
| Missing input signal | A gate uses a signal that was never declared or generated |
| Duplicate driven wire | Two gates both drive the same output wire |
| Empty circuit | Missing `IN`, `GATE`, or `OUT` information |
| Wrong NOT input count | `GATE N1 NOT A B -> Y` |
| Invalid MUX input count | `GATE M1 MUX SEL A -> Y` |

Example error message:

```text
ERROR: Unknown gate type 'BRO' on line 4.
Allowed gates: AND, OR, NOT, NAND, NOR, XOR, MUX.
```

---

## Testing

Run all tests:

```bash
pytest
```

Run a specific test file:

```bash
pytest tests/test_parser.py
```

The test suite checks:

1. Parser behavior for valid circuits
2. Parser rejection of malformed circuits
3. Verilog generation output
4. Logic simulation correctness
5. Truth table correctness
6. Timing report calculations

---

## Example Circuits

### Half Adder

Inputs:

```text
A, B
```

Outputs:

```text
SUM, CARRY
```

Logic:

```text
SUM = A XOR B
CARRY = A AND B
```

### Full Adder

Inputs:

```text
A, B, CIN
```

Outputs:

```text
SUM, COUT
```

Logic:

```text
SUM = A XOR B XOR CIN
COUT = A B + CIN(A XOR B)
```

### 2 to 1 Multiplexer

Inputs:

```text
SEL, A, B
```

Output:

```text
Y
```

Logic:

```text
Y = SEL ? B : A
```

---

## What This Project Demonstrates

This project demonstrates a small hardware automation workflow from circuit description to generated output.

It shows practical experience with:

1. Python scripting
2. File parsing
3. String processing
4. Data structures
5. Digital logic
6. Gate level netlists
7. Verilog generation
8. Logic simulation
9. Truth table verification
10. Simplified timing analysis
11. Debugging invalid circuit descriptions
12. pytest based regression testing
13. CLI based engineering workflow

---

## What This Project Is Not

This is not a commercial EDA tool.

It does not perform real synthesis, placement, routing, formal verification, or real static timing analysis.

It does not use real standard cell libraries, parasitics, process corners, clock constraints, or physical design data.

The purpose is educational. It is a small project that builds intuition for how EDA style tools represent, check, transform, and analyze digital circuits.

---

## Limitations

Current v0.1 limitations:

1. Combinational circuits only
2. No flip flop or latch support
3. No FSM support
4. No real standard cell mapping
5. No real static timing analysis
6. No Verilog testbench generation yet
7. No graphical circuit viewer
8. No SPICE level transistor simulation
9. No placement and routing
10. No support for buses or vectors yet

---

## Future Roadmap

Planned future improvements:

| Version | Feature | Purpose |
|---|---|---|
| v0.2 | D flip flop support | Add sequential circuit support |
| v0.2 | FSM support | Generate and simulate simple state machines |
| v0.2 | Verilog testbench generation | Add stronger verification workflow |
| v0.2 | Combinational loop detection | Detect invalid feedback paths |
| v0.3 | SPICE like CMOS exporter | Generate simple inverter, NAND, and NOR transistor networks |
| v0.3 | Graph visualization | Show circuit connectivity visually |
| v0.3 | Yosys integration | Feed generated Verilog into open source synthesis |
| v0.4 | SystemVerilog output | Generate cleaner RTL style modules |
| v0.4 | Basic bus support | Support multi bit signals and vectors |

---

## Skills Used

| Category | Skills |
|---|---|
| Programming | Python, file I/O, functions, dictionaries, lists, error handling |
| Hardware | Digital logic, gates, truth tables, combinational circuits |
| RTL | Verilog modules, ports, wires, assign statements |
| Verification | Truth tables, expected versus actual behavior, pytest |
| Timing | Gate delays, arrival time, critical path |
| Tooling | Git, GitHub, terminal, CLI workflow |
| EDA Concepts | Netlists, circuit representation, code generation, parser validation |

---

## Author

Hani Ahmed  
Electrical Engineering Student  
Toronto Metropolitan University
