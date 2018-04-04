IDEAL
MODEL SMALL
STACK 100h

DATASEG
	
	data db 101B
	key db  110B
	inc_value db 87

CODESEG

encrypt:
		
		xor dl, key ; xor 110B with the value that stored in the bl register
		add dl, inc_value ; add value so it will print an ASCII value and not something weirdo
		mov bl, dl ; assign the xored value in another register so it can be printed
		mov ah, 2 ; stdout instruction
		int 21h ; call the interrupt stack
		ret
		
decrypt:
		
		xor bl, key ; reverse the xor operation
		sub bl, inc_value ; substract the previously added value
		mov dl, bl ; assign the reverse value to the dl register so it can be printed
		mov ah, 2 ; stdout instruction
		int 21h ; call the interrupt stack
		ret
		
start:
		mov ax, @data
		mov ds, ax
		mov bl, data ; assign 101B to bl, B indicated that the value is passed in binary
		; prints the value before the xor operation
		mov dl, bl
		mov ah, 2
		int 21h
		
		; add some space between the outputs
		mov ah, 1
		int 21h
		
		call encrypt ; calls the encrypt function
		
		; add some space between the outputs
		mov ah, 1
		int 21h
		
		call decrypt ; calls the decrypt function
		

exit:
	mov ah, 4ch
	int 21h

END start