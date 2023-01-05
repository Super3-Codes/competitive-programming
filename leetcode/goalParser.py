def interpret(self, command: str) -> str:
        st = command.replace("()","o")
        st = st.replace("(al)","al")
        return st
