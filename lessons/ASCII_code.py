"""Learning the ASCII code behind each characters"""

ord("A")
ord("A") < ord("a")
chr(ord("A"))
ord(chr(65))

hex(90)
#0x5a, 0x denotes hexadecimal

"""
\"	Double quote (")
\'	Single quote (')
\t	Tab
\n	New Line
e.g print("Hello\nworld\n!!!")
\Uxxxxxxxx	32-bit unicode character
\\	Backslash (\)
"""

#f-strings
course: int = 110
print(f"I am in COMP{ course } right now!")
print("I am in COMP" + str(course) + " right now!")