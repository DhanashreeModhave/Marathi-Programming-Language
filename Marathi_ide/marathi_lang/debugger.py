import traceback


class Debugger:


    def __init__(self):

        self.env = {}
        self.trace = []
        self.step = 0



    def clean_memory(self):

        return {
            k:v
            for k,v in self.env.items()
            if k != "__builtins__"
        }




    def execute(self, runtime, ast):


        self.trace=[]

        try:

            for i,node in enumerate(ast):

                self.step=i+1


                self.trace.append(
                    f"Line {self.step} → {node}"
                )


                runtime.execute([node])


            self.env = runtime.env


            return runtime.output



        except Exception as e:


            error = traceback.format_exc()


            raise Exception(
                f"Error at step {self.step}\n\n{error}"
            )





    def reset(self):

        self.env={}
        self.trace=[]
        self.step=0