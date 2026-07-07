class Runtime:

    def __init__(self):
        self.env = {}
        self.output = []


    def log(self, v):
        self.output.append(str(v))


    # ---------------- EVALUATE ----------------

    def evaluate(self, v):

        if isinstance(v, (int, float)):
            return v

        if isinstance(v, str):

            if v.isdigit():
                return int(v)

            if v in self.env:
                return self.env[v]

            return v

        if isinstance(v, tuple):

            if v[0] in ["+","-","*","/","<",">","=="]:

                a = self.evaluate(v[1])
                b = self.evaluate(v[2])

                if v[0] == "+": return a + b
                if v[0] == "-": return a - b
                if v[0] == "*": return a * b
                if v[0] == "/": return a / b
                if v[0] == "<": return a < b
                if v[0] == ">": return a > b
                if v[0] == "==": return a == b

        return v


    # ---------------- EXECUTE BLOCK ----------------

    def execute_block(self, block):

        for node in block:

            if node is None:
                continue


            # BREAK
            if node[0] == "break":
                return "BREAK"


            # CONTINUE
            if node[0] == "continue":
                return "CONTINUE"


            # PRINT
            if node[0] == "print":
                self.log(self.evaluate(node[1]))


            # VAR
            elif node[0] == "var":
                self.env[node[1]] = self.evaluate(node[2])


            # SET (IMPORTANT FIX)
            elif node[0] == "set":
                self.env[node[1]] = self.evaluate(node[2])


            # IF
            elif node[0] == "if":
                if self.evaluate(node[1]):
                    res = self.execute_block(node[2])

                    if res == "BREAK":
                        return "BREAK"

                    if res == "CONTINUE":
                        return "CONTINUE"


            # FOR
            elif node[0] == "for":

                var = node[1]
                start = self.evaluate(node[2])
                end = self.evaluate(node[3])

                for i in range(start, end + 1):

                    self.env[var] = i

                    res = self.execute_block(node[4])

                    if res == "BREAK":
                        return "BREAK"

                    if res == "CONTINUE":
                        continue


            # WHILE
            elif node[0] == "while":

                while self.evaluate(node[1]):

                    res = self.execute_block(node[2])

                    if res == "BREAK":
                        return "BREAK"

                    if res == "CONTINUE":
                        continue


        return None


    def execute(self, ast):
        return self.execute_block(ast)