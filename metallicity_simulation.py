import astropy.cosmology as cosmo
import astropy.units as u
import numpy as np
from astropy.cosmology import FlatLambdaCDM  # For custom PR4 cosmology

# Custom Planck PR4 cosmology (2024 parameters: H0=67.4, Om0=0.315, etc. – latest as of 2025)
pr4 = FlatLambdaCDM(H0=67.4, Om0=0.315, Tcmb0=2.7255, Neff=3.046, m_nu=0.06 * u.eV, Ob0=0.049)

# Function to get universe age at redshift z
def age_at_z(z):
    return pr4.age(z).to(u.Gyr).value

# Parameters
Z0 = 1e-5  # Initial metallicity
k = 0.55   # Growth rate calibrated to solar

# Simulate base evolution
zs = np.linspace(0, 10, 100)
ages = [age_at_z(z) for z in zs]
metallicities = Z0 * np.exp(k * np.array(ages))

print('At z=0 (age ~13.80 Gyr, PR4): Z ≈', metallicities[0])
print('At z=10 (age ~0.48 Gyr, PR4): Z ≈', metallicities[-1])

# Sensitivity test
k_strong = k * 1.01
k_weak = k * 0.99
met_strong = Z0 * np.exp(k_strong * np.array(ages))
met_weak = Z0 * np.exp(k_weak * np.array(ages))

print('+1% stronger: Z at z=0 ≈', met_strong[0])
print('-1% weaker: Z at z=0 ≈', met_weak[0])

# Advanced: Add galaxy metallicity gradient (e.g., inside-out formation)
r = np.linspace(0, 10, 50)  # Radius in kpc
gradient = -0.05 * r + 0.02  # Example linear gradient (based on observed slopes ~ -0.05 dex/kpc)
print('Mean metallicity gradient at z=0: ', gradient.mean())

# New: Example comparison to real data (dummy JWST-like metallicity at high z)
observed_Z_high_z = 0.001  # Example from early galaxies
model_Z_high_z = metallicities[-1]
print('Model vs Observed Z at z=10: ', model_Z_high_z, 'vs', observed_Z_high_z)