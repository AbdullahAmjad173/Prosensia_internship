def evaluate_expression(expression, variables):
    try:
        return eval(expression, {}, variables)
    except NameError as e:
        return f"Undefined variable: {e}"
    except Exception as e:
        return f"Error: {e}"

# passing values to the function.
variables = {'x': 10, 'y': 5}
print(evaluate_expression("x + y", variables))
print(evaluate_expression("x + z", variables))
