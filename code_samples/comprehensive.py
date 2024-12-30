from src.interpreter import SoraInterpreter

# Comprehensive example demonstrating all Sora features
sora_code = """
@sora{
# 1. Variable Types and Arithmetic
name := "John Doe"
age := 30
height := 5.11
balance := 1000.50

print: User Profile:
print: Name: $name
print: Age: $age
print: Height: $height
print: Balance: $balance

# 2. Arithmetic Operations
initial_balance := 1000
deposit := 500.50
withdrawal := 200
final_balance := initial_balance + deposit - withdrawal
print: Banking:
print: Initial: $initial_balance
print: After transactions: $final_balance

# 3. String Operations
first_name := "John"
last_name := "Doe"
full_name := first_name + " " + last_name
print: Generated full name: $full_name

# 4. File Operations
# Save user profile
write_file data/profile.txt, Name: $name\nAge: $age\nBalance: $balance
print: Profile saved. Content:
print: $read_file data/profile.txt

# Save transaction log
write_file data/transactions.txt, Deposit: +$deposit\nWithdrawal: -$withdrawal\nFinal Balance: $final_balance
print: Transaction log:
print: $read_file data/transactions.txt

# 5. Logging
log: User profile created for $name
log: Transactions processed for account

# 6. Variable State
print: Current variable state:
show_vars
}
"""

# Create interpreter and run the code
interpreter = SoraInterpreter()
result = interpreter.parse_and_execute(sora_code)
print("\nProgram Output:")
print("-" * 50)
print(result)