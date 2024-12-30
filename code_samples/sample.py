from src.interpreter import SoraInterpreter

# Example Sora code demonstrating type handling
sora_code = """
@sora{
# String variable (with quotes)
name := "Alice"
print: Hello $name!

# Integer variable (without quotes)
age := 25
print: Your age is $age

# Float variable
height := 5.8
print: Your height is $height

# Arithmetic with proper type handling
x := 10
y := 20
sum := x + y
print: $x + $y = $sum

# Show variables with proper type formatting
show_vars

# File operations with proper path handling
write_file output/test.txt, Name: $name, Age: $age
print: read_file output/test.txt
}
"""

interpreter = SoraInterpreter()
result = interpreter.parse_and_execute(sora_code)
print(result)