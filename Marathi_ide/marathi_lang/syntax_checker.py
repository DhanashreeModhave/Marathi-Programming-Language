def check_syntax(code):

    lines = code.split("\n")


    for i, line in enumerate(lines):

        text = line.strip()


        if text == "":
            continue


        # blocks don't need ;
        if text.endswith("{"):
            continue


        if text.endswith("}"):
            continue


        # function declaration
        if text.startswith("कार्य"):
            continue



        # all normal statements need ;

        if not text.endswith(";"):


            spaces = " " * len(text)


            raise Exception(
f"""
❌ Syntax Error

ओळ क्रमांक: {i+1}

{text}

{spaces}^

सेमीकोलन (;) टाकणे आवश्यक आहे.
"""
            )


    return True