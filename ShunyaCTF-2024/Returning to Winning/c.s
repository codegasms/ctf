
c:     file format elf64-x86-64


Disassembly of section .init:

0000000000401000 <.init>:
  401000:	48 83 ec 08          	sub    $0x8,%rsp
  401004:	48 8b 05 d5 2f 00 00 	mov    0x2fd5(%rip),%rax        # 403fe0 <fopen@plt+0x2f40>
  40100b:	48 85 c0             	test   %rax,%rax
  40100e:	74 02                	je     401012 <putchar@plt-0x1e>
  401010:	ff d0                	call   *%rax
  401012:	48 83 c4 08          	add    $0x8,%rsp
  401016:	c3                   	ret

Disassembly of section .plt:

0000000000401020 <putchar@plt-0x10>:
  401020:	ff 35 ca 2f 00 00    	push   0x2fca(%rip)        # 403ff0 <fopen@plt+0x2f50>
  401026:	ff 25 cc 2f 00 00    	jmp    *0x2fcc(%rip)        # 403ff8 <fopen@plt+0x2f58>
  40102c:	0f 1f 40 00          	nopl   0x0(%rax)

0000000000401030 <putchar@plt>:
  401030:	ff 25 ca 2f 00 00    	jmp    *0x2fca(%rip)        # 404000 <fopen@plt+0x2f60>
  401036:	68 00 00 00 00       	push   $0x0
  40103b:	e9 e0 ff ff ff       	jmp    401020 <putchar@plt-0x10>

0000000000401040 <puts@plt>:
  401040:	ff 25 c2 2f 00 00    	jmp    *0x2fc2(%rip)        # 404008 <fopen@plt+0x2f68>
  401046:	68 01 00 00 00       	push   $0x1
  40104b:	e9 d0 ff ff ff       	jmp    401020 <putchar@plt-0x10>

0000000000401050 <fclose@plt>:
  401050:	ff 25 ba 2f 00 00    	jmp    *0x2fba(%rip)        # 404010 <fopen@plt+0x2f70>
  401056:	68 02 00 00 00       	push   $0x2
  40105b:	e9 c0 ff ff ff       	jmp    401020 <putchar@plt-0x10>

0000000000401060 <printf@plt>:
  401060:	ff 25 b2 2f 00 00    	jmp    *0x2fb2(%rip)        # 404018 <fopen@plt+0x2f78>
  401066:	68 03 00 00 00       	push   $0x3
  40106b:	e9 b0 ff ff ff       	jmp    401020 <putchar@plt-0x10>

0000000000401070 <fgetc@plt>:
  401070:	ff 25 aa 2f 00 00    	jmp    *0x2faa(%rip)        # 404020 <fopen@plt+0x2f80>
  401076:	68 04 00 00 00       	push   $0x4
  40107b:	e9 a0 ff ff ff       	jmp    401020 <putchar@plt-0x10>

0000000000401080 <gets@plt>:
  401080:	ff 25 a2 2f 00 00    	jmp    *0x2fa2(%rip)        # 404028 <fopen@plt+0x2f88>
  401086:	68 05 00 00 00       	push   $0x5
  40108b:	e9 90 ff ff ff       	jmp    401020 <putchar@plt-0x10>

0000000000401090 <setvbuf@plt>:
  401090:	ff 25 9a 2f 00 00    	jmp    *0x2f9a(%rip)        # 404030 <fopen@plt+0x2f90>
  401096:	68 06 00 00 00       	push   $0x6
  40109b:	e9 80 ff ff ff       	jmp    401020 <putchar@plt-0x10>

00000000004010a0 <fopen@plt>:
  4010a0:	ff 25 92 2f 00 00    	jmp    *0x2f92(%rip)        # 404038 <fopen@plt+0x2f98>
  4010a6:	68 07 00 00 00       	push   $0x7
  4010ab:	e9 70 ff ff ff       	jmp    401020 <putchar@plt-0x10>

Disassembly of section .text:

00000000004010b0 <.text>:
  4010b0:	31 ed                	xor    %ebp,%ebp
  4010b2:	49 89 d1             	mov    %rdx,%r9
  4010b5:	5e                   	pop    %rsi
  4010b6:	48 89 e2             	mov    %rsp,%rdx
  4010b9:	48 83 e4 f0          	and    $0xfffffffffffffff0,%rsp
  4010bd:	50                   	push   %rax
  4010be:	54                   	push   %rsp
  4010bf:	45 31 c0             	xor    %r8d,%r8d
  4010c2:	31 c9                	xor    %ecx,%ecx
  4010c4:	48 c7 c7 6f 12 40 00 	mov    $0x40126f,%rdi
  4010cb:	ff 15 07 2f 00 00    	call   *0x2f07(%rip)        # 403fd8 <fopen@plt+0x2f38>
  4010d1:	f4                   	hlt
  4010d2:	66 2e 0f 1f 84 00 00 	cs nopw 0x0(%rax,%rax,1)
  4010d9:	00 00 00 
  4010dc:	0f 1f 40 00          	nopl   0x0(%rax)
  4010e0:	c3                   	ret
  4010e1:	66 2e 0f 1f 84 00 00 	cs nopw 0x0(%rax,%rax,1)
  4010e8:	00 00 00 
  4010eb:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)
  4010f0:	b8 50 40 40 00       	mov    $0x404050,%eax
  4010f5:	48 3d 50 40 40 00    	cmp    $0x404050,%rax
  4010fb:	74 13                	je     401110 <fopen@plt+0x70>
  4010fd:	b8 00 00 00 00       	mov    $0x0,%eax
  401102:	48 85 c0             	test   %rax,%rax
  401105:	74 09                	je     401110 <fopen@plt+0x70>
  401107:	bf 50 40 40 00       	mov    $0x404050,%edi
  40110c:	ff e0                	jmp    *%rax
  40110e:	66 90                	xchg   %ax,%ax
  401110:	c3                   	ret
  401111:	66 66 2e 0f 1f 84 00 	data16 cs nopw 0x0(%rax,%rax,1)
  401118:	00 00 00 00 
  40111c:	0f 1f 40 00          	nopl   0x0(%rax)
  401120:	be 50 40 40 00       	mov    $0x404050,%esi
  401125:	48 81 ee 50 40 40 00 	sub    $0x404050,%rsi
  40112c:	48 89 f0             	mov    %rsi,%rax
  40112f:	48 c1 ee 3f          	shr    $0x3f,%rsi
  401133:	48 c1 f8 03          	sar    $0x3,%rax
  401137:	48 01 c6             	add    %rax,%rsi
  40113a:	48 d1 fe             	sar    %rsi
  40113d:	74 11                	je     401150 <fopen@plt+0xb0>
  40113f:	b8 00 00 00 00       	mov    $0x0,%eax
  401144:	48 85 c0             	test   %rax,%rax
  401147:	74 07                	je     401150 <fopen@plt+0xb0>
  401149:	bf 50 40 40 00       	mov    $0x404050,%edi
  40114e:	ff e0                	jmp    *%rax
  401150:	c3                   	ret
  401151:	66 66 2e 0f 1f 84 00 	data16 cs nopw 0x0(%rax,%rax,1)
  401158:	00 00 00 00 
  40115c:	0f 1f 40 00          	nopl   0x0(%rax)
  401160:	f3 0f 1e fa          	endbr64
  401164:	80 3d ed 2e 00 00 00 	cmpb   $0x0,0x2eed(%rip)        # 404058 <stdout@GLIBC_2.2.5+0x8>
  40116b:	75 13                	jne    401180 <fopen@plt+0xe0>
  40116d:	55                   	push   %rbp
  40116e:	48 89 e5             	mov    %rsp,%rbp
  401171:	e8 7a ff ff ff       	call   4010f0 <fopen@plt+0x50>
  401176:	c6 05 db 2e 00 00 01 	movb   $0x1,0x2edb(%rip)        # 404058 <stdout@GLIBC_2.2.5+0x8>
  40117d:	5d                   	pop    %rbp
  40117e:	c3                   	ret
  40117f:	90                   	nop
  401180:	c3                   	ret
  401181:	66 66 2e 0f 1f 84 00 	data16 cs nopw 0x0(%rax,%rax,1)
  401188:	00 00 00 00 
  40118c:	0f 1f 40 00          	nopl   0x0(%rax)
  401190:	f3 0f 1e fa          	endbr64
  401194:	eb 8a                	jmp    401120 <fopen@plt+0x80>

; win function
  401196:	55                   	push   %rbp
  401197:	48 89 e5             	mov    %rsp,%rbp
  40119a:	48 83 ec 10          	sub    $0x10,%rsp
  40119e:	48 8d 05 63 0e 00 00 	lea    0xe63(%rip),%rax        # 402008 <fopen@plt+0xf68>
  4011a5:	48 89 c7             	mov    %rax,%rdi
  4011a8:	e8 93 fe ff ff       	call   401040 <puts@plt>
  4011ad:	48 8d 05 85 0e 00 00 	lea    0xe85(%rip),%rax        # 402039 <fopen@plt+0xf99>
  4011b4:	48 89 c6             	mov    %rax,%rsi
  4011b7:	48 8d 05 7d 0e 00 00 	lea    0xe7d(%rip),%rax        # 40203b <fopen@plt+0xf9b>
  4011be:	48 89 c7             	mov    %rax,%rdi
  4011c1:	e8 da fe ff ff       	call   4010a0 <fopen@plt>
  4011c6:	48 89 45 f8          	mov    %rax,-0x8(%rbp)
  4011ca:	48 83 7d f8 00       	cmpq   $0x0,-0x8(%rbp)
  4011cf:	75 11                	jne    4011e2 <fopen@plt+0x142>
  4011d1:	48 8d 05 6c 0e 00 00 	lea    0xe6c(%rip),%rax        # 402044 <fopen@plt+0xfa4>
  4011d8:	48 89 c7             	mov    %rax,%rdi
  4011db:	e8 60 fe ff ff       	call   401040 <puts@plt>
  4011e0:	eb 3d                	jmp    40121f <fopen@plt+0x17f>
  4011e2:	48 8d 05 73 0e 00 00 	lea    0xe73(%rip),%rax        # 40205c <fopen@plt+0xfbc>
  4011e9:	48 89 c7             	mov    %rax,%rdi
  4011ec:	e8 4f fe ff ff       	call   401040 <puts@plt>
  4011f1:	eb 0b                	jmp    4011fe <fopen@plt+0x15e>
  4011f3:	0f be 45 f7          	movsbl -0x9(%rbp),%eax
  4011f7:	89 c7                	mov    %eax,%edi
  4011f9:	e8 32 fe ff ff       	call   401030 <putchar@plt>
  4011fe:	48 8b 45 f8          	mov    -0x8(%rbp),%rax
  401202:	48 89 c7             	mov    %rax,%rdi
  401205:	e8 66 fe ff ff       	call   401070 <fgetc@plt>
  40120a:	88 45 f7             	mov    %al,-0x9(%rbp)
  40120d:	80 7d f7 ff          	cmpb   $0xff,-0x9(%rbp)
  401211:	75 e0                	jne    4011f3 <fopen@plt+0x153>
  401213:	48 8b 45 f8          	mov    -0x8(%rbp),%rax
  401217:	48 89 c7             	mov    %rax,%rdi
  40121a:	e8 31 fe ff ff       	call   401050 <fclose@plt>
  40121f:	c9                   	leave
  401220:	c3                   	ret
  401221:	55                   	push   %rbp
  401222:	48 89 e5             	mov    %rsp,%rbp
  401225:	48 83 ec 40          	sub    $0x40,%rsp
  401229:	48 8b 05 20 2e 00 00 	mov    0x2e20(%rip),%rax        # 404050 <stdout@GLIBC_2.2.5>
  401230:	b9 00 00 00 00       	mov    $0x0,%ecx
  401235:	ba 02 00 00 00       	mov    $0x2,%edx
  40123a:	be 00 00 00 00       	mov    $0x0,%esi
  40123f:	48 89 c7             	mov    %rax,%rdi
  401242:	e8 49 fe ff ff       	call   401090 <setvbuf@plt>
  401247:	48 8d 05 2a 0e 00 00 	lea    0xe2a(%rip),%rax        # 402078 <fopen@plt+0xfd8>
  40124e:	48 89 c7             	mov    %rax,%rdi
  401251:	b8 00 00 00 00       	mov    $0x0,%eax
  401256:	e8 05 fe ff ff       	call   401060 <printf@plt>

; gets call
  40125b:	48 8d 45 c0          	lea    -0x40(%rbp),%rax
  40125f:	48 89 c7             	mov    %rax,%rdi
  401262:	b8 00 00 00 00       	mov    $0x0,%eax
  401267:	e8 14 fe ff ff       	call   401080 <gets@plt>

  40126c:	90                   	nop
  40126d:	c9                   	leave
  40126e:	c3                   	ret
  40126f:	55                   	push   %rbp
  401270:	48 89 e5             	mov    %rsp,%rbp
  401273:	b8 00 00 00 00       	mov    $0x0,%eax
  401278:	e8 a4 ff ff ff       	call   401221 <fopen@plt+0x181>
  40127d:	b8 00 00 00 00       	mov    $0x0,%eax
  401282:	5d                   	pop    %rbp
  401283:	c3                   	ret

Disassembly of section .fini:

0000000000401284 <.fini>:
  401284:	48 83 ec 08          	sub    $0x8,%rsp
  401288:	48 83 c4 08          	add    $0x8,%rsp
  40128c:	c3                   	ret
