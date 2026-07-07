def transpile_source(code: str) -> str:

    lines = code.split("\n")

    output = []
    indent = 0

    for raw in lines:
        line = raw.strip()

        if not line:
            continue

        # KEYWORDS
        line = line.replace("छापा", "print")
        line = line.replace("कार्य", "def")
        line = line.replace("परत", "return")
        line = line.replace("जोपर्यंत", "while")
        line = line.replace("जर", "if")
        line = line.replace("घे", "")

        # OPEN BLOCK
        if "{" in line:
            line = line.replace("{", ":")
            output.append("    " * indent + line)
            indent += 1
            continue

        # CLOSE BLOCK
        if "}" in line:
            indent = max(indent - 1, 0)
            continue

        # NORMAL LINE
        output.append("    " * indent + line)

    return "\n".join(output)