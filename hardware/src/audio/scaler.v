module scaler (
    input clk,
    input [4:0] synth_shift, // left shift applied to synth_out before truncation and unsigned reranging
    input [13:0] synth_out, // 2s complement signed number
    output [9:0] code // unsigned number
);
    wire [13:0] synth_out_shifted;
    assign synth_out_shifted = synth_out << synth_shift;
    wire [10:0] synth_out_sign_ext;
    assign synth_out_sign_ext = {synth_out_shifted[13], synth_out_shifted[13:4]};
    wire [10:0] synth_out_balanced;
    assign synth_out_balanced = synth_out_sign_ext + 11'd512;
    assign code = synth_out_balanced[9:0];
endmodule
