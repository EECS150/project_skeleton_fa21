# Final Project Report
Upon completing the project, you will be required to submit a report detailing the progress of your EECS151/251A project.
The report should document your final circuit at a high level, and describe the design process that led you to your implementation.
We expect you to document and justify any tradeoffs you have made throughout the semester, as well as any pitfalls and lessons learned.
Additionally, you will document any optimizations made to your system, the system's performance in terms of area (resource use), clock period, and CPI, and other information that sets your project apart from other submissions.

The staff emphasizes the importance of the project report because it is the product you are able to take with you after completing the course.
All of your hard work should reflect in the project report.
Employers may (and have) ask to examine your EECS151/251A project report during interviews.
Put effort into this document and be proud of the results.
You may consider the report to be your medal for surviving EECS151/251A.

## Report Details
You will turn in your project report on Gradescope by the date specified in the [project overview](./overview.md).
The report should be around 8 pages total with around 5 pages of text and 3 pages of figures (± a few pages on each).
Ideally you should mix the text and figures together.

Here is a suggested outline and page breakdown for your report.
You do not need to strictly follow this outline, it is here just to give you an idea of what we will be looking for.

- **Project Functional Description and Design Requirements** (~0.5 page)
  - Describe the design objectives of your project. You don't need to go into details about the RISC-V ISA, but you need to describe the high-level design parameters (pipeline structure, memory hierarchy, etc.) for this particular CPU.
- **High-level organization** (~1 page)
  - How is your project broken down into pieces? (block diagram level-description)
  - We are most interested in how you broke the CPU datapath and control down into submodules, since the code for the later checkpoints will be pretty consistent across all groups. Please include an updated block diagram.
- **Detailed Description of Submodules** (~2 pages)
  - Describe how your circuits work. Concentrate here on novel or non-standard circuits.
  - Also, focus your attention on the parts of the design that were not supplied to you by the teaching staff. For instance, describe the details of your FIFOs, audio synthesizer, and any extra credit work.
  - Describe the behavior of your pipeline stages; what work is done in what stage? How do you handle data and control hazards? What forwarding paths did you implement?
- **Verification** (~1 page)
  - How did you test your CPU? Did you write any Verilog testbenches, assembly tests, or C tests to exercise any microarchitectural features or hazards? What provided tests did you use?
  - What bugs did you catch during verification and how did you fix them?
- **Status and Results** (~1-2 pages)
  - What is working and what is not?
  - At what frequency (50MHz or greater) does your design run? Do certain checkpoints work at a higher clock speed while others only run at 50 MHz?
  - Provide the **number of LUTs, SLICE registers, BRAMs, and DSP blocks** used by your design (from the utilization report in `build/impl/post_place_utilization.rpt`).
  - Optimization
    - If you have hit 100 MHz, provide the critical path and the CPI/max frequency when running `mmult`.
    - If you are evaluating multiple optimizations instead, provide the max frequency after each optimization you implemented, the `mmult` CPI, and the critical path.
      - What was the best design point for performance?
  - This section is particularly important for non-working designs (to help us assign partial credit).
- **Conclusion** (~0.5 page)
  - What have you learned from this experience? How would you do it different next time?

When we grade your report, we will grade for clarity, organization, and grammar.
Submit your report to the Gradescope assignment.
Only one partner needs to submit the final project report.

## Division of Labor Report
**This section is mandatory.**
Each team member will turn in a separate document for this part only.
The submission for this document will also be on Gradescope.

Things to write about (just a few sentences is sufficient, but up to half a page is OK):
- How did you organize yourselves as a team?
- Exactly who did what?
- Did both partners contribute equally?
- Please note your team number next to your name at the top.
