+++
title = "Workshop Beyond Boussinesq (Lyon 2023)"
path = "workshop-2023-10/abstracts"
template = "simplepage.html"
+++

# Abstracts

[< Back to main page](@/pages/workshop-2023-10/index.md)

## Convection

- Dimitar Vlaykov - **Mixing at convective boundaries in stars**  
As a problem where multi-dimensional hydrodynamic simulations of stellar
interiors can provide clear guidelines, convective boundary mixing has received
a lot of attention in recent years. In this contribution we review several
recent studies to form a more complete picture of stellar convection and
overshooting. We will outline what has been understood, and discuss questions
that remain open. This discussion will be supported by data from global
simulations of stars produced with the fully compressible MUltidimensional
Stellar Implicit Code (MUSIC), and simulations of pre-main sequence, main
sequence, and red giant branch stars.

- Friedrich Kupka - **The Challenge of Numerical Simulations of Convection**  
Numerical 3D hydrodynamical simulations of convection have become a very
popular tool in astrophysics, both to provide a better understanding of this
process per se and for quantitative predictions in the fields of stellar
structure and evolution, asteroseismology, or stellar activity, among others.
Parameter calibration of simple, algebraic models with this type of numerical
simulations are in high demand especially in asteroseismology and, as a
consequence, exoplanet research. In spite of these incentives, this approach
requires care. In this talk, a spot-light will be given on important pitfalls
of such 3D simulations, particularly from the perspective of numerical
mathematics, and on the fact that even the best 3D simulations cannot overcome
basic limitations of simple models that intrinsically neglect essential physics
of convective energy transport and mixing.

- Yannick Ricard - **Compressible convection in the mantle of exoplanets**  
The radial density of planets increases with depth due to compressibility,
leading to impacts on their convective dynamics. To account for these effects,
including the presence of a quasi-adiabatic temperature profile and entropy
sources due to dissipation, the compressibility is expressed through a
dissipation number proportional to the planet's radius and gravity. In Earth's
mantle, compressibility effects are moderate, but in large rocky or liquid
exoplanets (super-earths), the dissipation number can become very large. We
explore the properties of compressible convection when the dissipation number
is significant. We start by selecting a simple Murnaghan equation of state that
embodies the fundamental properties of condensed matter at planetary
conditions. Next, we analyze the characteristics of adiabatic profiles and
demonstrate that the ratio between the bottom and top adiabatic temperatures is
relatively small and probably less than 2. We examine the marginal stability of
compressible mantles and reveal that they can undergo convection with either
positive or negative superadiabatic Rayleigh numbers. Lastly, we delve into
simulations of convection in 2D Cartesian geometry performed using the exact
equations of mechanics, neglecting inertia (infinite Prandtl number case), and
examine their consequences for super-earth dynamics.

- Mickael Bourgoin - **Preferential concentration of inertial particles in turbulent flows**  
Particle-laden flows are of relevant interest in many industrial and natural
systems. When the carrier flow is turbulent, a striking phenomenon occurs,
where particles with inertia tend to segregate in clusters, also leading to
depleted regions.This mechanism, called preferential concentration, results
from the interaction of the particles with the multi-scale and random structure
of turbulence. The exact mechanism at play and the full dynamical consequences
still remain however to be unveiled. This lecture will be devoted to recent
experimental investigations of clustering of small  water droplets in
homogeneous and isotropic active-grid-generated turbulence. We investigate the
effects of Reynolds number (Rλ, quantifying the turbulence intensity) and
particles Stokes number (St, quantifying particles inertia) on preferential
concentration. Using Voronoï tesselations, we characterise clustering level and
cluster properties (geometry, typical dimensions and fractality). We will show
that the exact same Voronoï analysis can be applied to investigate clustering
properties of specific topological points of the velocity field of single phase
homogeneous isotropic turbulence (obtained for instance from direct numerical
simulations) in order to explore the relevance of possible clustering
mechanisms, such as effective compressibility due to centrifugal effects (heavy
particles sampling preferentially low-vorticity regions) and sweep-stick
mechanisms (heavy particles preferentially sticking to low-acceleration
points). Finally some new questions, such as the possible existence of
super-clusters (clusters of clusters) and the role of particle finite size
effects on preferential concentration phenomenon will be briefly discussed.

- Rene Gassmoeller - **Non-adiabatic boundary layers and complex phase transitions:
  The problem with reference states in Earth's convection**  
Mantle convection and lithosphere dynamics in the Earth and other planets can
be treated as the slow deformation of a highly viscous fluid, and as such can
be described using the compressible Navier-Stokes equations. On Earth-sized
planets compressibility is not a dominant effect and density deviations from a
reference profile are generally less than a few percent. Therefore, most
modelling studies simplify the governing equations. Common approximations
assume a depth-dependent reference profile (the anelastic liquid
approximation), or drop compressibility altogether (the Boussinesq
approximation). In most previous studies, the error introduced by these
approximations was small compared to poorly constrained material properties and
limited numerical accuracy. However, as model parametrizations have become more
realistic, and model resolution has improved, the error by using simplified
conservation equations may no longer be negligible: while such approximations
may be reasonable for iso-chemical models of mantle plumes or subducted plates
traversing the whole mantle, they may be unsatisfactory for layered materials
undergoing significant heating or cooling in boundary layers or materials
experiencing complex, solution-dependent phase transitions. Here, I will
discuss other formulations of the continuity equation that include dynamic
density variations due to temperature, pressure and composition without a
density reference state. I also discuss the use of entropy instead of
temperature and its benefits for modelling complex phase transitions.
Quantifying the improvement in accuracy relative to existing formulations in a
number of benchmark models allows us to evaluate for which practical
applications these effects are important. Finally, I will present numerical
aspects of the new formulations and will conclude with remaining challenges.
The presented formulations are implemented and tested in the freely available
community software ASPECT.

- Stephane Labrosse - **Scaling of internally heated compressible convection**  
The thermal evolution of terrestrial planets is paced by the efficiency of
convective heat transfer in their rocky mantle. Two types of heat sources
produce buoyancy in such layers, the temperature difference between the surface
and the hot core and the radiogenic heating source that is distributed in the
bulk. The scaling of such mixed heating convection is rather well established
for incompressible fluids in the Boussinesq approximation and we extend this
scaling to the case of fully compressible fluids, using the Murnaghan equation
of state developed by Ricard et al (2022). The convection equations are solved
in 2D using Dedalus (Burns et al 2020). The system is controlled by 7
dimensionless numbers but we fix 4 of them to typical planetary values and
explore the parameter space formed by Ra, H and Di, the Rayleigh number,
internal heating rate and dissipation number. Compared to the Boussinesq case
where a slightly stably stratified mean temperature gradient develops in the
bulk in presence of internal heating, we find that the mean temperature profile
is closer to the isentropic reference when compressibility is considered.
Defining super-isentropic Rayleigh and Nusselt numbers allows us to recover
classical boundary layer-type scaling laws.

- Thierry Alboussiere - **Perspectives in compressible convection experiments**  
Compressible effects in planets and stars are essentially due to the large
length-scales of these objects. Reproducing them in a laboratory small-scale
experiment is challenging. In the rotor of a centrifuge, one can take advantage
of the large apparent gravity field and reach values of the dissipation
parameter similar to those of planetary interiors. This can be achieved using
gas as convective medium and its equation of state is thus very different from
that of condensed matter. Another difference is related to the importance of
Coriolis forces. It can be negligible as in Mantle convection or very strong as
in core convection. In a rotor centrifuge, its relative importance is bound to
be even larger than in core convection, to the point that two-dimensional
convection will be realized in most cases. In terms of intensity of convection,
as measured by a Rayleigh number, experiments in a rotor centrifuge are capable
of reaching much larger values than those accessible to numerical simulation.
This gives a specific advantage to the experiments as they are an intermediate
step toward the geo and astro-physical objects, where extreme values of
Rayleigh numbers can be found.

## Double-diffusive convection

- Remi Bourgeois (with Pascal Tremblin) - **Finite volume methods for compressible convection**  
We introduce a new class of finite-volume solvers for stratified flows based on
a flux-splitting approach. This approach can be easily extended to the MHD
system with gravity, and we present first applications of this solver to the
study of an extension of the double-diffusive convective theory to MHD leading
to triple-diffusive systems. We will discuss the comparison between 2D/3D
numerical experiments and theory.

- Adrien Morison - **Fully compressible numerical simulations of double-diffusive convection**  
I use the fully compressible finite volume numerical code MUSIC to simulate
double-diffusive convection.  I focus in particular on the consequences of
increasing the compressibility (i.e. departing from Boussinesq-like regimes) in
simple setups.

- Friedrich Kupka (with Florian Zaussinger) - **Compressible double-diffusion convection**

- Ulrich Hansen - **Double diffusive convection in geological systems**  
In most geological systems the density is determined by a least two components,
(a) the temperature and (b) the concentration of  chemical components. Since
the molecular diffusivities of both ingredients are very different ( the
chemical diffusivity can be virtually zero) these systems are prone to exhibit
double diffusive convection. Systems of investigation range from small scale
magma chambers to convective phenomena of planetary scale. Especially the
formation of distinct layers in magma chambers has been investigated  in the
context of double diffusive convection. Layer formation seems a very generic
feature in geology and it seems necessary to better understand the mechanisms
behind it. For example, the internal structure of the Earth is made up by
several layers, while it is unclear how many layers today exist and if all
layers are visible to remote sensing techniques. Layering can hardly be
explained by gravitational settling. Double-diffusive convection in the
diffusive regime, where the fast diffusing component (heat)  drives the flow,
while the slowly diffusing component (composition) acts as restoring force is
believed to a vital mechanism for layer generation. . A relatively high
viscosity is typical for geological systems, in general so high that mechanical
inertia is virtually negligible and the flow is characterized by an infinite
Prandtl number. At the same time, the thermal Rayleigh number is high (Ra >
$10^8$), such that thermal inertia plays a dominant role. Another typical feature
is the very strong dependence of the viscosity on temperature. Hot material can
be orders of magnitude less viscous than cold material.  
We have investigated the double diffusive convection in such a setting, i.e. in
a fluid with strongly temperature dependent viscosity (at least 6 orders of
magnitude) at infinite Prandtl number.  By choosing an initial condition in
which a compositional stably stratified fluid overlies a hot reservoir , we
mimic the situation in the early Earth after core formation. Differently from
earlier experiments we fixed the temperature rather than the heat flux at the
lower boundary, resembling a more realistic condition for the boundary between
Earth's core and mantle. We ran a series of numerical experiments in 2 and 3D
geometries  ranging from simple (constant viscosity) to complex rheologies
(strongly temperature and stress-dependent viscosity). For a wide range of
buoyancy ratios the initial non-layered structure develops  into a state with
several separately convecting layers. Since temperature is fixed at the bottom,
the layer formation is a self organized process, rather than driven
externally. In the course of the experiment the number of layers varies and in
the run -down cases ( i.e. zero-compositional flux is assumed at all
boundaries) the layering finally disappears. Temperature dependent viscosity is
found to significantly stabilize the layers. A dynamical model of a planetary
mantle , taking into account double diffusive convection in a fluid with
complex rheology leads to thermal history model of a planet (especially Earth)
which can potentially explain several features , like the existence of chemical
reservoirs and also the onset of plate tectonics.  
Further numerical experiments will be presented, carried out to better
understand the role of the absolute value of the Rayleigh number on layer
formation in the diffusive regime. Also the fingering regime has been
investigated , having in mind the thermo-chemical evolution of magma chambers.
Here we have concentrated on the effect of compositional and temperature
dependent viscosity on the flow.

- Celine Guervilly - **Fingering convection in planetary cores**  
We study fingering convection in the context of stably-stratified layers in
planetary cores, using hydrodynamical numerical simulations in a rotating
spherical shell. In this talk, we will discuss how the size and velocity of the
flow structures vary with the stratification and rotation rate. We will also
describe the formation of zonal flows in this system. 

- Andreas Tilgner - **Experiments on double diffusive finger convection**  
Double diffusive systems of interest are usually characterized by two diffusion
constants differing by several orders of magnitude. This presents a challenge
for numerical simulations. The resulting difficulties are particularly striking
in the case of finger convection with staircases when narrow slowly evolving
fingers coexist with large scale turbulent convection rolls and all structures
need to be resolved. Experimental studies of such systems are therefore
essential. This contribution will present experiments which used an
electrodeposition cell to sustain a destabilizing concentration difference of
copper ions in aqueous solution between the top and bottom boundaries of the
cell. The resulting convecting motion is analogous to Rayleigh- Bénard
convection at high Prandtl numbers if the cell is kept at spatially uniform
temperature. If a stabilizing temperature gradient is imposed across the cell,
double diffusive fingers appear even for thermal buoyancy two orders of
magnitude smaller than chemical buoyancy. It is found that the fingers obey
several simple scaling laws. The control parameters can also be chosen such
that fingers and convection rolls coexist in vertically stacked layers, the so
called staircases. Staircases are observed even if the density stratification
is unstable. The mechanisms governing the transitions from a single convection
roll to a single finger layer and a staircase will be discussed.

- Andrew Cumming - **Composition gradients and convection in dense interiors: giant planets and white dwarfs**  
I will discuss two situations involving the interaction of composition
gradients and convection driven by boundary fluxes: the evolving composition
profile of Jupiter's interior and crystallization-driven fingering convection
in white dwarfs. Both are motivated by recent observational results - the
inferred density profile of Jupiter from the Juno mission, and new results on
cooling white dwarfs from Gaia. For both situations, I will discuss the
important role of rotation, and likely important effects of compressibility
which has yet to be included in simulations. For Jupiter, I will show results
from Boussinesq simulations of penetrative convection and layer formation at
Prandtl number<1, and discuss the penetration rate and the mechanism for layer
formation and how it compares to evolutionary models of Jupiter. These
simulations suggest that rotation acts to significantly reduce the efficiency
with which heavy elements can be mixed into the convection zone. For white
dwarfs, I will discuss the regime of convection driven by chemical separation
during crystallization. The large thermal conductivity of the white dwarf
generally leads to fingering/thermohaline convection with up-gradient heat
transport. I will show the current state of evolutionary models and
(Boussinesq) simulations of this kind of convection, and discuss what further
work is needed to be able to accurately follow the evolution and to assess
whether white dwarf magnetic fields could originate from a
crystallization-driven dynamo.

## Gravity waves (and associated problems)

- Kevin Belkacem - **Gravity waves and induced transport of angular momentum in radiative interior of low-mass stars**  
Transport of angular momentum is a long-standing problem in stellar physics
which recently became more acute thanks to the observations of the space-borne
mission CoRoT and Kepler. Indeed, the need for an efficient mechanism able to
explain the rotation profile of low-mass stars has been emphasized by
asteroseimology and waves are among the potential candidates to do so. After
reviewing the observational constraints we now have for rotation profiles in
low-mass stars, I will focus on how waves are able to transport and
redistribute angular momentum in these stars. Particular emphasis will be given
on the importance of realistic estimate of wave generation together with the
importance of properly considering interactions between meridional circulation
and waves.

- Arthur Le Saux - **Studying internal gravity waves in stellar interiors with fully compressible simulations**  
To date, the properties of internal gravity waves (IGWs) in stellar interiors
remain poorly constrained because of the challenge of observing them. Indeed,
in low-mass stars, which possess a convective envelope, they propagate in the
inner radiative region and have very small amplitude at the photosphere. In
higher mass stars, IGWs are generated at the edge of the convective core and
can propagate in the radiative envelope but it remains unclear if they can
travel up to the stellar surface.  
Hydrodynamical simulations thus offer a great opportunity to study the
properties of IGWs and thus to guide observations. I will present a study of
IGWs properties in solar-like and intermediate-mass stars based on 2D stellar
structure models preformed with a fully compressible hydrodynamics time
implicit code, the MUSIC code. Our results present a good agreement with
theoretical predictions concerning waves generation, propagation and damping by
radiative effects. In addition, to model realistic IGWs propagating in
radiative zone of stars, it is crucial to include a realistic profile of
radiative diffusion in hydrodynamical simulations. Especially as it is through
radiative damping that waves are able to transport angular momentum and energy.  
Finally, we add a word of caution regarding the interpretation of results from
simulations as their numerical set up can have an impact of physical phenomena.
Consequently, direct comparison between numerical simulations and observations
must be made with caution.

- Daniel Lecoanet - **Generation and Propagation of Convectively Excited Gravity Waves**  
Many astrophysical and geophysical systems have regions which are unstable to
convective adjacent to stably-stratified regions. In these cases, the
convection can excite internal gravity waves. In turn, these waves can
transport angular momentum, energy, and chemicals. Here we will present a
series of increasingly realistic numerical simulations of convective excitation
and subsequent propagation of gravity waves. In all cases, the wave generation
matches classic theoretical predictions, and the wave propagation follows from
linear theory. This gives robust estimates for the amplitudes of internal
gravity waves in astrophysical and geophysical systems, which can then be used
to parametrize wave mixing and transport.

- Guillaume Laibe - **Topology for stars and discs pulsations**  
Global modes of stellar and disc pulsations are revisited with topological
tools inherited from condensed matter physics. We present topological
quantities to which the existence and the signature of stable and unstable
topological modes are connected, and explain the central role played by
compressibility in these systems.

- Guillaume Roullet - **The energetics of mixing in implicit large eddy simulations of oceanic flows**  
Implicit large eddy simulations (ILES) are a tool to study flows at very large
Reynolds numbers. Compared to explicit LES, ILES do not have an explicit
sub-grid closure controlling the key turbulent processes such as mixing and
dissipation. In ILES these processes are performed implicitly by the numerics
which handles the resolved transport. As a result, these processes seem to
emerge from a black box. This is a strong critique to ILES. Here, we present a
method to diagnose the local rates of tracer mixing and energy dissipation in
ILES. The method is based on extracting the irreversible part of the numerical
fluxes. We apply the method to a series of idealized Boussinesq stratified
flows, including a convection experiment and a gravity current. These local
rates, complemented with the injection rate and the conversion rate allow to
monitor the exchanges of energy between the kinetic energy, the available
potential energy and the background energy reservoirs. This energy cycle
reveals how the flows work, from the energy point of view. The diagnostic also
naturally provides the mixing efficiency of the flows, which turns out to
crucially depend on the primary source of energy, whether it is kinetic or
potential.

- Joel Sommeria - **From internal gravity waves to turbulence and mean flow generation**  
An overview of experiments on internal gravity waves and inertio-gravity waves
performed on the Coriolis rotating platform at Grenoble will be presented.
Regimes of wave turbulence are observed in a closed domain, involving cascade
process by wave-wave interactions. Stratified turbulence is obtained at small
scales as the outcome of this cascade process. Consequences for vertical mixing
and mean flow generation by turbulence will be discussed.

- Eyal Heifetz - **On the non-Boussinesq effect of self gravitating Rossby interfacial waves in proto-stellar accretion discs**  
The dynamical response of edge waves under the influence of self-gravity is
examined in an idealised two-dimensional model of a proto-stellar disc,
characterised in steady state as a rotating vertically infinite cylinder of
fluid with constant density except for a single density interface at some
radius $r_0$. The fluid in basic state is prescribed to rotate with a Keplerian
profile $Ω_k(r)\sim r^{−3/2}$ modified by some additional azimuthal sheared
flow. A linear analysis shows that there are two azimuthally propagating edge
waves, kin to the familiar Rossby waves and surface gravity waves in
terrestrial studies, which move opposite to one another with respect to the
local basic state rotation rate at the interface. Instability only occurs if
the radial pressure gradient is opposite to that of the density jump (unstably
stratified) where self-gravity acts as a wave stabiliser irrespective of the
stratification of the system. The propagation properties of the waves are
discussed in detail in the language of vorticity edge waves. The roles of both
Boussinesq and non-Boussinesq effects upon the stability and propagation of
these waves with and without the inclusion of self-gravity are then quantified.
The dynamics involved with self-gravity non-Boussinesq effect is shown to be a
source of vorticity production where there is a jump in the basic state density
In addition, self-gravity also alters the dynamics via the radial main pressure
gradient, which is a Boussinesq effect. Further applications of these
mechanical insights are presented in the conclusion including the ways in which
multiple density jumps or gaps may or may not be stable.

## Beyond sphericity: deformation effects due to fast rotation

- Michel Rieutord - **Modelling Rapidly Rotating Stars**  
I shall present a few results obtained within the ESTER project on modelling
actual stars like Altair, anticipating evolution of massive stars or predicting
the spectral energy distribution of fast rotating stars.

- Thomas Guillet - **Directions and prospects for stellar hydrodynamics simulations with MUSIC**  
I will present some possible future directions for simulations of stellar
hydrodynamics with the MUSIC code, including convection in fast-rotating stars,
as well as prospects towards improving our understanding of stellar convection
and waves.

- Thomas Gastine - **Numerical models of rotating convection in spherical shells**

- Benjamin Favier - **Wall modes in rapidly-rotating convection: an experimental
challenge solved by numerical simulations?**  
Rapidly-rotating thermal convection is relevant in many planetary cores but
remains an asymptotic regime difficult to probe numerically or
experimentally. Most existing experimental setups are using a cylindrical
container elongated along the rotation axis. Unfortunately, recent measurements
show the emergence of strong zonal flows attached to the vertical side wall,
which significantly perturb the geophysically-relevant heat flux transported by
the bulk flow. I will first discuss their origin and illustrate their
surprising robustness, reminiscent of topologically-protected edge states in
condensed-matter physics. In a second part, I will show using numerical
simulations how to suppress them and potentially achieve the geophysically
relevant regime of rotating convection in the lab.

- Jerome Noir - **On the effects of small scale topography in rotating fluids**  
Geophysical observations suggest the CMB is not perfectly smooth, nor is the
bottom of our oceans, the same is likely to be true in Earth-like planets and
icy satellites. How does the small scale topography affect the coupling between
the fluid and solid layers in planets remains an open question. Most efforts on
this topic focus to oceanic and atmospheric circulation,  with a particular
emphasis on local and meso-scale dynamics. Numerically very challenging, this
topic might be better approach through experiments. I will present some
experimental results on the effect of topography in rapidly rotating fluid for
quasi-steady flows, Spin-up/Down, and oscillatory inertial waves.

- David Cébron - **Simulations of non-spherical liquid cores of planets**  
Current simulations of planetary cores consider spherical shells. Such
geometries are indeed well suited for convection, and allow the use of fast
spectral codes (based on spherical harmonics). However, certain observations
motivate the modelling of non-spherical cores. For instance, the early magnetic
fields of the Earth and Moon, as inferred from paleomagnetic data, call for
further investigations of the dynamos driven by tides and precession,
respectively. Yet, these unusual dynamo mechanisms require large-scale
departures from spherical geometries. The opposite small-scale limit is also of
interest to explain the dissipative coupling constant used in the Earth’s
nutation models. I will present how these various deformations can be modelled
for planetary cores by using different complementary methods to account for
buoyancy, rotation, and magnetic effects.

- Michael Le Bars - **Turbulence driven by tides and libration**  
Rotating turbulence is commonly known for being dominated by geostrophic
vortices that are invariant along the rotation axis and undergo an inverse
cascade. Yet, another state of inertial wave turbulence is also possible, with
weakly non-linearly interacting inertial waves driving fully three-dimensional
motions and a downscale energy cascade. This second state could be especially
relevant in planetary and stellar non-convecting interiors, where energy is
injected through wave excitation via gravitational interactions including tides
and libration. The presence of inertial wave turbulence in such systems would
then significantly change our current understanding of dissipation, mixing, and
dynamo mechanism. In this talk, I will review our experimental and numerical
works focusing on the conditions of emergence and on the characteristics of the
inertial wave turbulence, and I will discuss the future challenges for
planetary and stellar applications.

