// PUT The Height of the rectangle in R0  RAM[0]



@R0
D=M

@n
M=D

@SCREEN
D=A

@addr
M=D

@i
M=0

(LOOP)
	@i
	D=M
	@n
	D=D-M
	@END
	D;JGT
	

	@addr
	A=M
	M=-1

	@32
	D=A
	
	@i
	M=M+1	

	@addr
	M=M+D

	@LOOP
	0;JMP

(END)
@END
0;JMP		
	



