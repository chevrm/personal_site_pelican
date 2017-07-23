#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Marc G Chevrette'
SITENAME = u'Marc Chevrette'
SITESUBTITLE = u'Mining Chemical Diversity'
SITEURL = 'http://chevrm.github.io'

PATH = 'content'

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = u'en'

# Theme declaration
THEME = './elegant'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Currie Lab', 'http://currielab.wisc.edu/'),
         ('Warp Drive', 'http://www.warpdrivebio.com'),)

# Social widget
SOCIAL = (('twitter', 'http://www.twitter.com/wildtypeMC'),
          ('linkedin', 'http://www.linkedin.com/in/chevrette'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

LANDING_PAGE_ABOUT = {'title': 'Mining Chemical Diversity', 'details': 
'''
<p> Bacteria, especially actinomycetes, have a reputation for biosynthesizing chemicals
that are of high clinical or biotechnological value.  Over half of the drugs approved by the
FDA in the past decade are of natural origin or are synthetically derived from natural
scaffolds.  I'm interested in a) developing computational tools to mine genome data from
these bacteria to find novel biosynthetic gene clusters and predict their chemical
products, b) understanding the evolutionary histories and trajectories of these compounds 
to inform discovery stradegies, and c) developing methods of engineering the gene
content of these clusters towards generating even more chemical diversity. </p>

<p> Until recently, I was the Head of Experimental Genomics at
<a href='http://www.warpdrivebio.com'>Warp Drive Bio</a>, which has built the largest
bacterial genome database in history to exploit gene cluster diversity for the discovery
of novel therapeutics and exciting biosynthesis.  I joined
<a href='http://www.genetics.wisc.edu/'>UW-Madison Genetics</a> in 2015 as a member of
<a href='http://currielab.wisc.edu/'>Cameron Currie's lab</a> to continue my research on
specialized metabolites, their role in nature, and the possibility of
enrichment for novel compounds of therapeutic use.  As a
<a href='https://biochem.wisc.edu/cbit'>Chemistry-Biology Interface</a> Predoctoral Fellow,
I take an evolutionary approach to probe the chemical diversity of polyketide and non-ribosomal
peptide gene clusters in many systems, including our model system of symbiosis. </p>

<p> Working towards an understanding of the evolutionary underpinnings of natural product
biosynthesis has two major consequences.  First, it offers a rational prioritization framework
for isolation of strains enriched in novel biosynthetic potential. Second, it leads to
testable hypotheses about the natural roles of natural products.  Uncovering the role these 
molecules play in mediating ecological interations will offer huge insights for optimizing
natural product drug discovery. </p>

<p> The model system to study this phenomenon in the
<a href='http://currielab.wisc.edu/'>Currie Lab</a> is nothing short of fascinating.  Certain
ants are farmers.  These ants farm (and later eat) a fungus, which is highly rich in nutrients.
Like human farmers, the ants have been faced with the challenge of pathogenic decimation of their
"crop".  To circumvent this challenge, millions of years of coevolution has resulted in a symbiotic
relationship between the ants and actinomycete bacteria that coat their bodies.  These bacteria can
synthesize chemical compounds that protect against bad, nasty organisms trying to steal the ant's food.
Today, the actinobacterial strains that coat these ants are specific to a given colony. </p>

<center> <figure> <img src="images/mut.jpg" alt="Leaf-Cutter System"> <figcaption><font 
size="3">Photo: Currie Lab</font></figcaption> </figure> </center>

<p> These bacteria are both highly prolific in specialized metabolite capability and are variable
in their biosynthetic gene cluster content over space and evolutionary time.  Our hypothesis is
that not only can these actinomycetes provide antibiotic and antifungal protection of the ant's
cultivar, they may be a prolific discovery avenue for compounds of human therapeutic and biotechnological
use.  Furthermore, this is an ideal system to study the coevolution of interaction specificity
between the invading pathogen(s) and the actinobacteria. </p>

<center> <figure> <img src="images/struct.jpg" alt="Structures and Activities of Insect-associated Compounds">
<figcaption><font size="3">Photo: Currie Lab</font></figcaption> </figure> </center>

<p> The likelihood of a gene cluster under high selective pressure to hit a eukaryotically conserved
target (and thus a medically relevant target) is relatively high when you consider that millions of
years of selective evolution are on our side.  Nature is spending a lot of energy to make these
molecules, so it follows that they must be making them for a biological reason.  In a variety of
collaborations we hope to prove exactly this while uncovering the evolutionary mechanisms of biosynthesis.
Ecological- and evolutionary-minded investigations of these and other actinomycetes promise exciting
avenues for therapeutic discovery and uncovering the evolutionary mechanisms of biosynthesis. </p>

<p> You can find me reliably on <a href='http://twitter.com/wildtypeMC'>twitter</a> and
<a href='http://www.linkedin.com/in/chevrette'>linkedin</a>.  I have sporadically active
<a href='https://github.com/chevrm'>github</a> and <a href='https://bitbucket.org/chevrm/'>bitbucket</a> accounts,
but typically you will have to ask me for my code. 
Do not be shy!  Feel free to contact me at chevrm (at) gmail (dot) com! </p> 

'''
}

PROJECTS = [	#{'name': 'Twitter',
		#'url': 'http://twitter.com/wildtypeMC',
		#'description': ''},
		#{'name': 'LinkedIn',
		#'url': 'http://www.linkedin.com/in/chevrette',
		#'description': ''},
		#{'name': 'CV',
                #'url': 'https://github.com/chevrm/cv/raw/master/ChevretteCV.pdf',
                #'description': 'PDF download of my CV.'},
		#{'name': 'Google Scholar',
		#'url': 'https://scholar.google.com/citations?user=VX3Laf8AAAAJ&hl=en',
		#'description': 'Links to my publications.'},
		#{'name': 'Bio - Currie Lab',
		#'url': 'https://currielab.wisc.edu/bio.php?id=Marc+Chevrette',
		#'description': ''},
		#{'name': 'Video: Leaf-Cutter Ants',
		#'url': 'https://www.youtube.com/watch?v=Xxnmh4IDYaU',
		#'description': 'A brief video from the NSF outlining major areas of research in the Currie Lab.'},
		{'name': 'Currie Lab Homepage',
		'url': 'http://currielab.wisc.edu/',
		'description': ''},
                {'name': 'WiSolve Consulting Group',
		'url': 'http://www.wisolve.org/',
		'description': ''},
                {'name': 'ComBEE UW',
		'url': 'https://sites.google.com/a/wisc.edu/combee/home',
		 'description': ''},
                {'name': 'UW Genetics',
		'url': 'http://www.genetics.wisc.edu/',
		 'description': ''},
		{'name': 'Warp Drive Bio',
		'url': 'http://www.warpdrivebio.com/',
		'description': ''},
		{'name': 'Johnson Biosignatures Lab',
		'url': 'http://www.johnsonbiosignatureslab.com/',
		'description': ''},
]
