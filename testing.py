import numpy as np
import matplotlib.pyplot as plt

# Constants
pKa = 8
intrinsic_solubility_non_ionized = 1  # mg/mL

# Davies equation constants (for water at 25°C)
A = 0.51
B = 0.33
C = 0.3
D = 0.2
a_i = 3  # effective diameter in nm

# Equilibrium constant for ion pair formation
K_ip = 10**3  # example value

# Saturation limit for solubility based on counterion concentration (example)
counterion_concentration = 0.01  # M

def ionic_strength(h_concentration, cl_concentration, bh_concentration):
    return 0.5 * (h_concentration**2 + cl_concentration**2 + bh_concentration**2)

def activity_coefficient(ionic_strength):
    if ionic_strength == 0:
        return 1.0  # Activity coefficient is 1 for very dilute solutions
    return 10 ** (-A * (ionic_strength**0.5) / (1 + B * a_i * (ionic_strength**0.5)) + (C * ionic_strength) / (1 + D * ionic_strength))

def solubility(pH):
    h_concentration = 10**(-pH)
    bh_concentration = 10**(pKa - pH) * intrinsic_solubility_non_ionized
    cl_concentration = h_concentration
    
    I = ionic_strength(h_concentration, cl_concentration, bh_concentration)
    gamma_bh_plus = activity_coefficient(I)

    # Calculate ion pair concentration
    bh_cl_concentration = (bh_concentration * cl_concentration) / K_ip
    bh_cl_concentration = min(bh_cl_concentration, counterion_concentration)
    
    # Effective concentration of ionized form after accounting for ion pairs
    effective_bh_concentration = bh_concentration - bh_cl_concentration
    
    # Ensure concentration is non-negative and adjust by activity coefficient
    effective_bh_concentration = max(effective_bh_concentration * gamma_bh_plus, 0)
    
    # Cap the total solubility based on the saturation limit
    total_solubility = intrinsic_solubility_non_ionized + effective_bh_concentration
    total_solubility = min(total_solubility, counterion_concentration)  # Cap by counterion concentration
    
    return total_solubility

# Generate pH range
pH_range = np.linspace(1, 10, 100)
solubility_values = [solubility(pH) for pH in pH_range]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(pH_range, solubility_values, label='Total Solubility')
plt.xlabel('pH')
plt.ylabel('Solubility (mg/mL)')
plt.title('Solubility vs pH with Counterion Effects')

# Set axis limits to zoom in on a specific region
plt.xlim(3, 7)  # Zoom in on pH range from 3 to 7
plt.ylim(1e-2, 1e0)  # Zoom in on solubility range from 0.01 to 1 mg/mL
