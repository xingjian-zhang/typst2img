# Typst Formula Renderer
A fast script to render your Typst formulas to svg.

## Usage

Command line:

```bash
python render_typ.py '$y = A x + b$' -o output.svg
```

In Jupyter Notebook (recommended):

```python
from render_typ import FormulaRenderer

formulas = [
    r'$ A = pi r^2 $',
    r'$ "area" = pi dot "radius"^2 $',
    r'$ cal(A) := { x in RR | x "is natural" } $',
    r'$ x < y => x gt.eq.not y $',
    r'$ mat(1, 2; 3, 4) $',
    r'''$ sum_(k=0)^n k
    &= 1 + ... + n \
    &= (n(n+1)) / 2 $''',
]

# Render in-line in a notebook.
basic_renderer = FormulaRenderer()
for f in formulas:
    basic_renderer.render(f)

# Save to file.
named_formulas = {
    "mass_energy_equivalence": r'$ E = m c^2 $',
    "euler_identity": r'$ e^(i pi) + 1 = 0 $',
    "general_relativity": r'$ G_(mu nu) + Lambda g_(mu nu) = kappa T_(mu nu) $',
}

for k, v in named_formulas.items():
    basic_renderer.render(v, name=k)
```

See [`example.ipynb`](example.ipynb) for more examples.

## Installation

```bash
pip install -r requirements.txt
```

## Convert to PNG

You can convert the SVG files to PNG using [ImageMagick `convert`](https://imagemagick.org/script/download.php). This feature is only tested on MacOS.

```bash
$ make all
convert -density 1000 output/euler_identity.svg output/euler_identity.png
convert -density 1000 output/general_relativity.svg output/general_relativity.png
convert -density 1000 output/mass_energy_equivalence.svg output/mass_energy_equivalence.png
```

## Examples

### Euler Identity

![Euler Identity](output/euler_identity.svg)

### General Relativity

![General Relativity](output/general_relativity.svg)

### Mass Energy Equivalence

![Mass Energy Equivalence](output/mass_energy_equivalence.svg)