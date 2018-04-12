IDEAL
MODEL small
STACK 100h
DATASEG

; view the output in the TD debugger - Seek for the values that defined in the "list" variable (eg. ASCii values: W V U T S) in the memory (eg. CPU window under the "view" tab)
; the goal is to xor the above value (W V U T S) and unxor it back

	list dw 87, 86, 85, 84, 83 ; values in decimal, hex values (57, 56, 55, 54, 53)
	xored dw 5 dup (0) ; xored data
	xored_1 dw 5 dup (0) ; reverted data
	unxored dw 5 dup (0) ; reverted data

CODESEG

start:
	mov ax, @data
	mov ds, ax
	mov cx, 5
	lea si, [list] ; load the address space of list

	; prints before the xor
;	mov ah, 2
;	int 21h

again_x0r:
	mov dx, [si] ; pointer si to dx so it can load the index effectively (eg. inc si * 2 = the next index to take from the xored_1 array for unxoring)

	; inc by 2 for the indexing of the elements in the list var "array" that comes from SI and initialized to DX
	inc si
	inc si

	; inc by 2 for the indexing of the elements in the xored var "array"
	inc di
	inc di

	call x0r ; call the x0r_d3_x0r function
	
	dec cx ; for the For-Loop counter
	jnz again_x0r ; looping until the ZF=1 (CX = 0)
	
	call th3_x0r_start ; calls the unxor operation
	
		
x0r:
	xor dx, 14h ; xor the current value in the ax register with the value decimal value key 14 (E)
	mov [xored + di], dx
	mov [xored_1 + di], dx
	ret


th3_x0r_start:
	xor di, di
	xor dx, dx
	xor ax, ax
	xor bx, bx
	xor cx, cx
;	mov ax, @data
;	mov ds, ax
	mov cx, 5
	lea si, [xored_1 + 2] ; load the address space of si (in addition to 2 so it will load the right first value like in the xoring operation)
	
again_th3_x0r:
	mov dx, [si] ; pointer si to dx so it can load the index effectively (eg. inc si * 2 = the next index to take from the xored_1 array for unxoring)

	; inc by 2 for the indexing of the elements in the list var "array"
	inc si
	inc si

	; inc by 2 for the indexing of the elements in the xored var "array"
	inc di
	inc di

	call th3_x0r ; call the x0r_d3_x0r function
	dec cx ; for the For-Loop counter
	jnz again_th3_x0r
	
	call exit ; terminates the program
		

th3_x0r:
	xor dx, 14h ; xor the current value in the ax register with the value decimal value key 14 (E)
	mov [unxored + di], dx
	ret
		
exit:
	mov ah, 4ch
	int 21h
END start