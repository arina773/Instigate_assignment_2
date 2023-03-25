module hello(O, A, B, CLK, Z);
    input [15:0] A;
    input [15:0] B;
    input CLK;
    output [15:0] O;
    output [15:0] Z;

    reg [15:0] Z_r = 0;
    reg [15:0] O_r = 0;

    assign Z = Z_r;
    assign O = O_r;

    always@(posedge CLK)
    begin
        Z_r = A ^ B;
        O_r = A & B;
    end
endmodule
