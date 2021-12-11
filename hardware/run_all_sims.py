from subprocess import run
from os import remove, makedirs, path
from shutil import rmtree
from typing import Tuple

RESULT_DIR = 'test_results'

def run_bench(name, cleanup, success_cond):
    print(f"Running make {name}: ", end='')
    cleanup()
    proc = run(['make', name], capture_output=True)
    stdout = proc.stdout.decode("utf-8")
    stderr = proc.stderr.decode("utf-8")
    with open(path.join(RESULT_DIR, f'{name.split("/")[-1]}.out'), "w") as fout:
        fout.write(stdout)
    with open(path.join(RESULT_DIR, f'{name.split("/")[-1]}.err'), "w") as ferr:
        ferr.write(stderr)
    if not success_cond(stdout):
        print(f"Failed")
        print(f"See {RESULT_DIR} for logs")
        exit(1)
    else:
        print("Passed")

def cleanup_isa_tests():
    rmtree('sim/isa', ignore_errors=True)

def cleanup_c_tests():
    rmtree('sim/c_tests', ignore_errors=True)

def get_grep_output(proc):
    stdout = proc.stdout.decode("utf-8").strip()
    return stdout.split('\n')

def isa_test_success_cond(_) -> bool:
    proc_failed = run('grep -r -i "failed" sim/isa/*.log', shell=True, capture_output=True)
    proc_timout = run('grep -r -i "timeout" sim/isa/*.log', shell=True, capture_output=True)
    tests_failed = get_grep_output(proc_failed) + get_grep_output(proc_timout)
    filtered_tests = list(filter(lambda l: ('fence_i' not in l) and l != '', tests_failed))
    if filtered_tests:
        return False, str(filtered_tests)
    return True, ''

def c_test_success_cond(_) -> bool:
    proc_failed = run('grep -r -i "failed" sim/c_tests/*.log', shell=True, capture_output=True)
    proc_timout = run('grep -r -i "timeout" sim/c_tests/*.log', shell=True, capture_output=True)
    tests_failed = get_grep_output(proc_failed) + get_grep_output(proc_timout)
    filtered_tests = list(filter(lambda l: l != '', tests_failed))
    if filtered_tests:
        return False, str(filtered_tests)
    return True, ''

def silent_remove_factory(testbench):
    def foo():
        try:
            remove(f'sim/{testbench}')
        except OSError:
            pass
    return foo

def main():
    makedirs(RESULT_DIR, exist_ok=True)
    run_bench("sim/cpu_tb.vpd", silent_remove_factory('cpu_tb.vpd'), lambda stdout: "All tests passed!" in stdout)
    run_bench("sim/asm_tb.vpd", silent_remove_factory('asm_tb.vpd'), lambda stdout: "ALL ASSEMBLY TESTS PASSED!" in stdout)
    run_bench("isa-tests", cleanup_isa_tests, isa_test_success_cond)
    run_bench("c-tests", cleanup_c_tests, c_test_success_cond)
    run_bench("sim/echo_tb.vpd", silent_remove_factory("echo_tb.vpd"), lambda stdout: "Test passed!" in stdout)
    run_bench("sim/uart_parse_tb.vpd", silent_remove_factory("uart_parse_tb.vpd"), lambda stdout: "CSR test PASSED! Strings matched." in stdout)
    run_bench("sim/bios_tb.vpd", silent_remove_factory("bios_tb.vpd"), lambda stdout: "BIOS testbench done! Num failed tests:          0" in stdout)
    run_bench("sim/synth_top_tb.vpd", silent_remove_factory("synth_top_tb.vpd"), lambda stdout: "failed" not in stdout)
    print("All tests passed!")

if __name__ == '__main__':
    main()
