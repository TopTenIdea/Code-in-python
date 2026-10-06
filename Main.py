import math
code = ""
codepcs = code.splitlines()

#storage
vars = {}
#
for codepart in codepcs:
    if codepart.startswith("STV"):#set variable
        localpart = codepart.split()
        currvar = localpart[1]
        currvartoset = localpart[2]
        if currvar.isdigit():#check that the variable we are setting isnt a decimal value
            raise Exception("Cannot set decimal to a value")
        if not currvar.isascii():#check that the variable we are setting is legal
            raise Exception("Cannot use a non-ASCII value as variable")
        if not currvartoset.isascii():#check that the value we are setting is legal
            raise Exception("Cannot set a variable to a non-ASCII value")
        if currvartoset in vars:
            currvartoset = vars[currvartoset]
        if isinstance(currvartoset, str):
            try:
                currvartoset = float(currvartoset)
            except ValueError:
                pass
        vars[currvar] = currvartoset
    if codepart.startswith("INC"):#increment
        localpart = codepart.split()
        currvartoinc = localpart[1]
        incby = localpart[2]
        if currvartoinc not in vars:#make sure that we are incrementing something that exists
            raise Exception("Variable to increment does not exist")
        if isinstance(vars[currvartoinc], (int, float)):
            if incby in vars:
                if not isinstance(vars[incby], (int, float)):
                    raise Exception("Cannot increment a decimal value by a non-decimal value")
                vars[currvartoinc] = float(vars[currvartoinc]) + float(vars[incby])
            else:
                try:
                    vars[currvartoinc] = float(vars[currvartoinc]) + float(incby)
                except ValueError:
                    raise Exception("Cannot increment a decimal value by a non-decimal value")
        else:
            if incby in vars:
                incby = vars[incby]
            if not isinstance(incby, str):
                raise Exception("Cannot increment a decimal value by a non-decimal value")
            vars[currvartoinc] += incby
    if codepart.startswith("SIN"):#sin function on input in radians
        localpart = codepart.split()
        currvartosin = localpart[1]
        if not isinstance(vars[currvartosin], (int, float)):#check that its a decimal value
            raise Exception("Cannot use non-decimal input to sin function")
        vars[currvartosin] = math.sin(float(vars[currvartosin]))
    if codepart.startswith("COS"):#cos function on input in radians
        localpart = codepart.split()
        currvartosin = localpart[1]
        if not isinstance(vars[currvartosin], (int, float)):#check that its a decimal value
            raise Exception("Cannot use non-decimal input to cos function")
        vars[currvartosin] = math.cos(float(vars[currvartosin]))