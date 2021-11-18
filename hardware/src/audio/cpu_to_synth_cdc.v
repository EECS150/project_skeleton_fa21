module cpu_to_synth_cdc #(
    parameter N_VOICES = 1
)(
    input cpu_clk,
    input [N_VOICES-1:0] [23:0] cpu_carrier_fcws,
    input [23:0] cpu_mod_fcw,
    input [4:0] cpu_mod_shift,
    input [N_VOICES-1:0] cpu_note_en,
    input [4:0] cpu_synth_shift,
    input cpu_req,
    output cpu_ack,

    input synth_clk,
    output [N_VOICES-1:0] [23:0] synth_carrier_fcws,
    output [23:0] synth_mod_fcw,
    output [4:0] synth_mod_shift,
    output [N_VOICES-1:0] synth_note_en,
    output [4:0] synth_synth_shift
);
    // Remove these lines once you have implemented this module
    assign cpu_ack = 0;
    assign synth_carrier_fcws = 0;
    assign synth_mod_fcw = 0;
    assign synth_mod_shift = 0;
    assign synth_note_en = 0;
    assign synth_synth_shift = 0;
endmodule