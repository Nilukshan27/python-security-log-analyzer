
print("Python Security Log Analyzer")

failed_logins = 0
failed_by_ip = {}

with open("sample_security.log", "r") as file:
    logs = file.readlines()

for line in logs:
    if "event=login_failed" in line:
        failed_logins = failed_logins + 1

        ip = line.split("ip=")[1].strip()

        if ip in failed_by_ip:
            failed_by_ip[ip] = failed_by_ip[ip] + 1
        else:
            failed_by_ip[ip] = 1

print("Failed login attempts:", failed_logins)
print("Failures by IP:", failed_by_ip)

