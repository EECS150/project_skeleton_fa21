module dmem (
  input clk,
  input en,
  input [3:0] we,
  input [13:0] addr,
  input [31:0] din,
  output reg [31:0] dout
);
  reg [31:0] mem [16384-1:0];

  always @(posedge clk) begin
    if (en)
      dout <= mem[addr];
  end

  genvar i;
  generate for (i = 0; i < 4; i = i+1) begin
    always @(posedge clk) begin
      if (we[i] && en)
          mem[addr][i*8 +: 8] <= din[i*8 +: 8];
    end
  end endgenerate
endmodule
