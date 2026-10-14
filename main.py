
print("Python Security Log Analyzer")

failed_logins = 0

with open("sample_security.log", "r") as file:
    logs = file.readlines()

for line in logs:
    if "event=login_failed" in line:
        failed_logins = failed_logins + 1

print("Failed login attempts:", failed_logins)
