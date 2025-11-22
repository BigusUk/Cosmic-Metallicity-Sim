# Cosmic Metallicity Evolution Simulation

"AI and Humanity: Collaborating to Build a Better Future for the Universe."
"These tools aim to help humankind by advancing research in clean energy, life's origins, and cosmic evolution"

This is a simplified toy model; adjust k for specific calibrations (e.g., k=0.55 for solar Z~0.02)

## Description
This script simulates the evolution of metallicity (fraction of heavy elements) in the universe over cosmic time using Astropy for cosmology parameters and a simple exponential growth model. It includes sensitivity tests to show how small changes in physical constants (like a proxy for nuclear force) affect outcomes.

## Requirements
- Python 3.8+
- astropy
- numpy

## How to Run
1. Install dependencies if needed: `pip install astropy numpy`
2. Save the code as `metallicity_simulation.py`
3. Run: `python metallicity_simulation.py`

## Assumptions
- Based on Planck 2018 cosmology for universe ages at different redshifts.
- Exponential growth formula: Z(t) = Z0 * exp(k * t), with Z0 = 1e-5 (initial low metallicity) and k = 0.55 Gyr^-1 (calibrated to reach solar-like ~0.02 today).
- Redshift range: z=0 (today) to z=10 (~0.48 Gyr after Big Bang).
- Sensitivity test varies growth rate by ±1% to mimic constant changes.
## Advanced Features
- Galaxy metallicity gradient simulation (inside-out evolution).
- Comparison to observed data (extend with real JWST datasets).

## Example Output
At z=0 (age ~13.8 Gyr): Z ≈ 0.0196
At z=10 (age ~0.48 Gyr): Z ≈ 1.35e-05
+1% stronger constant: Z at z=0 ≈ 0.0212 (~8% increase)
-1% weaker constant: Z at z=0 ≈ 0.0182 (~7% drop)

## License
MIT License

Copyright (c) 2025 xAI

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"AI and Humanity: Collaborating to Build a Better Future for the Universe."