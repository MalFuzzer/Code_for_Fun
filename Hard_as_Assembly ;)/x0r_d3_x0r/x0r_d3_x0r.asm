IDEAL
MODEL small
STACK 100h
DATASEG

; view the output in the TD debugger - Seek for the values that defined in the "list" variable (eg. ASCii values: W V U T S) in the memory (eg. CPU window under the "view" tab)

	list dw 87, 86, 85, 84, 83
	count equ 05h

CODESEG

start:
	 mov ax, @data
	 mov ds, ax
	 mov dx, count - 1 ; assign the value of count variable (-1 beacuse 0 + 4 = 5) to to the dx register
	 
	 back:
		mov cx, dx ; assign the value in dx register to cx register for looping purposes
		mov si, offset list ; assign the offset of list to si register
		
	 again:
		mov ax, [si]
		cmp ax, [si + 2]
		call x0r_th3_x0r
		xchg ax, [si + 2] ; swap operation 1
		call x0r_th3_x0r
		xchg ax, [si] ; swap operation 2
		call x0r_th3_x0r
		
	 go:
		; si incrementation so the elements in the list variable can be accessed via index
		inc si
		inc si
		loop  again ; loop the rythem ;)
		dec dx ; decrement dx so the loop will end after 5 iterations
		jnz back ; jump to back function if the ZF is not 1
		call exit ; calls the exit function
		
x0r_th3_x0r:
	xor ax, 14
	ret
		
exit:
	mov ah, 4ch
	mov al, 0h
	int 21h
END start