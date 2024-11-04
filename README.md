# RC-FIAP-Curso
RC-FIAP “Reinforced Concrete Frame Inelastic Analysis Platform”, developed in Python, with the analysis library OpenSeesPy at its core, is an open analysis platform conceived to evaluate the seismic vulnerability of different archetypes of reinforced concrete frames, including ACI318 compliant structures. The platform is a tool for educational performance-based earthquake engineering, including research capabilities for risk assessment. In this version of the platform, the fragility assessment is carried in a few seconds from conception to pushover, IDA, or multi-stripe analysis, including design and construction of the nonlinear model. Input variables include number of stories and spans, material properties (steel, concrete), dimensioning of beams and columns, gravity loading, seismic design parameters per ASCE 7-16, damping model, and choice of design detailing per ACI318-19. The GUI-based platform allows studying the impact of these variables in the performance of frames, by including ASCE/SEI 41-17 accept.

Installation instructions
 1. Install Python3 ([Anaconda](https://www.anaconda.com) Recommended)
 2. Install [Openseespy](https://openseespydoc.readthedocs.io/en/latest/src/installation.html) 
 3. Install Pyqt using the Anaconda prompt : conda install -c anaconda pyqt or using pip install pyqt
 4. Clone or download the [RC-FIAP repository](https://github.com/vfceball/RC-FIAP)  
 5. Using your preferred IDE(PyCharm, Spyder) open the RC_FIAP_main.py file

Contact vceballos@uninorte.edu.co for further assistance, or if you need to perform IDA or Conditional Scenario Spectra (CSS) type of analyses.
