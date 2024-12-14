from ase import Atoms
from ase.visualize import view


d = 1.10
atom = Atoms('2N', positions=[(0., 0., 0.), (0., 0., d)])
atom.center(vacuum=5.0, axis=2)
#atom.write('Slab.xyz')

view(atom)