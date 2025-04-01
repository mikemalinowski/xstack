
# xstack

xstack is an execution framework which allows a developer to define components which 
can then be added to the stack - declaring options, requirements and outputs. 

## Installing

You can install xstack using `pip install xstack`

## Getting Started

The stack can be executed to run sequentially from top to bottom, from a specific
point, to a specific point or individiaully. 

Below is an example of what it looks like to add components to the stack, manipulate
the build order and execute a stack

```python
import xstack

COMPONENT_PATH = "location/to/where/you/store/your/components"

# -- Create a new stack. When we create a stack we need to tell it where
# -- to look for components
stack = xstack.Stack(
    component_paths=[COMPONENT_PATH],
)

# -- Add a component of type "RunTestComponent" into the stack. Note that you
# -- can see this component within the /test directory of xstack
component_a = stack.add_component(
    label="test a",
    component_type="RunTestComponent",
)

# -- Add the same component type again. 
component_b = stack.add_component(
    label="test b",
    component_type="RunTestComponent",
)

# -- Our stack now has two components in it, by default these will be in 
# -- a flat list and ordered based on the order they were added. Here we will
# -- make component_a a child of component_b - meaning that component_a will
# -- always execute after component_b
stack.set_build_position(
    component_a,
    parent=component_b,
)

# -- Execute the whole stack
stack.build()

# -- Execute just a single component
stack.build(build_only=component_a)
```

Defining a component is relatively simple...

```python
import xstack

class MyXStackComponent(xstack.Component):
    
    # -- Every component needs an identifier which can be used to differentiate
    # -- it from other components
    identifier = "MyExample"

    def __init__(self, *args, **kwargs):
        super(MyXStackComponent, self).__init__(*args, **kwargs)
        
        # -- Declare a requirement. A Requirement is an attribute of a component
        # -- that typically expects to be filled before execution. By default
        # -- all requirements will be validated for a value before executing. 
        self.declare_requirement(
            name="example_requirement",
            value="",
            group="Some Requirements",
        )
        
        # -- Options are considered to be attributes which are not essential to
        # -- be set but might tailor or alter what the result is
        self.declare_option(
            name="test_option",
            value="foo",
            pre_expose=True,
        )
        
        # -- An output is an attribute which this component promises to fullful
        # -- during the execution. This is useful because instead of specifying a 
        # -- value to a requirement, you can infact specify an output attribute 
        # -- address, and the value will be resolved at execution time. 
        self.declare_output(
            name="result"
        )
    
    # -- This function is where we write any code that should be run during the 
    # -- stack execution
    def run(self):
        return self.option("test_option").get() == "bar"

```