CoopSim
=======

A computer simulation of the evolution of 
cooperation, based on the book of R.Axelrod: "The
Evolution of Cooperation"

Version: 0.9.9 beta 6 (September 6th, 2015)

(c) 2015 by Eckhart Arnold, MIT Open Source License

Author: Eckhart Arnold
web:    www.eckhartarnold.de
email:  eckhart_arnold@yahoo.de


Description
-----------

CoopSim is a computer program for simulating a game theoretic model of
cooperative behavior that can be used in biology as well as social
sciences. The model is the reiterated pairwise prisoners dilemma that
has been made popular by Robert Axelrod and his book "The Evolution of
Cooperation". The reiterated pairwise prisoners dilemma can be
regarded as a formal description of some (but certainly not all!)
cooperation dilemmas.

CoopSim follows the description in Axelrod's book. Different strategies
can be put against each other in a computer tournament. The user can
select the strategies, adjust game parameters and inspect the outcome
of single matches, the whole tournament and the ecological development
over a sequence of tournaments.

CoopSim is open source software under the MIT License
(https://opensource.org/licenses/MIT).

Most of the development of CoopSim took place 10 years ago. While I still
add changes so that it can run on current machines, I do not think it is
really worth while to develop it further. Due to the use of the wxPython
widgets toolkit it cannot even be ported to Python3.

There exists another project by Vincent Knight, Own Campbell and Marc Harper 
with the same goal, however, that is being actively developed, 
and which I'd like to recommend to anyone interested
in this kind of computer simulations: 
https://github.com/Axelrod-Python/Axelrod


Manual
------

There CoopSim-Manual can be read online: 
http://www.eckhartarnold.de/apppages/onlinedocs/CoopSim_Doc/toc.html 


Some Remarks on Game Theoretical Simulation Models
--------------------------------------------------

While I enjoyed programming CoopSim and doing Prisoner's Dilemma simulations, 
I have become more and more skeptical about game theory as a scientific 
method. In my opinion game theory becomes the most valuable if it is
combined with empirical research - both field research and laboratory
research! Good examples of the combination of empirical and theoretical
research methods can be found in the research on public goods. The challenges
of such research are well described in the book: [Working Together:
Collective Action, the Commons, and Multiple Methods in Practice
by Amy R. Poteete, Marco A. Janssen & Elinor Ostrom,
Princeton University Press2010](http://press.princeton.edu/titles/9209.html).

Unfortunately, though, the research on the Reiterated Prisoner's Dilemma (RPD)
in the Axelrod tradition has for its greater part remained thoroughly
theoretical and the myriads of RPD-simulations that have been conducted have 
in fact contributed only very little to our understanding of the evolution of 
cooperation as a natural and social phenomenon. 
I have expressed my worries about this in a few scientific 
papers and I very much hope that they might convince some simulation
scientists that it is important to be concerned about how their simulations 
can be validated empirically and how their theoretical findings can be 
integrated with empirical research:

[How Models Fail. A Critical Look at the History of Computer
Simulations of the Evolution of Cooperation, in: Catrin Misselhorn
(Ed.): Collective Agency and Cooperation in Natural and Artificial
Systems. Explanation, Implementation and Simulation, Philosophical
Studies Series, Springer 2015, DOI 10.1007/978-3-319-15515-9,
pp. 261-279.]
(http://www.eckhartarnold.de/papers/2015_How_Models_Fail/How_models_fail.html)

[What's wrong with social simulations? in: The Monist 2014 (97,3), 361-379, DOI: 10.5840/monist201497323](http://www.eckhartarnold.de/papers/2014_Social_Simulations/Whats_wrong_with_social_simulations.html)

[Simulation  Models  of   the  Evolution  of   Cooperation  as Proofs of  Logical Possibilities. How Useful Are They? in: Etica & Politica
/ Ethics & Politics, XV, 2013, 2, pp. 101-138](http://www.eckhartarnold.de/papers/2013_Simulations_as_Logical_Possibilities/Arnold_2013_Simulations_as_Proofs_of_Logical_Possibilities.pdf)

