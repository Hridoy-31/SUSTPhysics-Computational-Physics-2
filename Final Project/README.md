# Description

A Lorenz system simulator with dynamics & chaos analyzer (written in Python 3) which uses the [fourth order Runge-Kutta
(RK4) method](https://lpsa.swarthmore.edu/NumInt/NumIntFourth.html) to solve the set of [differential equations](https://tutorial.math.lamar.edu/classes/de/de.aspx) 
from the [atmospheric convection](https://www.thoughtco.com/what-is-convection-4041318) in dimensionless form using the 
[Boussinesq approximation](https://www.comsol.com/multiphysics/boussinesq-approximation#:~:text=What%20Is%20the%20Boussinesq%20Approximation,of%20the%20Navier%2DStokes%20equations.). The Lorenz system is an accurate and 
typical model of chaos motion.

# Required modules

The following modules are used:

- [Matplotlib](https://matplotlib.org/stable/index.html)
- [\_\_future\_\_](https://docs.python.org/3/library/__future__.html) {Default module. NO NEED TO INSTALL}
- [Scipy](https://scipy.org/)
- [NumPy](https://numpy.org/)

For installing **Matplotlib**, the commands are the following:

    python -m pip install -U pip
    python -m pip install -U matplotlib

For installing **Scipy**, the command is the following:

    python -m pip install scipy

For installing **NumPy**, the command is the following:

    pip install numpy


# Usage instructions

Run `rk4-solver.py` to solve the system of linear ordinary differential equations of weather evolution. The obtained data is
used to get the simulation by running the simulator `lorenz.py` file.  


# Contributors & contact information

- S.M. Raihanul Bashir / raihanulbashirhridoy@gmail.com
- Showrav Acharjee / showravacharjee6@gmail.com
- Tanver Hossain Refat / tanveerrefat2223@gmail.com
- Md Kawser Ahmed / kawserahmedseyam13@gmail.com
