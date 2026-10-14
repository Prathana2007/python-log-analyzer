def analyze_logs(logs):
    errors = []

    for line in logs:
        if "ERROR" in line:
            errors.append(line)

    return errors


if __name__ == "__main__":
    sample_logs = [
        "INFO: Application started",
        "ERROR: Database connection failed",
        "INFO: Application stopped"
    ]

    errors = analyze_logs(sample_logs)

    print("Total errors:", len(errors))
    for error in errors:
        print(error)
