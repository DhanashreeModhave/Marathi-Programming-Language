class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0


    def peek(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None


    def eat(self):
        t = self.peek()
        if t:
            self.pos += 1
        return t


    def parse(self):
        ast = []

        while self.peek():
            node = self.statement()
            if node:
                ast.append(node)
            else:
                self.eat()

        return ast


    # ---------------- STATEMENT ----------------

    def statement(self):

        token = self.peek()

        if not token:
            return None

        kind = token[0]


        # BREAK
        if kind == "BREAK":
            self.eat()
            return ("break",)


        # CONTINUE
        if kind == "CONTINUE":
            self.eat()
            return ("continue",)


        # PRINT
        if kind == "PRINT":
            self.eat()
            self.eat()
            value = self.expression()
            return ("print", value)


        # VAR
        if kind == "VAR":
            self.eat()
            name = self.eat()[1]
            self.eat()
            value = self.expression()
            return ("var", name, value)


        # IF
        if kind == "IF":

            self.eat()
            condition = self.expression()

            if self.peek() and self.peek()[0] == "LBRACE":
                self.eat()

            body = []
            while self.peek() and self.peek()[0] != "RBRACE":
                body.append(self.statement())

            if self.peek():
                self.eat()

            return ("if", condition, body, None)


        # FOR
        if kind == "FOR":

            self.eat()
            var = self.eat()[1]

            self.eat()
            start = self.expression()

            self.eat()
            end = self.expression()

            self.eat()

            body = []
            while self.peek() and self.peek()[0] != "RBRACE":
                body.append(self.statement())

            if self.peek():
                self.eat()

            return ("for", var, start, end, body)


        # WHILE
        if kind == "WHILE":

            self.eat()
            condition = self.expression()

            self.eat()

            body = []
            while self.peek() and self.peek()[0] != "RBRACE":
                body.append(self.statement())

            if self.peek():
                self.eat()

            return ("while", condition, body)


        # ASSIGNMENT (IMPORTANT FIX)
        if kind == "ID":

            name = self.eat()[1]

            if self.peek() and self.peek()[0] == "ASSIGN":

                self.eat()

                value = self.expression()

                return ("set", name, value)

            return name


        return self.expression()


    # ---------------- EXPRESSION ----------------

    def expression(self):

        left = self.factor()

        while self.peek() and self.peek()[0] == "OP":
            op = self.eat()[1]
            right = self.factor()
            left = (op, left, right)

        return left


    # ---------------- FACTOR ----------------

    def factor(self):

        token = self.eat()

        if not token:
            return None

        kind, value = token

        if kind == "NUMBER":
            return int(value)

        if kind == "STRING":
            return value

        if kind == "ID":
            return value

        return value