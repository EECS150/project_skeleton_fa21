module scaler (
    input clk,
    input [4:0] synth_shift, // left shift applied to synth_out before truncation and unsigned reranging
    input [13:0] synth_out, // 2s complement signed number
    output [9:0] code // unsigned number
);
    // Remove this line once you have implemented this module
    assign code = 0;
endmodule