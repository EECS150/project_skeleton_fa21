module synth #(
    parameter N_VOICES = 1
)(
    input clk,
    input rst,
    input [N_VOICES-1:0] [23:0] carrier_fcws,
    input [23:0] mod_fcw,
    input [4:0] mod_shift,
    input [N_VOICES-1:0] note_en,

    output [13:0] sample,
    output sample_valid,
    input sample_ready
);
    // Remove these lines once you have implemented this module
    assign sample = 0;
    assign sample_valid = 0;
endmodule