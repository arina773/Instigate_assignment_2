from pathlib import Path
import hdlparse.verilog_parser as vlog
import sys


def generate_test_bench(inputs: list, outputs: list, module: str, filepath):
    x = f'`timescale 1ns/1ns\n\n' \
        f'module testbench;\n' \
        f'reg [15:0] {", ".join([a for a in inputs if a != "CLK"])} = 0;' \
        f'\nreg CLK = 0;\nwire [15:0] {", ".join(outputs)};\n' \
        f"{module} uut({', '.join([f'.{a}({a})' for a in inputs])}, {', '.join([f'.{a}({a})' for a in outputs])});\n" \
        f'always begin;\n' \
        f'\tCLK = ~CLK;\n' \
        f'\t#10;\nend\n' \
        f'initial begin\n' \
        f'\t$dumpfile("testbench.vcd");' \
        f'\n\t$dumpvars(0, testbench);\n' \
        f"\tA = 16'b10;\n\tB = 1;\n\t#10;\n\tA = 0;\n\tB = 15;\n\t#10;\n\t" \
        f"A = 0;\n\tB = 0;\n\t#10;\n\tA = 1;\n\tB = 1;\n\t#10;" \
        f'\n\t$display("Test Complete");\n' \
        f'\t$finish();\n' \
        f'end\n' \
        f'endmodule'

    with open('testbench.v', 'w') as f:
        f.write(x)
    return x


def parse_file(filepath: Path):
    vlog_ex = vlog.VerilogExtractor()
    with open(filepath, 'rt') as fh:
        code = fh.read()
    vlog_mods = vlog_ex.extract_objects_from_source(code)
    for m in vlog_mods:
        names = dict()
        for p in m.ports:
            if p.mode not in names.keys():
                names[p.mode] = [p.name]
            else:
                names[p.mode].append(p.name)
        print(generate_test_bench(names['input'], names['output'], m.name, filepath))
        print('-----TESTBENCH WAS CREATED-----')


# parse_file(Path("/home/arina/PycharmProjects/try/hello.v"))
parse_file(Path(sys.argv[1]))
