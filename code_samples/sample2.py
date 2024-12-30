from sora import SoraInterpreter

sora_code = """
@sora{
name := Sora
age := 19

print: Basic Info
print: Name: $name
print: Age: $age

func greet(person)
    print: Hello $person!
end

func add_numbers(x, y)
    sum := x + y
    print: Sum of $x and $y is $sum
end

call greet(Sora)
call add_numbers(10, 20)

write_file output/soraa.txt, Name: $name, Age: $age

log: User profile created for $name and $age

show_vars
}

"""

interpreter = SoraInterpreter()
result = interpreter.parse_and_execute(sora_code)
print(result)
