# Checkpoint 4: Optimization

This optimization checkpoint is lumped with the final checkoff.
This part of the project is designed to give students freedom to implement the optimizations of their choosing to improve the performance of their processor.

The optimization goal for this project is to minimize the **execution time** of the `mmult` program, as defined by the 'Iron Law' of Processor Performance.

<p align=center>
  <img src="https://render.githubusercontent.com/render/math?math=\frac{\text{Time}}{\text{Program}} = \frac{\text{Instructions}}{\text{Program}} \times \frac{\text{Cycles}}{\text{Instruction}} \times \frac{\text{Time}}{\text{Cycle}}" />
</p>

The number of instructions is fixed, but you have freedom to change the CPI and the CPU clock frequency.
Often you will find that you will have to sacrifice CPI to achieve a higher clock frequency, but there also will exist opportunities to improve one or both of the variables without compromises.

## Grading on Optimization: Frequency vs. CPI
### Performance
#### 100 MHz Option
You will receive a full credit for the final checkpoint if you can push your clock frequency of your working `cpu` implementation to 100 MHz.
You must demonstrate that your processor has a working BIOS, can load and execute `mmult` (CPI does not need to be less than 1.2).

The bare minimum is that you should improve the achievable frequency of your existing implementation from Checkpoint 2.

#### Multiple Optimizations Option
*Alternatively*, full credit can also be awarded on effort, in particular if you're able to evaluate different design trade-off points (at least three) between frequency and CPI of `mmult` (especially if you have implemented some interesting optimization for CPI and increasing the frequency further would degrade the performance instead of helping).

Also note that your final optimized design does not need to be a three-stage pipeline.

### FPGA Utilization
A **very minor** component of the optimization grade is based total FPGA resource utilization, with the best designs using as few resources as possible.
Credit for your area optimizations will be calculated using a cost function.
At a high level, the cost function will look like:

`Cost = (C_LUT x N_LUT) + (C_BRAM x N_BRAM) + (C_FF x N_FF) + (C_DSP x N_DSP)`

where `C_LUT`, `C_BRAM`, `C_FF`, and `C_DSP` are constant value weights that will be decided upon based on how much each resource that you use should cost, and the `N_*` values are the counts of each resource used (from the `impl/post_place_utilization.rpt` report).
As part of your final grade we will evaluate the cost of your design based on this metric.

Keep in mind that cost is only one very small component of your project grade. Correct functionality is far more important.

## Clock Generation and Changing Clock Frequency
Open up `z1top.v`.
There's top level input called `CLK_125MHZ_FPGA`.
It's a 125 MHz clock signal, which is used to derive the CPU clock.

Scrolling down, there's an instantiation of `clocks` (`clocks.v`), which is a wrapper module of PLL (phase locked loop) primitives on the FPGA.
This is a circuit that can create a new clock from an existing clock with a user-specified multiply-divide ratio.

The `CLKIN1` (line 47) input clock of the PLL is driven by the 125 MHz `CLK_125MHZ_FPGA`.
The frequency of `CLKOUT0` (line 39) is calculated as:

`CLKOUT0_freq = CLKIN1_freq * ((CPU_CLK_CLKFPOUT_MULT) / (CPU_CLK_DIVCLK_DIVIDE * CPU_CLK_CLKOUT_DIVIDE)`

<p align=center>
  <img src="https://render.githubusercontent.com/render/math?math=\text{CLKOUT0\_freq} = 125 \text{ MHz} \cdot \frac{34}{5 \cdot 17} = 50 \text{ MHz}" />
</p>

To change the CPU clock frequency you must:
1. Change the parameters (`CPU_CLK_CLKFBOUT_MULT`, `CPU_CLK_DIVCLK_DIVIDE`, `CPU_CLK_CLKOUT_DIVIDE`) in `z1top` according to the table below
2. Change the `CPU_CLOCK_FREQ` parameter in `z1top` to match the PLL parameters
- You must do **both** of these things for the CPU and UART to function properly

This table specifies the ideal PLL parameters to get certain output frequencies.

<div align="center">

| Frequency | DIVCLK_DIVIDE | CLKFBOUT_MULT | CLKOUT0_DIVIDE |
| --------- | ------------- | ------------- | -------------- |
| 50 MHz    | 5             | 34            | 17             |
| 60 MHz    | 5             | 36            | 15             |
| 65 MHz    | 5             | 39            | 15             |
| 70 MHz    | 5             | 42            | 15             |
| 75 MHz    | 5             | 33            | 11             |
| 80 MHz    | 5             | 48            | 15             |
| 85 MHz    | 5             | 34            | 10             |
| 90 MHz    | 5             | 36            | 10             |
| 95 MHz    | 5             | 38            | 10             |
| 100 MHz   | 5             | 36            | 9              |

</div>

## Critical Path Identification
After running `make impl`, timing analysis will be performed to determine the critical path(s) of your design.
The timing tools will automatically figure out the CPU's clock timing constraint based on the PLL parameters you set in `z1top.v`.

The critical path can be found by looking in:

`hardware/build/impl/post_route_timing_summary.rpt`

Look for the paths within your CPU.

For each timing path look for the attribute called 'slack'.
Slack describes how much extra time the combinational delay of the path has before the rising edge of the receiving clock.
It is a setup time attribute.
Positive slack means that this timing path resolves and settles before the rising edge of the clock, and negative slack indicates a setup time violation.

There are some common delay types that you will encounter.
`LUT` delays are combinational delays through a LUT.
`net` delays are from wiring delays. They come with a fanout (`fo`) attribute which you should aim to minimize.
Notice that your logic paths are usually dominated by routing delay; as you optimize, you should reach the point where the routing and LUT delays are about equal portions of the total path delay.

### Schematic View
To visualize the path, you can open Vivado (`make vivado`), and open a DCP (Design Checkpoint) file (`File` → `Checkpoint` → `Open`).
The DCP is in `build/impl/z1top_routed.dcp`.

Re-run timing analysis with `Reports` → `Timing` → `Report Timing Summary`.
Use the default options and click `OK`.
Navigate (on the bottom left) to `Intra-Clock Paths` → `cpu_clk` → `Setup`.

You can double-click any path to see the logic elements along it, or you can right-click and select `Schematic` to see a schematic view of the path.

The paths in post-PAR timing report may be hard to decipher since Vivado does some optimization to move/merge registers and logic across module boundaries.
It may help to look at the post-synth DCP in `build/synth/z1top.dcp`.
You can also use the [keep_hierarchy attribute](https://www.xilinx.com/support/answers/54778.html) to prevent Vivado from moving registers and logic across module boundaries (although this may degrade QoR).

```verilog
// in z1top.v
(* keep_hierarchy="yes" *) cpu #( ) cpu ( );
```

### Finding Actual Critical Paths
When you first check the timing report with a 50 MHz clock, you might not see your 'actual' critical path.
50 MHz is easy to meet and the tools will only attempt to optimize routing until timing is met, and will then stop.

You should increase the clock frequency slowly and rerun `make impl` until you fail to meet timing.
At this point, the critical paths you see in the report are the 'actual' ones you need to work on.

Don't try to increase the clock speed up all the way to 100 MHz initially, since that will cause the routing tool to give up even before it tried anything.

## Optimization Tips
As you optimize your design, you will want to try running `mmult` on your newly optimized designs as you go along.
You don't want to make a lot of changes to your processor, get a better clock speed, and then find out you broke something along the way.

You will find that sacrificing CPI for a better clock speed is a good bet to make in some cases, but will worsen performance in others.
You should **keep a record** of all the different optimizations you tried and the effect they had on CPI and minimum clock period; this will be useful for the final report when you have to justify your optimization and architecture decisions.

There is no limit to what you can do in this section.
The only restriction is that you have to run the original, unmodified `mmult` program so that the number of instructions remain fixed.
You can add as many pipeline stages as you want, stall as much or as little as desired, add a branch predictor, or perform any other optimizations.
If you decide to do a more advanced optimization (like a 5 stage pipeline), ask the staff to see if you can use it as extra credit in addition to the optimization.

Keep notes of your architecture modifications in the process of optimization.
Consider, but don't obsess, over area usage when optimizing (keep records though).
