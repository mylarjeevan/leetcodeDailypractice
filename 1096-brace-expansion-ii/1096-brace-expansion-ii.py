class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        i = 0
        n = len(expression)

        def product(a, b):
            return {x + y for x in a for y in b}

        def parse():
            nonlocal i

            # Result of comma-separated terms
            result = set()

            # Result of the current concatenation term
            current = {""}

            while i < n and expression[i] != "}":
                if expression[i] == ",":
                    # Union: finish current term
                    result |= current
                    current = {""}
                    i += 1

                elif expression[i] == "{":
                    i += 1          # skip '{'
                    inner = parse()
                    i += 1          # skip '}'

                    current = product(current, inner)

                else:
                    # Parse consecutive letters
                    start = i
                    while i < n and expression[i].isalpha():
                        i += 1

                    word = expression[start:i]
                    current = product(current, {word})

            return result | current

        return sorted(parse())