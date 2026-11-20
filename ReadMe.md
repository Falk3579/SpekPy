[Home](https://bitbucket.org/spekpy/spekpy_release/src/master/ReadMe), 
[Further information](https://bitbucket.org/spekpy/spekpy_release/src/master/info/Further%20information), 
[Function glossary](https://bitbucket.org/spekpy/spekpy_release/src/master/info/Function%20glossary),
[Release history](https://bitbucket.org/spekpy/spekpy_release/src/master/info/Release%20history),

# Welcome to the SpekPy homepage

[What SpekPy is](#markdown-header-what-spekpy-is)

[What SpekPy is not](#markdown-header-what-spekpy-is-not)

[Try before you install](#markdown-header-try-before-you-install)

[How to install SpekPy](#markdown-header-how-to-install-spekpy)

[How to use SpekPy](#markdown-header-how-to-use-spekpy)

[The software license](#markdown-header-the-software-license)

[About us](#markdown-header-about-us)

[Contacts](#markdown-header-contacts)

[Our book](#markdown-header-our-book)

[How to reference SpekPy](#markdown-header-how-to-reference-spekpy)

## What SpekPy is

SpekPy is a powerful and free software toolkit for calculating and manipulating the spectra of x-ray tubes. The code is written in the Python programming language. It can be used in a Python interpreter or from a Python script. For more information on SpekPy, please see [Further information](info/Further%20information).

Initially, SpekPy could only model x-ray tubes with the classic "reflection" geometry. With release v2.5.0, however, it was extended to model transmission targets. Currently it is capable of modelling both possibilities for several target materials. For W targets, tube potentials ranging from 10 to 500 kV can be selected. For Cr, Cu, Mo, Rh, Ag, Au targets, the more restricted range of 10 to 50 kV is possible. 

## What SpekPy is not

SpekPy is a toolkit, not a command-line program or a piece of software with a fancy Graphical User Interface (i.e. a GUI). If you want to use it you will have to write a Python script or type commands yourself. Fortunately, SpekPy is easy to use and both it and Python are free. An alternative, for basic calculations, is to use SpekPy Web, our online web application. This free app can be found [here](https://spekpy.smile.ki.se/) and [here](https://spekpyweb.onrender.com/).

SpekPy also isn't a "medical device" (or "software as a medical device"). This means that it shouldn't be used in any way that influences diagnosis, prevention, monitoring, prediction, prognosis, or treatment of human beings. 

## Try before you install

*SpekPy Web*

The easiest way to get started with SpekPy is via the web app. You can find the SpekPy Web app [here](https://spekpyweb.onrender.com/).  

*Binder*

Alternatively, the following button launches a Jupyter notebook running SpekPy:

[![Binder](https://static.mybinder.org/badge_logo.svg)](https://mybinder.org/v2/git/https%3A%2F%2Fbitbucket.org%2Fspekpy%2Fspekpy_release%2Fsrc%2Fmaster/HEAD?filepath=SpekPy-Notebook.ipynb)

Binder can be slow to load, but gives you a chance to try scripting with SpekPy before installing.

Tips:

* Click on a code-block and press **Run** to run the code snippet

* If the plot doesn't show after running the code-block, try pressing **Run** again

## How to install SpekPy

*New for 2024*

SpekPy is now available in the PyPI package index. This means that it can be installed in a Python environment using *pip*, without dowloading the source from this repository:

```console
pip install spekpy
```

Thanks go to [Xandra Campo Blanco](https://github.com/lmri-met/uspekpy) for making this possible.

*Install from source*

You can download the source from here. Click on **Source** on the menu to the left to go to the source code. Then you can clone the git repository (click on the **Clone** button on that page for more info). Alternatively, you can download the software as a zip file by clicking on **Downloads**.

SpekPy is designed to be compatible with both Python2 (2.6 or higher) and Python3 (3.6 or higher). Note, however, that Python2 is officially depreciated by the Python Software Foundation as of 1st January 2020. 

We typically install and uninstall SpekPy using the standard Python *pip* utility. You can do this by navigating to the SpekPy directory in a command window and typing:

```console
pip install .
```

The package needs the standard NumPy and SciPy libraries. If these are not installed already, the SpekPy installation process will try to install them for you.

To be able to save spectrum states and create new filter materials, you need write permission for where you install. If you don't have admin rights on the account you want to use for SpekPy, you can try:

```console
pip install . --user
```

This should install SpekPy to you local user space. You can probably successfully install SpekPy via running the *setup.py* script or *easy_install*. The latter is depreciated, however, and the former is less convenient if you want to uninstall/reinstall.

*Advice for Anaconda Python*

If you use Anaconda Python, it is good to be aware that in some cases *pip* and *conda* installations of packages can cause conflicts. We recommend creating a clean conda environment:

```console
conda create -n spekpy-env python=3.7 numpy scipy matplotlib
```
before proceeding with:
```console
conda activate spekpy-env
pip install .
```
Installing *NumPy* and *SciPy* first, using the conda installer, should ensure that you have no conflicts.

## How to use SpekPy

Here's an example of some Python code, to model a tungsten target (default) reflection-type (default) tube:

```python
import spekpy as sp

r = sp.Spek(kvp=80,th=12) # Generate a spectrum (80 kV, 12 degree tube angle)
r.filter('Al', 4.0) # Filter by 4 mm of Al

hvl = r.get_hvl1() # Get the 1st half-value layer in mm Al

print(hvl) # Print out the HVL value

```

Here's an example of how to model a transmission tube with a 10um thick copper target:

```python
import spekpy as sp

t = sp.Spek(kvp=80,trans=True,thick=10,targ='Cu') # Target thickness entered in um
t.filter('Be', 250e-3) # Filter thickness entered in mm i.e. 250 um of Al; 

phi = t.get_flu() # Get the total integrated fluence

print(phi) # Print out the fluence

```

To see a complete list of SpekPy tools (methods and functions), please take a look at the [Function glossary](info/Function%20glossary).

## The software license

The software toolkit is available under the permissive MIT License. Yes, you could put it in your software application and make millions of dollars and not have to pay us a dime! Please do credit and reference us though.

## About us

SpekPy was developed by Gavin Poludniowski and Robert Bujila with considerable help from Artur Omar. The work was initiated (by Gavin) at the University of Surrey in the UK and continued in Sweden, at the Karolinska University Hospital (with Robert and Artur). Our academic associations are with Karolinska Institutet (both Gavin and Artur) and the Royal Technical University (Robert). Robert Bujila has now moved to GE Healthcare (Waukesha, WI, USA).

The models underlying SpekPy V2 were developed by Artur Omar, Gavin Poludniowski and Pedro Andreo.

The SpekPy Web app was developed by Robert Vorbau (Karolinska University Hospital) in collaboration with Gavin Poludniowski.

## Contacts

Drop me an email if you have a query, suggestion or have found a bug:

Email: gpoludniowski@gmail.com

Please do let us know about any bugs. You can either email or raise an issue using the **Issues** option in the left-hand panel.

## Our book

*Calculating X-ray Tube Spectra: Analytical and Monte Carlo Approaches*, by Gavin Poludniowski, Artur Omar, Pedro Andreo

![Book cover](https://images.tandf.co.uk/common/jackets/crclarge/978100305/9781003058168.jpg
)

Key Features of CaXTuS:

* Covers simple modelling approaches as well as full Monte Carlo simulation of x-ray tubes.
* Bremsstrahlung and characteristic contributions to the spectrum are discussed in detail.
* Learning is supported by free open-source software and an online repository of code.

An online repository of the code that accompanies this book can be found [here](https://bitbucket.org/caxtus/book).

## How to reference SpekPy

#### Primary references

G Poludniowski, A Omar, *The SpekPy toolkit for modelling X-ray tube spectra: Extension to transmission targets and additional target materials*. Appl Radiat Isot. 2026;229:112374.

G Poludniowski, A Omar, R Bujila and P Andreo, *Technical Note: SpekPy v2.0—a software toolkit for modeling x-ray tube spectra*. Med Phys. 2021; https://doi.org/10.1002/mp.14945

R Bujila, A Omar and G Poludniowski, *A validation of SpekPy: a software toolkit for modelling x-ray tube spectra*. Phys Med. 2020; 75:44-54.

Vorbau R, Poludniowski G. *Technical note: SpekPy Web-online x-ray spectrum calculations using an interface to the SpekPy toolkit*. J Appl Clin Med Phys. 2024;25(3):e14301.

#### Secondary references

A Omar, P Andreo and G Poludniowski, *A model for the energy and angular distribution of x rays emitted from an x-ray tube. Part I. Bremsstrahlung production*. Med Phys. 2020; 47(10):4763-4774

A Omar, P Andreo and G Poludniowski, *A model for the energy and angular distribution of x rays emitted from an x-ray tube. Part II. Validation of x-ray spectra from 20 to 300 kV*. Med Phys. 2020; 47(9):4005-4019

A Omar, P Andreo and G Poludniowski, *A model for the emission of K and L x rays from an x-ray tube*. NIM B 2018; 437:36-47.

G Poludniowski, *Calculation of x-ray spectra emerging from an x-ray tube. Part II. X-ray production and filtration in x-ray targets*. Med Phys. 2007; 34(6):2175-86.

G Poludniowski and PM Evans, *Calculation of x-ray spectra emerging from an x-ray tube. Part I. electron penetration characteristics in x-ray targets*. Med Phys. 2007; 34(6):2164-74.

G Poludniowski, et al., *SpekCalc: a program to calculate photon spectra from tungsten anode x-ray tubes*. Phys Med Biol. 2009; 54(19):N433-8.

A Omar, P Andreo and G Poludniowski, *Performance of different theories for the angular distribution of bremsstrahlung produced by keV electrons incident upon a target*. Radiat. Phys. and Chem. 2018; 148:73-85.