from src.interpreter import SoraInterpreter

sora_code = """
@sora{
# Create some data
user := "Bob"
score := 95
date := "2024-01-20"

# Write to different files
write_file scores/daily.txt, User: $user\nScore: $score\nDate: $date
write_file scores/summary.txt, $user achieved $score points

# Read and display file contents
print: Daily Report:
print: read_file scores/daily.txt

print: Summary:
print: read_file scores/summary.txt

# Log the operation
log: Score recorded for $user
}
"""

interpreter = SoraInterpreter()
result = interpreter.parse_and_execute(sora_code)
print(result)