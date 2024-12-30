from src.interpreter import SoraInterpreter

# Basic example focusing on core features
sora_code = """
@sora{
# Basic variable assignment
name := "Alice"
age := 25
height := 5.8

# Simple printing
print: Basic Info:
print: Name: $name
print: Age: $age
print: Height: $height

# Basic arithmetic
x := 10
y := 20
sum := x + y
print: Sum: $sum

# Show variables
show_vars
}
"""

interpreter = SoraInterpreter()
result = interpreter.parse_and_execute(sora_code)
print(result)