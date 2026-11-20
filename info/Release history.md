[ReadMe](../ReadMe),
[Further information](Further%20information),
[Function glossary](Function%20glossary),
[Release history](Release%20history),

# Release history

This page documents the history of releases, including bug identification and resolution.

## Version 2.5.5, Released 2026-11-20

**Minor addition**

Bitbucket have removed Wikis. The information previously on the SpekPy Wiki has been updated and moved to Markdown files in the repository itself.

## Version 2.5.4, Released 2026-01-28

**Bug fix**.

The use of NumPy >= 2.4.0 led to two new bugs:

* Raise TypeError on attempt to convert array with ndim > 0 to scalar

* Warning emitted when using 'where' mask without 'out' 

These issues have been correct in release 2.5.4. Thanks go to Thomas Baudier for bring the issues to our attention.

## Version 2.5.3, Released 2025-08-04

**Bug fix**.

* In some circumstances, for positions x>0 with x large enough (anode-cathode direction), there was a floating-point precision problem that led to (very) anomalously large characteristic contribitions for the default 'casim' model. Now corrected. Thanks go to Azamat Taubaldiev for identifying this issue. This bug did not manifest prior to v2.0.11 (to the best of our knowledge).

## Version 2.5.2, Released 2025-07-02

**(Very) minor addition**.

* An image file illustrating the target geometries for reflection and transmission tubes has been added to the repository

## Version 2.5.1, Released 2025-06-29

**Minor corrections**.

* Bug/limitation: when exporting spectra to files, spectrum model parameters were only recorded to 1 decimal place in the header of the file. This could result in problems with rounding. The decimal places have now been increased to 3, which should reduce issues. A thank you to Anders Berglund for pointing out this issue.

## Version 2.5.0, Released 2025-06-24

**Substantial extensions and some corrections**.

* Further target materials added: Cr, Cu ,Ag and Au in addition to Mo, Rh, W.
* Extension to the modelling of transmission targets.
* Addition of an option to return water kerma or calculate HVL in terms of water kerma instead of air kerma
* Correction of an error that occured for W targets if the kvp was very slightly higher (<0.15 keV) than the K-edge: a thank you to Enze Zhou for pointing this issue out
* Change of the format of spectrum export from fixed decimal precision (.4f) to scientific (.8e): a thank you to Anders Berglund for pointing out the limitations of fixed decimal precision

## Version 2.0.13.1, Released 2024-08-09

**Bug correction (minor).**  An error was raised if the user specified a kVp lower than 20 kV for Mo or Rh targets. Now limit reduced to 10 kV as intended for the release v2.0.13.

## Version 2.0.13, Released 2024-08-05

**Improvements (minor)**. Electron penetration data has been added for the Rh target for first time (instead of extrapolating from Mo). Extra electron penetration data has also been added for Mo. The grid for electron data now is the same for Mo and Rh as for W (up to 50 keV electron energy), that is, tabulations at (10, 15, 20, 25, 30, 40, 50) keV. Further, L-lines have been added for Mo and Rh for the first time.

Consequences:

* Mo and Rh target spectrum available down to 10 kV tube potential (old range: 20 to 50 kV; new range: 10 to 50 kV)
* L-lines of Mo and Rh now present (only relevant when no or very low added filtration present)

This update was made possible due to the work of Artur Omar.

## Version 2.0.12, Released 2024-07-01

**Bug fixes**. Solved incompatability with SciPy 1.14 (thanks to Xandra Campo for pointing out problems). Fully compatable with SciPy 1.14 and NumPy 2.0 but should also still be fully compatiböe with older version (and even Python 2).

## Version 2.0.11.1, Released 2023-11-29

**Bug fix (very minor)**. Corrected an inconsistency between version number in setup.py and \__init__.py. Thanks go to Robert Vorbau for spotting this!

## Version 2.0.11, Released 2023-10-30

**Bug fix**. Corrected a bug identified by a user, which affected the self-filtration of the characteristic radiation for 'casim' and 'uni' physics models (SpekAniso.py). Thankfully, the error seems to have negligible affect in typical scenarios (the benchmark tests are passed both before and after correction). Thanks go to Brecht Laperre for pointing out this bug.

## Version 2.0.10, Released 2023-06-16

**Additions**. Added a check for anode take-off angle so that zero fluence is always returned for negative angles. A warning is also now issued.

**Other**. Changed the import method for scipy.ndimage.map_coordinates (due to deprecation of old syntax)

## Version 2.0.9, Released 2023-06-02

**Additions**. Added electron penetration data to extend the range of tube potentials for SpekPy V2 models. Now covers 10 to 500 kV (instead of 20 to 300 kV). Extra data was also added at intermediate points to aid interpolations. Thanks to Artur Omar for providing the electron data (from PENELOPE Monte Carlo simulations).

Previous numerical results should be reproducible with only small numerical deviations. 

## Version 2.0.8, Released 2022-05-04

Corrected issue #11 in Bitbucket issue tracker (NaN for lowest energy bin in certain circumstances)

Corrected issue #7 in Bitbucket issue tracker (added a docstring for the __init__ method of the Spek() class)

No previous predictions should be modified due to the update, although, depending on precise inputs (kvp, dk, shift), there may be one less energy bin (the first bin is dropped if the lower bin limit is not higher than 1 keV).

## Version 2.0.7, Released 2022-01-19

Minor release correcting some small bugs and adding functionality etc.

**Additions**. Addition of an extra physics mode called 'classical'. This is the same as 'uni' except for it uses Kramers' classical thin target bremsstrahlung cross-section instead of the NIST cross-section. This was included for educational reasons, to support material in our [forthcoming book](https://www.routledge.com/Calculating-X-ray-Tube-Spectra-Analytical-and-Monte-Carlo-Approaches/Poludniowski-Omar-Andreo/p/book/9780367520847). 

**Bug fix**. Corrected a bug that manifested when exporting a spectra elsewhere than the current working directory. Many thanks to Josef Lundman for pointing this out.

**Bug fix**. While correcting the export bug, I noticed an issue with loading a spectrum from a file when running SpekPy in an interpreter (rather than from a script). Now corrected.

**Bug fix**. Dialogue with a user brought to light a bug in the characteristic spectrum. A very small contribution was present in the maximum energy bin for physics models including L-lines. This occurred because the lowest L1 line has an energy lower than 1 keV (the array index ended up as -1). Now fixed. Thanks to Scott Elliott for the discussion leading to this bug fix.

**Behaviour change**. If a path isn't specified the export/import of a spectrum to/from a file uses the current working directory rather than the directory of the script.

**Other**. Changed the way spectrum results are passed to the methods of the state class (now explicitly passed to methods rather than adding to state object in ad hoc fashion). No behaviour change, but the code is less horrible!

## Version 2.0.6, Released 2021-10-06

**Bug fix**. The density of uranium (U.comp) is corrected. It was a factor 10 too low. Thanks go to Andy Soundy for bringing this to our attention.

**Change in default behaviour**. The default for get_kerma() is to provide output as uGy rather than uGy per mAs (the default for the "norm" keyword is now False). Thanks go to "Former user" for bringing the inconsistency with the summarize() method to our attention.

**Bug fix**. In physics='kqp' mode, if a z value was passed to a method, SpekPy threw an error. This has now been corrected.

**Improvement**. show_states() and show_matls() now output entries alphabetically

**Addition**. Copies of some materials have been added with short names: Water, Concrete, Lexan, Mylar, Perspex, Delrin, Teflon, Cellophane, Kapton. Thanks go to "Former user" for the suggestion.

**Addition**. The get_spectrum() method now has an extra keyword "addend". When set to True, it adds an extra bin to the spectrum array, to include a zero fluence point. Sometimes this is useful for plotting spectra 

## Version 2.0.5, Released 2021-05-19

**Bug fix**. The use of the function *scipy.interpolate.interp1d* was causing an error, for some versions of *scipy*. The only observed problem was for *mu_data_source="pene"*, for *Pb*, at photon energies just below the K-edge (around 80-88 keV). Solved in this release.

*Thanks go to Lidiane Évora dos Reis for pointing out the bug.*

## Version 2.0.4, Released 2021-04-11

Two minor additions to assist in comparison of SpekPy with external spectra:

(1) A new optional keyword parameter, *sig*, has been added for the *get_spectrum()* method. The energy resolution of the predictions are degraded by a Gaussian of the requested width. This allows predictions to be matched to the resolution of a detector (*Full-Width-Half-Maximum = 2.355 x sig*). NB: this addition was suggested by an anonymous reviewer.

(2) A new optional keyword parameter, *shift*, has been added for the *Spek* class. This allows the bin centres to be shifted by up to +/- 0.5 times the bin width. The bin centres in SpekPy were chosen for good reasons, but it was annoying when they did not coincide with other spectra (other models or measured).

## Version 2.0.3, Released 2020-12-15

Additional electron penetration data added. Initial energies tabulated are now: (20, 30, 40, 50, 75, 100, 150, 300 keV) for tungsten and (20, 25, 30, 35, 50 keV) for Mo/Rh.

Changes in the interpolation between energies (for e.g. kerma and HVL) should be minimal in all cases (much less than 1%).

The lower limit on the tube potential for the v2 models is now reduced to 20 kV for tungsten (from 30 kV previously).

## Version 2.0.2, Released 2020-12-04

Improved interpolation between tabulated incident electron energies (30, 50, 75, 100, 150, 300 keV) for the physics models added in version 2. This only affects the total fluence, not the spectrum shape, and the total fluence remains unchanged for tube potentials corresponding to the initial electron energies above.

## Version 2.0.1, Released 2020-07-05

Very minor revision. The online Jupyter notebook displayed a warning in Version 2.0.0, due to a deprecated feature in the NumPy library. This has been corrected.

## Version 2.0.0, Released 2020-07-03

Major upgrade based on Omar et al. (2020) Part I and Part II (see references). Extra physics models have been added and the default model has changed.

In the new physics modes ('casim' is the new default) the model covers tungsten anodes (30 to 300 kV) and molybdenum and rhodium anodes (20 to 50 kV). All the new models incorporate the improved characterstic x-ray model of Omar et al. (2018) (see references).

The new methods *get_eflu* (to return energy fluence) and *get_hvl* (which returns same result as *get_hvl1()*) have been added. The method *get_spectrum* now has additional optional inputs allowing the energy-fluence spectrum to be returned as well as the non-differential fluence and energy-fluence spectra (i.e. number of photons per bin *not* number per keV). 

Backwards compatability with v1 has been maintained, except that if no physics model was previously specified, to get the same results you must now specify: *physics='spekpy-v1'* or equivalently (though not recommended because the name is misleading) *physics='default'*.

## Version 1.0.1, Released 2019-11-06

Minor bug fix (get_matl: see [issue](https://bitbucket.org/spekpy/spekpy_release/issues/1/behaviour-of-get_matl)).

## Version 1.0.0, Released 2019-11-04

Initial public release.