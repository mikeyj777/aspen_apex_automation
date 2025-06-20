from emnengr.aspen.com import App
import numpy as np

mole_fractions = {
    "ACETIC": 0.3,
    "PROPIONIC": 0.3,
    "WATER": 0.4
}

def get_wils_hoc_vp_curve_ternary():
    
    Tmin, Tmax, n_points = 300, 400, 10
    T_vals = np.linspace(Tmin, Tmax, n_points)
    vp_curve = []

    with App(visible=False) as sim:
        # Add components
        apple = 1
        pressure_node = sim.getNode(r"\\Data\\Streams\\FEED\\Input\\Pressure")
        unit = pressure_node.unitOfMeasure # This gives the unit column index

        comp_node = sim.getNode(r"\\Data\\Components\\Specifications\\Input")
        comp_node[r"\\CASN\\0"].value = "64-19-7"   # Acetic Acid
        comp_node[r"\\OUTNAME\\0"].value = "ACETIC"
        comp_node[r"\\CASN\\1"].value = "79-09-4"   # Propionic Acid
        comp_node[r"\\OUTNAME\\1"].value = "PROPIONIC"
        comp_node[r"\\CASN\\2"].value = "7732-18-5" # Water
        comp_node[r"\\OUTNAME\\2"].value = "WATER"

        # Set WILS-HOC property method
        sim.getNode(r"\\Data\\Properties\\Specifications\\Input\\GOPSETNAME").value = "MYPROPSET"
        sim.getNode(r"\\Data\\Properties\\Property Methods\\MYPROPSET\\Input\\CPROP\\1").value = "GAMMA"
        sim.getNode(r"\\Data\\Properties\\Property Methods\\MYPROPSET\\Input\\MODELNAME\\1").value = "WILS-HOC"

        # Set up flash block and feed
        sim.getNode(r"\\Data\\Blocks\\FLASH1\\Input\\Block Type").value = "FLASH2"
        sim.getNode(r"\\Data\\Blocks\\FLASH1\\Input\\Connections\\Inlets\\0").value = "FEED"
        sim.getNode(r"\\Data\\Streams\\FEED\\Input\\Mole Flow").value = 100
        sim.getNode(r"\\Data\\Streams\\FEED\\Input\\Pressure").value = 1  # Initial guess

        for comp, frac in mole_fractions.items():
            sim.getNode(fr"\\Data\\Streams\\FEED\\Input\\Composition\\Mole Fractions\\{comp}").value = frac

        for T in T_vals:
            sim.getNode(r"\\Data\\Streams\\FEED\\Input\\Temperature").value = T
            sim.reinitialize()
            sim.run()
            P = sim.getNode(r"\\Data\\Results\\Blocks\\FLASH1\\Output\\Pressure").value
            vp_curve.append((T, P))

    return vp_curve

vps = get_wils_hoc_vp_curve_ternary()

apple = 1
