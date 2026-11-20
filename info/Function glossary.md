[ReadMe](../ReadMe),
[Further information](Further%20information),
[Function glossary](Function%20glossary),
[Release history](Release%20history),

# Function glossary

## Miscellaneous

[filter()](#markdown-header-filter)

[multi_filter()](#markdown-header-multi_filter)

[set()](#markdown-header-set)

[clone()](#markdown-header-clone)

[summarize()](#markdown-header-summarize)

[comment()](#markdown-header-comment)

## Extracting values and metrics

In addition to any arguments explicitly specified in the function descriptions, the following keyword arguments (kwargs) can be specified: *x, y, z, mas, brem, char, obli*. See [here](Further%20information) for further information on these keyword arguments.

[get_k()](#markdown-header-get_k)

[get_spk()](#markdown-header-get_spk)

[get_spectrum()](#markdown-header-get_spectrum)

[get_kerma()](#markdown-header-get_kerma)

[get_hvl1()](#markdown-header-get_hvl1)

[get_hvl()](#markdown-header-get_hvl)

[get_hvl2()](#markdown-header-get_hvl2)

[get_hc()](#markdown-header-get_hc)

[get_emean()](#markdown-header-get_emean)

[get_eeff()](#markdown-header-get_eeff)

[get_matl()](#markdown-header-get_matl)

[get_flu()](#markdown-header-get_flu)

[get_eflu()](#markdown-header-get_eflu)

[get\_norm\_flu()](#markdown-header-get_norm_flu)

[get\_std\_results()](#markdown-header-get_std_results)

## Materials

[make_matl()](#markdown-header-make_matl)

[remove_matl()](#markdown-header-remove_matl)

[show_matls()](#markdown-header-show_matls)

## States

[load_state()](#markdown-header-load_state)

[save_state()](#markdown-header-save_state)

[remove_state()](#markdown-header-remove_state)

[show_states()](#markdown-header-show_states)

## Input/output

[export_spectrum()](#markdown-header-export_spectrum)

[load\_from\_file()](#markdown-header-load_from_file)

## clone
     
    clone()

    Parameters
    **********
    None

    Returns
    *******
    : Spek
        A new instance of the Spek class with an identical state to the parent

    Purpose
    *******
    Creates a clone (deep copy) of the parent Spek class instance (i.e. of a spectrum model). This is
    particularly useful if you want to apply filtration to the clone without affecting the original spectrum.

Usage:

```python
s = sp.Spek()
t=sp.Spek.clone(s)
```

## comment
     
    comment(comment=None)
    
    Parameters
    **********
    comment : str
        The comment string
    
    Returns
    *******
    None (but changes the Spek instance)

    Purpose
    *******
    Associates the comment string with the state and it is included when the state is saved, or when the
    spectrum is exported. Calling comment() erases any previous comment.

Usage:

```python
s = sp.Spek()
s.comment('My message') # Adds a comment
s.comment() # Removes the comment
```

## export_spectrum
     
    export_spectrum(file_name=None, comment=None, delim=';')

    Parameters
    **********
    file_name : str
        Name of the text file to be created
    comment : str
        Comment (if any) to append to the file      
    delim : str
        Chosen delimiter to delimit data columns

    Returns
    *******
    None (but creates a new file)

    Purpose
    *******
    Save a spectrum and associated information as a text file. Three columns are output: mid-bin energies
    in keV, total x-ray fluences (i.e. bremsstrahlung + characteristic) per keV, and characteristic x-ray 
    fluences per keV.

Usage:

```python
s=sp.Spek()
spek_name = 'Demo_export_spectrum.spk' # Specify file name
s.export_spectrum(spek_name, comment='A demo spectrum export') # Export spectrum to file
```

## filter
     
    filter(matl, t)

    Parameters
    **********
    matl : str
        Name of material
    t : float
        Thickness of material in mm (it can be negative for stripping off filters)

    Returns
    *******
    None (but changes the Spek instance)

    Purpose
    *******
    To add filtration to the spectrum model.

Usage:

```python
s = sp.Spek()
s.filter('Al',2.5)
```

## get_k
     
    get_k()

    Parameters
    **********
    None

    Returns
    *******
    : numpy.ndarray (1d, dtype=numpy.float)
        Array of energy bins (the mid-bin values in keV)

    Purpose
    *******
    To extract the energy bins for the spectrum.

Usage:

```python
s = sp.Spek()
kbins = s.get_k()
```

## get_spk
     
    get_spk(**kwargs)

    Parameters
    **********
    kwargs :
        Optional (can include any valid keyword argument for the set() method)

    Returns
    *******
    : numpy.ndarray (1d, dtype=numpy.float)
        Array of fluences (# per cm2 per keV)

    Purpose
    *******
    To extract the x-ray fluences corresponding to the energy bins.

Usage:

```python
s = sp.Spek()
spk = s.get_spk()
```

## get_spectrum
     
    get_spectrum(edges=False,flu=True,diff=True,sig=False,**kwargs)

    Parameters
    **********
    edges : Bool
        If edges=False (default), the energy bins are defined at the mid-bin values, else at the bin edges 
        (histogram format)
    flu : Bool
    	If flu=True (default), fluence is returned, else energy-fluence
    diff : Bool
        If diff=True (default), the fluence or energy-fluence returned is differential in energy, 
        else the non-differential quantity is returned (e.g. # per cm2 per bin versus # per cm2 per keV)
    sig : float
        If sig=None (default), the calculated spectrum is returned. If a value is specified, a Gaussian 
        filter of the specified sigma value (keV ) is applied to the spectrum, to degrade the energy 
        resolution of output. Note: Full-Width-Half-Maximum = 2.355 x sig.
    kwargs : 
        Optional (can include any valid keyword argument for the set() method)


    Returns
    *******
    : numpy.ndarray (1d, dtype=numpy.float)
        Array of energy bins (mid-bin or edge values in keV)
    : numpy.ndarray (1d, dtype=numpy.float)
        Array of fluences corresponding to energy bins ('# per cm2 per keV' (default), '# per cm2' or
        'keV per cm2')

    Purpose
    *******
    To return the energy bin and x-rays fluences together. If edges is specified as True, 
    the arrays are returned in "stair-case" or "Monte Carlo" style format.

Usage:

```python
s = sp.Spek()
kbins, spk = s.get_spectrum(edges=True)
```

## get_kerma
     
    get_kerma(norm=True,to='air',**kwargs)

    Parameters
    **********
    norm : Bool
        If norm=True, the kerma per mAs is returned
    to : str
        Must take a value of 'air' or 'water'. Specifies whether kerma is air or water kerma (default: air)
    kwargs : 
        Optional (can include any valid keyword argument for the set() method)

    Returns
    *******
    : numpy.float
        Air kerma in uGu or uGy/mAs

    Purpose
    *******
    To obtain the normalized or un-normalized air kerma for the reference conditions 
    (or those specified by kwargs) 

Usage:

```
#!Python
s = sp.Spek()
k = s.get_kerma()
```

## get_hvl1
     
    get_hv1(matl='Al',to='air',**kwargs)

    Parameters
    **********
    matl : str
        Material used to specify the half-value layer (default: Al)
    to : str
        Must take a value of 'air' or 'water'. Specifies whether half-value layer defined in terms of air or     
        water kerma (default: air)
    kwargs : 
        Optional (can include any valid keyword argument for the set() method)


    Returns
    *******
    : numpy.float
        The first half-value-layer in mm

    Purpose
    *******
    To obtain the first half-value-layer for a specified material under for the reference conditions 
    (or those specified by kwargs)

Usage:

```python
s = sp.Spek()
hvl1 = s.get_hvl()
```

## get_hvl
     
    get_hvl(matl='Al',to='air',**kwargs)

    Parameters
    **********
    matl : str
        Material used to specify the half-value layer (default: Al)
    to : str
        Must take a value of 'air' or 'water'. Specifies whether half-value layer defined in terms of air or 
        water kerma (default: air)
    kwargs : 
        Optional (can include any valid keyword argument for the set() method)


    Returns
    *******
    : numpy.float
        The first half-value-layer in mm

    Purpose
    *******
    To obtain the first half-value-layer for a specified material under for the reference conditions 
    (or those specified by kwargs). This method is identical to *get_hvl1()*.

Usage:

```python
s = sp.Spek()
hvl = s.get_hvl()
```

## get_hvl2
     
    get_hv2(matl='Al',to='air',**kwargs)

    Parameters
    **********
    matl : str
        Material used to specify the half-value-layer (default: Al)
    to : str
        Must take a value of 'air' or 'water'. Specifies whether half-value layer defined in terms of air or     
        water kerma (default: air)
    kwargs : 
        Optional (can include any valid keyword argument for the set() method)


    Returns
    *******
    : numpy.float
        The second half-value-layer in mm

    Purpose
    *******
    To obtain the second half-value-layer for a specified material under for the reference conditions 
    (or those specified by kwargs)

Usage:

```python
s = sp.Spek()
hvl2 = s.get_hv2()
```

## get_hc
     
    get_hc(matl='Al',to='air',**kwargs)

    Parameters
    **********
    matl : str
        Material used to specify the homogeneity coefficient (default: Al)
    to : str
        Must take a value of 'air' or 'water'. Specifies whether half-value layers defined in terms of air or     
        water kerma (default: air)
    kwargs : 
        Optional (can include any valid keyword argument for the set() method)


    Returns
    *******
    : numpy.float
        Homogeneity coefficient (i.e. 1st HVL/2nd HVL)

    Purpose
    *******
    To obtain the homogeneity coefficient for a specified material under for the reference conditions 
    (or those specified by kwargs)

Usage:

```python
s = sp.Spek()
hc = s.get_hc()
```

## get_matl
     
    get_matl(matl='Al', hvl_matl='Al', hvl=False, frac=False, to='air' **kwargs)

    Parameters
    **********
    matl : str
        Material used to filter spectrum (default: Al)
    hvl_matl : str
        If a valid string is specified, that material will be used (default: Al)
    hvl : float
        If a value is specified, that will be taken as the target hvl
    frac : float
        If a value is specified, that will be taken as the target fraction of air kerma
    to : str
        Must take a value of 'air' or 'water'. Specifies whether eveything defined in terms of air or water     
        kerma
    kwargs :
        Optional (can include any valid keyword argument for the set() method)

    Returns
    *******
    : numpy.float
        Thickness of filter material that provides the target attenuation characteristics

    Purpose
    *******
    To find the amount of filtration needed to obtain a specified half-value-layer or fraction of air 
    kerma for the reference conditions (or those specified by kwargs).
    Note that one of "hvl" or "frac" must be assigned, but not both. "hvl_matl" should only be specified 
    in conjunction with "hvl". 

Usage:

```python
s = s.Spek()
t = s.get_matl(matl='Sn',hvl_matl='Cu',hvl=1.0) # Thickness of tin that gives a 1st HVL of 1 mmCu
```

or

```python
s = s.Spek()
t = s.get_matl(matl='Sn',frac=0.1) # Thickness of tin that reduces air kerma to 10% 
```

## get_emean
     
    get_emean(**kwargs)

    Parameters
    **********
    kwargs :
        Optional (can include any valid keyword argument for the set() method)

    Returns
    *******
    : numpy.float
        Mean energy of photons in the spectrum in keV

    Purpose
    *******
    To obtain the mean energy of x-ray photon in the spectrum.

Usage:

```
#!Python
s = sp.Spek()
km = s.get_emean()
```

## get_eeff
     
    get_eeff(matl='Al',**kwargs)

    Parameters
    **********
    matl : str
        Material used to define effective energy (default: Al)
    kwargs : 
        Optional (can include any valid keyword argument for the set() method)


    Returns
    *******
    : numpy.float
        Effective energy in keV

    Purpose
    *******
    To obtain the effective energy for a specified material under for the reference conditions (or those 
    specified by kwargs).
    The effective energy is defined as the energy at which a monoenergetic spectrum would have the same 
    half-value layer as the polyenergetic spectrum (for the specified material).

Usage:

```python
s = sp.Spek()
ke = s.get_eeff()
```

## get_flu
     
    get_flu(**kwargs)

    Parameters
    **********
    kwargs : 
        Optional (can include any valid keyword argument for the set() method)

    Returns
    *******
    : numpy.float
        The fluence integrated over the spectrum (# per cm2)

    Purpose
    *******
    To obtain the total fluence integrated over the spectrum (summed over energy bins).

Usage:

```python
s = sp.Spek()
fl = s.get_flu()
```


## get_eflu
     
    get_eflu(**kwargs)

    Parameters
    **********
    kwargs : 
        Optional (can include any valid keyword argument for the set() method)

    Returns
    *******
    : numpy.float
        The energy-fluence integrated over the spectrum (keV per cm2)

    Purpose
    *******
    To obtain the total energy fluence integrated over the spectrum (summed over energy bins).

Usage:

```python
s = sp.Spek()
efl = s.get_eflu()
```


## get\_norm\_flu
     
    get_norm_flu(kerma=1, **kwargs)

    Parameters
    **********
    kerma : float
        The kerma to normalize the fluence to (in uGy)
    kwargs : 
        Optional (can include any valid keyword argument for the set() method)

    Returns
    *******
    : numpy.float
        The fluence integrated over the spectrum (# per cm2) normalized to specified kerma

    Purpose
    *******
    To obtain the total fluence integrated over the spectrum (summed over energy bins) that would 
    correspond to a specified air kerma value.

Usage:

```python
s = sp.Spek()
fl = s.get_norm_flu(kerma=100)
```

## get\_std\_results
     
    get_std_results(**kwargs)

    Parameters
    **********
    kwargs : 
        Optional (can include any valid keyword argument for the set() method)

    Returns
    *******
    : StandardResults class
        An instance of the StandardResults class. Attributes include:
            k, spk, flu, kerma, emean, 
            hvl_1_al, hvl_2_al, hc_al, eeff_al,
            hvl_1_cu, hvl_2_cu, hc_cu, eeff_cu

    Purpose
    *******
    Convenient return off all common metrics of interest in one function call. Attributes can be 
    extracted using dot indexing or the in-built getattr() Python method.

Usage:

```python
s=sp.Spek()
res=s.get_std_results()
```

## load\_from\_file
     
    load_from_file(spectrum_name, spectrum_delimeter, z=100.0, mas=1.0, mu_data_source='nist')

    Parameters
    **********
    spectrum_name : str
        The pathname for a spectrum file
    spectrum_delimeter : str
        The delimeter used to separate values in the spectrum file (e.g. ';')
    z : float
        The focus-to-detector distance along central axis (default: 100 cm)
    mas : float
        The exposure for the measurement (default: 1 mAs)
    mu_data_source : str
        The source of linear absorption/attenuation coefficients (default: 'nist', otherwise: 'pene')

    Returns
    *******
    : Spek class
        An new instance of the Spek class based on the external spectrum file

    Purpose
    *******
    Imports an external spectrum that can then be manipulated by and use all the SpekPy tools. The external         
    spectrum is assumed defined on-axis. If metrics are subsequently calculated off-axis, they do not include 
    varying anode self-filtration. The external spectrum should consist of two or three columns of data, 
    separated by delimiters: mid-bin energy in keV, brem+char fluence per keV, char fluence per keV.
    The last column is optional. 

Usage:

```python
e = sp.Spek.load_from_file('my_spectrum', ';')
```

## load_state
     
    load_state(state_name)

    Parameters
    **********
    state_name : str
        The name of a saved state

    Returns
    *******
    : Spek class
        An new instance of the Spek class for the saved state
 
    Purpose
    *******
    Load a saved state previously generated by SpekPy. This avoids the need to redefine parameters 
    and filtering for a spectrum that will be used in separate sessions.

Usage:

```python
s=sp.Spek.load_state('my_state')
```

## make_matl
     
    make_matl(matl_name=None, matl_density=None, wt_matl_comp=None, chemical_formula=None, matl_comment=None)

    Parameters
    **********
    matl_name : str
        The name for the new material
    matl_density : float
        The density for the new material (g/cm3)
    wt_matl_comp : list of tuples
        The composition of the material by weight: each tuple is an atomic number and relative weight by mass
    chemical_formula : str
        The chemical formula for the material (if wt_matl_comp not specified)
    matl_comment : str
        Optional explanatory comment

    Returns
    *******
    None (but creates a new material)

    Purpose
    *******
    Allows the user to generate their own materials to act as filters/attenuators.

Usage:

```python
name = 'Water 1'
comment = 'Defined by relative weights'
composition = [(1, 0.1119), (8, 0.8881)]
sp.Spek.make_matl(matl_name=name, matl_density=1.0, wt_matl_comp=composition, matl_comment=comment)
```

or

```python
name = 'Water 2'
comment = 'Defined by chemical formula'
composition='H2O'
sp.Spek.make_matl(matl_name=name, matl_density=1.0, chemical_formula=composition,matl_comment=comment)
```

## multi_filter
     
    multi_filter(filter_list)

    Parameters
    **********
    filter_list : list of tuples
        A set of filters to apply: each tuples consists of a filter name (str) and thickness (float)

    Returns
    *******
    None (but changes the Spek instance)

    Purpose
    *******
    Allows multiple filters to be applied in one command call.

Usage:

```python
my_filters=[('Al',4.0),('Cu',0.2),('Air',1000)]
s=sp.Spek()
s.multi_filter(my_filters)
```

## save_state
     
    save_state(file_name=None, comment=None)

    Parameters
    **********
    file_name : str
        Name of state (if not supplied, a generic name with timestamp will be assigned)
    comment : str
        Optional explanatory note

    Returns
    *******
    None (but saves a new state in SpekPy's state_usr directory)

    Purpose
    *******
    Allows the user to save a state they will need in another session.
    Note: you cannot specify a different directory to save the file in (always to state_usr). 

Usage:

```python
s=sp.Spek()
state_name='My spectrum state'
s.save_state(state_name)
```

# set
     
    set(**kwargs)

    Parameters
    **********
    kwargs :
        can include kvp, th, dk, mu_data_source, physics, x, y, z, mas, brem, char, obli, ref_kerma, ref_flu,     
        shift

    Returns
    *******
    None (but changes the Spek instance)

    Purpose
    *******
    Changes the SpekPy state, data or reference point. See 
    [here](https://bitbucket.org/spekpy/spekpy_py2.7/wiki/Further%20information) for further information
    on these keyword arguments.
    Note: calling set() without specifying ref_kerma or ref_flu will reset fluence normalization to default.

Usage:

```python
s=sp.Spek()
s.set(kvp=200,brem=True,char=False,z=3500)
```

## summarize
     
    summarize(mode='minimal')

    Parameters
    **********
    mode : str
        Mode for output (default: 'minimal', otherwise: 'full')

    Returns
    *******
    Prints information to screen

    Purpose
    *******
    Prints information to screen. If mode = 'minimal', this information includes the spectrum inputs 
    defining the state. 
    If mode = 'full', then the information includes outputs:
    Fluence; Air kerma; Mean energy;
    1st HVL, Al; 2nd HVL, Al; HC, Al; Eff. energy, Al;
    1st HVL, Cu; 2nd HVL, Cu; HC, Cu; Eff. energy, Cu;

Usage:

```python
s=sp.Spek()
s.summarize(mode='full')
```

## remove_matl
     
    remove_matl(matl_name)

    Parameters
    **********
    matl_name : str
        Name of a user-defined material to be removed

    Returns
    *******
    None (but deletes the specified materials file from SpekPy's matl_usr directory)

    Purpose
    *******
    Used to remove a user-created material when it is no longer required.

Usage:

```python
sp.Spek.remove_matl('my_unwanted_material')
```

## remove_state
     
    remove_state(state_name)

    Parameters
    **********
    state_name : str
        Name of a user-defined state to be removed

    Returns
    *******
    None (but deletes the specified state from SpekPy's state_usr directory)

    Purpose
    *******
    Used to remove a user-created state when it is no longer required.

Usage:

```python
sp.Spek.remove_state('my_unwanted_state')
```

## show_matls
     
    show_matls(matl_name=None, matl_group=None, matl_dir=None)

    Parameters
    **********
    matl_name : str
        Name of materials to show properties for
    matl_group : str
        Name of group to show materials for ('ICRU' or 'ICRP')
    matl_dir :str
        Name of directory to show materials for ('usr' or 'def')

    Returns
    *******
    Prints information to screen

    Purpose
    *******
    Provides information on materials. Only one of matl_name, matl_group and matl_dir can be specified.
    matl_name: prints detailed information on the specified material;
    matl_group: lists the materials in a group (ICRU or ICRP);
    matl_dir: lists all the materials in a directory (matl_usr or matl_def);
    None specified: lists all the materials (matl_usr and matl_def).

Usage:

```python
sp.Spek.show_matl()
sp.Spek.show_matls(matl_dir="def")
sp.Spek.show_matls(matl_group='ICRU')
sp.Spek.show_matls(matl_name='Air')
```

## show_states
     
    show_states(state_dir=None)

    Parameters
    **********
    state_dir : str
        Name of directory to show states for ('usr' or 'def')

    Returns
    *******
    Prints information to screen

    Purpose
    *******
    Provides information on saved states (user and/or default).
    If state_dir is specified ('usr' or 'def') then states will only be listed for that directory.

Usage:

```python
sp.Spek.show_states()
sp.Spek.show_states(state_dir="usr")
```