// This is just an example to add RAM[0], RAM[1] into RAM[2]
// NOTE: This's not required for this course it's an example
// to practice the hack assembly language

@R0
D=M
@R1
D=M+D
@R2
M=D
(END)
	@END
	0;JMP
