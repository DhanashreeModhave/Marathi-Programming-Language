from graphviz import Digraph


def draw_ast(ast):

    dot = Digraph()

    counter = [0]


    def add_node(label):

        node_id = str(counter[0])
        counter[0] += 1

        dot.node(
            node_id,
            str(label)
        )

        return node_id



    def build(node, parent=None):

        if node is None:
            return


        # list
        if isinstance(node, list):

            for item in node:
                build(item, parent)

            return



        # normal values
        if not isinstance(node, tuple):

            child = add_node(node)

            if parent:
                dot.edge(parent, child)

            return



        kind = node[0]



        # PROGRAM

        if kind == "program":

            current = add_node("PROGRAM")

            for child in node[1]:
                build(child, current)

            return



        # FUNCTION

        if kind == "func":

            current = add_node(
                "FUNCTION\n" + str(node[1])
            )

            if parent:
                dot.edge(parent, current)


            params = add_node("PARAMETERS")

            dot.edge(
                current,
                params
            )


            for p in node[2]:

                build(
                    p,
                    params
                )


            body = add_node("BODY")

            dot.edge(
                current,
                body
            )


            build(
                node[3],
                body
            )

            return




        # VARIABLE

        if kind == "var":

            current = add_node(
                "VARIABLE\n" + str(node[1])
            )


            if parent:
                dot.edge(parent, current)


            build(
                node[2],
                current
            )

            return




        # PRINT

        if kind == "print":

            current = add_node("PRINT")


            if parent:
                dot.edge(parent, current)


            build(
                node[1],
                current
            )

            return




        # RETURN

        if kind == "return":

            current = add_node("RETURN")


            if parent:
                dot.edge(parent, current)


            build(
                node[1],
                current
            )

            return




        # CALL

        if kind == "call":

            current = add_node(
                "CALL\n" + str(node[1])
            )


            if parent:
                dot.edge(parent, current)


            for arg in node[2]:

                build(
                    arg,
                    current
                )

            return




        # IF

        if kind == "if":

            current = add_node("IF")


            if parent:
                dot.edge(parent, current)


            condition = add_node("CONDITION")

            dot.edge(
                current,
                condition
            )


            build(
                node[1],
                condition
            )


            body = add_node("BODY")

            dot.edge(
                current,
                body
            )


            build(
                node[2],
                body
            )

            return




        # FOR

        if kind == "for":

            current = add_node(
                "FOR\n" + str(node[1])
            )


            if parent:
                dot.edge(parent, current)


            build(node[2], current)
            build(node[3], current)
            build(node[4], current)

            return




        # WHILE

        if kind == "while":

            current = add_node("WHILE")


            if parent:
                dot.edge(parent, current)


            build(
                node[1],
                current
            )


            build(
                node[2],
                current
            )

            return




        # BREAK

        if kind == "break":

            current = add_node("BREAK")

            if parent:
                dot.edge(parent, current)

            return



        # CONTINUE

        if kind == "continue":

            current = add_node("CONTINUE")

            if parent:
                dot.edge(parent, current)

            return




        # EXPRESSION / OPERATOR

        if len(node) == 3:


            current = add_node(
                "OP\n" + str(node[0])
            )


            if parent:
                dot.edge(parent, current)


            build(
                node[1],
                current
            )


            build(
                node[2],
                current
            )

            return




    root = ("program", ast)

    build(root)


    return dot