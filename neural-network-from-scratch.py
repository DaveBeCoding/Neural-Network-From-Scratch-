import numpy as np


class Operation:
    """
    An Operation is a node in a "Graph". TensorFlow will also use this concept of a Graph.

    This Operation class will be inherited by other classes that actually compute the specific
    operation, such as adding or matrix multiplication.
    """

    def __init__(self, input_nodes=[]):
        """
        Intialize an Operation
        """
        self.input_nodes = input_nodes  # The list of input nodes
        self.output_nodes = []  # List of nodes consuming this node's output

        # For every node in the input, we append this operation (self) to the list of
        # the consumers of the input nodes
        for node in input_nodes:
            node.output_nodes.append(self)

        # There will be a global default graph (TensorFlow works this way)
        # We will then append this particular operation
        # Append this operation to the list of operations in the currently active default graph
        _default_graph.operations.append(self)

    def compute(self):
        """
        This is a placeholder function. It will be overwritten by the actual specific operation
        that inherits from this class.

        """

        pass


class add(Operation):
    def __init__(self, x, y):

        super().__init__([x, y])

    def compute(self, x_var, y_var):

        self.inputs = [x_var, y_var]
        return x_var + y_var


class multiply(Operation):
    def __init__(self, a, b):

        super().__init__([a, b])

    def compute(self, a_var, b_var):

        self.inputs = [a_var, b_var]
        return a_var * b_var


class matmul(Operation):
    def __init__(self, a, b):

        super().__init__([a, b])

    def compute(self, a_mat, b_mat):

        self.inputs = [a_mat, b_mat]
        return a_mat.dot(b_mat)


class Placeholder:
    """
    A placeholder is a node that needs to be provided a value for computing the output in the Graph.
    """

    def __init__(self):

        self.output_nodes = []

        _default_graph.placeholders.append(self)


class Variable:
    """
    This variable is a changeable parameter of the Graph.
    """

    def __init__(self, initial_value=None):

        self.value = initial_value
        self.output_nodes = []

        _default_graph.variables.append(self)


class Graph:
    def __init__(self):

        self.operations = []
        self.placeholders = []
        self.variables = []

    def set_as_default(self):
        """
        Sets this Graph instance as the Global Default Graph
        """
        global _default_graph  # global to be shared throughout the file
        _default_graph = self


g = Graph()
g.set_as_default()
