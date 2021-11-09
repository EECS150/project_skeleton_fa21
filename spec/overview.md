# EECS 151/251A Project Specfication

## Introduction
The goal of this project is to familiarize EECS151/251A students with the methods and tools of digital design.
Working in a team of two, you will design and implement a 3-stage pipelined RISC-V CPU with a UART for tethering.
You will then integrate the audio and IO components from the labs and build a simple audio synth.
<!-- Afterwards, you will build a hardware accelerator to accelerate a small Convolutional Neural Network and do a system integration with your RISC-V CPU. -->

Finally, you will optimize your CPU for performance (maximizing the Iron Law) and cost (FPGA resource utilization).

You will use Verilog to implement this system, targeting the Xilinx PYNQ platform (a PYNQ-Z1 development board with a Zynq 7000-series FPGA).
The project will give you experience designing with RTL descriptions, resolving hazards in a simple pipeline, building interfaces, and teach you how to approach system-level optimization.

In tackling these challenges, your first step will be to map the high level specification to a design which can be translated into a hardware implementation.
After that, you will produce and debug that implementation.
These first steps can take significant time if you have not thought out your design prior to trying implementation.

As in previous semesters, your EECS151/251A project is probably the largest project you have faced so far here at Berkeley.
Good time management and good design organization is critical to your success.

## Checkpoints
The project is organized into several checkpoints to help you track your progress and receive feedback.
Here is a description of each checkpoint and how many weeks will be alloted to each one.
*Note*: this schedule is tentative and is subject to change.

### Checkpoint 1 (CPU Pipeline Diagram)
- **Due:** October 29, Friday (1 week)
- Read through the [checkpoint 1/2 spec](./checkpoint1.md)
- Draw a schematic of your processor's datapath and pipeline stages, and provide a brief writeup of your answers to [the Checkpoint 1 questions](./checkpoint1.md#checkpoint-1-questions).
- Push all of your IO-circuit Verilog modules that you have implemented in the labs to your assigned project Github repository in `hardware/src/io_circuits` (see [Integrate Designs From Labs](./checkpoint1.md#integrate-designs-from-labs)).
- Commit your design documents (block diagram + writeup) to `docs`.

### Checkpoint 1.5 (Decoder/Control Unit + ALU Implementation and Testbench)
- **Due:** November 12th, Friday (2 weeks)
- Implement your ALU and decoder/control unit in Verilog and write a testbench for each one.
  - Your ALU should implement all the arithmetic/logical operations supported by the RV32I ISA
  - Your control unit should take in an instruction and emit the control signals used for the rest of your CPU (e.g. `RegWrEn`, `ALUOp`, `MemWrEn`, ...)
    - You don't need to have a dedicated control unit module; it is OK to disperse the decoding of each control signal through your pipeline. If you do this, you don't need to write a unit test for your scattered boolean logic.
- This checkpoint **doesn't** involve an in-person checkoff; just commit your Verilog files to your team repo by the deadline.

### Checkpoint 2 (Pipelined RISC-V CPU)
- **Due:** November 19th, Friday (1 week)
- Implement a fully functional RISC-V processor core in Verilog. Your processor core should be able to run the `mmult` benchmark successfully.
- See the [checkpoint 1/2 spec](./checkpoint1.md)
- You have to get this checkpoint checked off with an FPGA TA either in lab or office hours; demonstrate the following in person:
    - Functionality of the BIOS (`sw` and `lw, lhu, lbu`)
    - Loading `mmult` using `hex_to_serial` into the IMEM/DMEM
    - Jumping to `mmult` from the BIOS, successful execution of `mmult` with the correct checksum, and jump back to BIOS
    - The measured CPI should be less than 1.2

### Checkpoint 3 (IO Integration, Sigma-Delta DAC, Safe Clock Crossing, Audio Synth)
- **Due:** December 3rd, Friday (2 weeks)
  - This checkpoint will be graded during the final checkoff
- Integrate the FPGA board buttons/LEDs as CPU readable/controllable IOs
- Build a simple sigma-delta DAC
- Build a memory-mapped hardware-accelerated audio synth with 2 NCOs and a digital mixer
  - Learn how to safely cross clock domains using a 4 way handshake
- *251A only*: extend the audio synth with support for polyphony
- See the [checkpoint 3 spec](./checkpoint3.md)

### Checkpoint 4 (Optimization)
- **Due:** December 3rd, Friday (2 weeks) (final day of class)
  - This checkpoint will be graded during the final checkoff
- Attempt to maximize the performance of your CPU by co-optimizing the CPI the clock frequency
- See the [checkpoint 4 spec](./checkpoint4.md)

### Final Checkoff
- Scheduled for **December 6th and 7th** (Monday and Tuesday, RRR week)
- Demonstration of your project and final check for functionality
- See the [final checkoff spec](./final_checkoff.md)

### Final Report
- **Due:** December 8th, Wednesday (RRR week)
- See the [final report spec](./final_report.md)

### Grading Rubric
- Functionality (80%) at the final project checkoff.
    - 10% from the `cpu_tb`, `asm_tb` (and your custom assembly tests), and the `isa-tests`.
    - 20% from the `c-tests`, `echo_tb`, and `bios_tb`.
    - 30% from the `bios` on the FPGA.
    - 20% from `mmult` on the FPGA.
    - 10% from the `user_io_test` on the FPGA.
    - 10% from `piano` on the FPGA.
- Optimization (10%) from the final report submission.
    - This score is contingent on implementing all the required functionality. An incomplete project will receive a zero in this category.
    - If you get your processor running at 100 MHz you will get full credit for optimization
    - If you instead evaluate different optimizations by recording the CPI / frequency / critical path for each trial, you will get full credit with 3 such evaluations
- Final report and style (10%) demonstrated throughout the project.
    - A final report that is well written and hits all the points in the [final report spec](./final_report.md) will get full credit.
    - Style relates to the cleanliness and clarity of your Verilog code. Your Verilog code should be readable. Your git repo should have no build artifacts and junk committed to it.
- Extra credit (up to 10%)
    - Credit based on additional functionality will be qualified on a case by case basis. Students interested in expanding the functionality of their project must meet with a GSI well ahead of time to be qualified for extra credit.
    - Point value will be decided by the course staff on a case by case basis, and will depend on the complexity of your proposal, the creativity of your idea, and relevance to the material taught.

## General Project Tips
Document your project as you go.
You should comment your Verilog and keep your diagrams up to date.
Aside from the final project report (you will need to turn in a report documenting your project), you can use your design documents to help the debugging process.

### Extra Credit
Finish the required features first.
Attempt extra features after everything works well.
**If your submitted project does not work by the final deadline, you will not get any credit for any extra credit features you have implemented.**

Teams that have completed the base set of requirements are eligible to receive extra credit worth up to 10% of the project grade by adding extra functionality and demonstrating it at the time of the final checkoff.
The following are suggested projects that may or may not be feasible in one week.

- Branch Predictor: Implement a two bit (or more complicated) branch predictor with a branch history table (BHT) to replace the naive 'always taken' predictor used in the project
- 5-Stage Pipeline: Add more pipeline stages and push the clock frequency past 100MHz
- Audio Recording: Capture mic input from the Pynq's microphone and wire it to the CPU via MMIO
- RISC-V M Extension: Extend the processor with a hardware multiplier and divider and verify its functionality by modifying `mmult` and your own set of assembly tests

When the time is right, if you are interested in implementing any of these, see the staff for more details.

### Local Development
You can build and run everything for this project from your laptop.
See the [local development doc](./local_dev.md) for the details.
