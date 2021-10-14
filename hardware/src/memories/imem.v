module imem (
  input clk,
  input ena,
  input [3:0] wea,
  input [13:0] addra,
  input [31:0] dina,
  input [13:0] addrb,
  output reg [31:0] doutb
);
  reg [31:0] mem [16384-1:0];

  always @(posedge clk) begin
      doutb <= mem[addrb];
  end

  genvar i;
  generate for (i = 0; i < 4; i = i+1) begin
    always @(posedge clk) begin
      if (wea[i] && ena)
          mem[addra][i*8 +: 8] <= dina[i*8 +: 8];
    end
  end endgenerate
endmodule
