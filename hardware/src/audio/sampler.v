module sampler (
    input clk,
    input rst,
    input synth_valid,
    input [9:0] scaled_synth_code,
    output synth_ready,
    output pwm_out
);
    // Remove these lines once you have implemented this module
    assign synth_ready = 0;
    assign pwm_out = 0;
endmodule