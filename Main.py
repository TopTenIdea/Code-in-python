
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
        if currvar.isdecimal():#check that the variable we are setting isnt a decimal value
            raise Exception("Can not set decimal to a value")
        if not currvar.isascii():#check that the variable we are setting is legal
            raise Exception("Can not use a non ASCII value as variable")
        if not currvartoset.isascii():#check that the value we are setting is legal
            raise Exception("Can not set a variable to a non ASCII value")
        if currvartoset in vars:
            currvartoset = vars[currvartoset]
        if currvartoset.isdecimal():#if its a decimal convert to float
            currvartoset = float(currvartoset)
        vars[currvar] = currvartoset
    if codepart.startswith("INC"):#increment
        localpart = codepart.split()
        currvartoinc = localpart[1]
        incby = localpart[2]
        if not currvartoinc in vars:#make sure that we are incrementing something that exists
            raise Exception("Variable to increment does not exist")
        if vars[currvartoinc].isdecimal() and not incby.isdecimal():#we can incrment a string by a string and with a "decimal" using concatenation and we can incrememnt a decimal value with another decimal but we cannot incrment a decimal by a string
            raise Exception("Can not increment a decimal value by a non-decimal value")
        if vars[currvartoinc].isdecimal():#change to a float if we are incrmemnting a decimal value
            incby = float(incby)
        vars[currvartoinc]+=incby