# EECS 151/251A Project Specfication

## Introduction
The goal of this project is to familiarize EECS151/251A students with the methods and tools of digital design.
Working in a team of two, you will design and implement a 3-stage pipelined RISC-V CPU with a UART for tethering.
You will then integrate the audio and IO components from the labs and build a small beat detection accelerator.
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

### Checkpoint 3 (IO Integration, Sigma-Delta DAC, Safe Clock Crossing, Audio Synth)
- **Due:** December 3rd, Friday (2 weeks)
- Integrate the FPGA board buttons/LEDs as CPU readable/controllable IOs
- Build a simple sigma-delta DAC
- Build a memory-mapped hardware-accelerated audio synth with 2 NCOs and a digital mixer
  - Learn how to safely cross clock domains using a 4 way handshake
- *251A only*: extend the audio synth with support for polyphony
- See the [checkpoint 3 spec](./checkpoint3.md)

### Checkpoint 4 (Optimization)
- **Due:** December 3rd, Friday (2 weeks) (final day of class)
- See the [checkpoint 4 spec](./checkpoint4.md)

### Final Checkoff
- Scheduled for **December 6th and 7th** (Monday and Tuesday, RRR week)
- Demonstration of your project and final check for functionality
- See the [final checkoff spec](./final_checkoff.md)

### Final Report
- **Due:** December 8th, Wednesday (RRR week)
- See the [final report spec](./final_report.md)

## General Project Tips
Document your project as you go.
You should comment your Verilog and keep your diagrams up to date.
Aside from the final project report (you will need to turn in a report documenting your project), you can use your design documents to help the debugging process.

Finish the required features first.
Attempt extra features after everything works well.
**If your submitted project does not work by the final deadline, you will not get any credit for any extra credit features you have implemented.**

### Local Development
You can build and run everything for this project from your laptop.
See the [local development doc](./local_dev.md) for the details.
