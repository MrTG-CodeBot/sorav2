from sora import SoraInterpreter

sora_code = """
@sora{

name := "Alice"
age := 25
height := 5.8

print: Basic Info:
print: Name: $name
print: Age: $age
print: Height: $height

x := 10
y := 20
sum := x + y
print: Sum: $sum

show_vars
}
"""

interpreter = SoraInterpreter()
result = interpreter.parse_and_execute(sora_code)
print(result)
