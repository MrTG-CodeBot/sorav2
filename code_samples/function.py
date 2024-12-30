from src.interpreter import SoraInterpreter

# Example demonstrating function features
sora_code = """
@sora{
# Basic variable types
name := "Alice"
age := 25
height := 5.8

# Function with string parameter
func greet(person)
    print: Hello $person!
end

# Function with arithmetic
func add_numbers(x, y)
    sum := x + y
    print: Sum of $x and $y is $sum
end

# Function with multiple operations
func process_data(name, age)
    print: Processing data for $name
    next_age := age + 1
    print: Next year age will be $next_age
end

# Call functions
call greet(name)
call add_numbers(10, 20)
call process_data(name, age)

# Show final variables
show_vars
}
"""

interpreter = SoraInterpreter()
result = interpreter.parse_and_execute(sora_code)
print("\nProgram Output:")
print("-" * 50)
print(result)