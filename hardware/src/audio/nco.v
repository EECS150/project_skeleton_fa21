module nco(
    input clk,
    input rst,
    input [23:0] fcw,
    input next_sample,
    output [13:0] code
);
    assign code = 0;
endmodule
