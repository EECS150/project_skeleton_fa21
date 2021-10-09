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

### Checkpoint 0 (CPU Pipeline Diagram)
- **Due:** October 22, Friday (1 week)
- Draw a schematic of your processor's datapath and pipeline stages, and provide a brief writeup of your answers to the questions in ~\ref{sec:chkpt1_questions}.
- Push all of your IO-circuit Verilog modules that you have implemented in the labs to your assigned project Github repository in `hardware/src/io_circuits` (see [Integrate Designs From Labs](./checkpoint1.md#integrate-designs-from-labs)).
- Commit your design documents (block diagram + writeup) to `docs`.

### Checkpoint 0.5 (Decoder + ALU Implementation and Testbench)
- **Due:** October 29, Friday (1 week)

### Checkpoint 1 (Pipelined RISC-V CPU)
- **Due:** November 12, Friday (2 weeks)
- Implement a fully functional RISC-V processor core in Verilog. Your processor core should be able to run the \textbf{mmult} demo successfully.
- See the [checkpoint 1 spec](./checkpoint1.md)

### Checkpoint 2 (IO / Audio Circuit Integration)
- **Due:** November 19, Friday (1 week)
- Integrate the FPGA board buttons/LEDs as CPU controllable IOs
- Integrate the NCO and DAC as memory mapped devices

### Checkpoint 3 (BPM Detector)
- **Due:** December 3rd, Friday (2 weeks) (final day of class)
- Implement a memory-mapped hardware-accelerated BPM detector

### Checkpoint 4 (Optimization)
- **Due:** December 3rd, Friday (2 weeks) (final day of class)

### Final Checkoff
- Scheduled for **December 6th and 7th** (Monday and Tuesday, RRR week)
- Demonstration of your project and final check for functionality

### Final Report
- **Due:** December 8th, Wednesday (RRR week)

## General Project Tips
Document your project as you go.
You should comment your Verilog and keep your diagrams up to date.
Aside from the final project report (you will need to turn in a report documenting your project), you can use your design documents to help the debugging process.

Finish the required features first.
Attempt extra features after everything works well.
**If your submitted project does not work by the final deadline, you will not get any credit for any extra credit features you have implemented.**
