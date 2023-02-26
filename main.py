from pathlib import Path
import hdlparse.verilog_parser as vlog
import sys

def generate_test_bench(inputs: list, outputs: list, module: str, filepath):
    x = f'`timescale 1ns/1ns\n\nmodule testbench;\nreg {", ".join(inputs)} = 0;\nwire {", ".join(outputs)};\n' \
        f'{module} uut({", ".join(inputs)}, {", ".join(outputs)});\nalways begin\n' \
        f'\tCLK = ~CLK;\n\t#10;\nend\nalways begin\ninitial begin\n\t$dumpfile("testbench.vcd");' \
        f"\n\t$dumpvars(0, testbench);\n\t{{A, B}} =2'b00; #20;\n\t{{A, B}} =2'b01; #20;\n\t{{A, B}} =2'b10; #20;\n\t" \
        f'$display("Test Complete");\n\t$finish()\nend\nendmodule'
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
        print('-----TEST BENCH WAS CREATED-----')

parse_file(Path("C:/Users/Arina/PycharmProjects/Intigate_assignment_2/hello.v"))
# parse_file(Path(sys.argv[1]))mm