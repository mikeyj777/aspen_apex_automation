from emnengr.aspen.com import App

flattened_tree = []

def recurse_that_node(curr_node, prefix = ''):
    global flattened_tree
    for child in curr_node.children:
        comp_status_value = ''
        child_name = ''
        try:
            if hasattr(child, 'comp_status'):
                comp_status = child.comp_status
                if hasattr(comp_status, 'value'):
                    comp_status_value = comp_status.value
            if hasattr(child, 'name'):
                child_name = child.name
            row = f'{prefix}.{child_name} - comp status {comp_status_value}'
            flattened_tree.append(row)
            print(row)
            if hasattr(child, 'children'):
                recurse_that_node(child, prefix=f'{prefix}.{child_name}')
        except:
            pass
        if prefix == 'Data':
            apple = 1


def add_component(sim, component_id):
    """
    Adds a component to the Aspen Plus simulation if it's not already present.
    
    Parameters:
       happ: The IHapp interface object.
       component_id: The ID of the component to add (e.g., "METHANOL").
    """
    comp_node = sim.getNode(r"\Data\Components\Specifications\Input\OUTNAME")
    elements = comp_node.Elements

    # Check if component already exists
    for i in range(elements.Count):
        if elements.Item(i).Value.upper() == component_id.upper():
            print(f"Component '{component_id}' already exists.")
            return

    # Add the new component at the next available index
    next_index = elements.Count + 1 # Aspen uses 1-based indexing
    elements.Item(next_index).Value = component_id
    print(f"Component '{component_id}' added at position {next_index}.")


with App('/temp/aspen_test/hoac_h2o/hoac_h2o.bkp', visible=True) as sim:
    comps = sim.getComponents()
    add_component(sim, "METHANOL")
    apple = 1
