module hello(A,B, CLK, Z);
    input A, B, CLK;
    output Z;

    reg D = 0;
    assign Z = D;

    always@(posedge CLK)
    begin
        D = A ^ B;
    end
endmodule