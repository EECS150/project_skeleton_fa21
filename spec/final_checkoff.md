# Final Checkoff
The final checkoff will be done in person in Cory 111 during a 20 minute appointment per team during RRR week.
We will send a signup sheet for appointment times through Piazza the week before RRR week.

Make sure you come to your appointment prepared:
  - Have your latest bitstream compiled and ready to go on an FPGA. You should demonstrate the bitstream with the highest `mmult` performance.
  - Have headphones attached to the FPGA audio jack.
  - Verify that your bitstream is working by loading a program (e.g. `mmult`) and running it.

You will be asked to demonstrate the following in person.

1. A clean repo; all files should be checked in and pushed to your team Github repo
1. Run through the testbenches and demonstrate that they all pass
    - `cpu_tb`
    - `asm_tb` (show your added assembly tests)
    - `isa-tests`
    - `c-tests`
    - `echo_tb`
    - `bios_tb`
    - Any other testbenches you wrote and want to demonstrate
    - We will record which tests passed and failed and incorporate these simulation results with your FPGA implementation for the final grade
2. Open `screen` and connect to the BIOS program. Demonstrate the `sw, sh, sb` and `lw, lhu, lbu` commands work using this sequence:
```
sw deadbeef 30000000
lw 30000000
lbu 30000003
lhu 30000002
```
3. Load the `mmult` program with `hex_to_serial`, open `screen`, and `jal` to `mmult`.
    - Demonstrate that you get the right checksum.
    - Show us your clock period by opening `build/impl/post_route_timing_summary.rpt`.
    - Calculate your CPI using the cycle and instruction counter values printed from running `mmult`.
4. Load the `user_io_test` program and jump to it
    - Demonstrate that your buttons FIFO works properly
    - Demonstrate that reading the switches and setting the LEDs work properly
5. Load the `piano` program and jump to it. Run the `piano` Python script.
    - Demonstrate that you can control the audio synthesizer parameters and play notes from the keyboard
    - 251A only: demonstrate polyphony
    - If the synthesizer doesn't work, what testbenches do work? (SD-DAC, `synth_tb`)
6. Are there any remaining bugs (functional or timing) in your processor?
7. What optimizations did you try and what were their outcomes?
8. Please submit your final report with all these details in the status section + your FPGA utilization
