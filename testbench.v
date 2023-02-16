`timescale 1ps/1ps
`include "C:\Users\Arina\PycharmProjects\Intigate_assignment_2\hello.v"
module testbench;
reg A, B, CLK = 0;
wire Z;
hello uut(A, B, CLK, Z);
always begin
	CLK = ~CLK;
	#10;
end
always begin
initial begin
	$dumpfile("testbench.vcd");
	$dumpvars(0, testbench);
	{A, B} =2'b00, #20;
	{A, B} =2'b00, #20;
	{A, B} =2'b00, #20;
	$display("Test Complete");
end