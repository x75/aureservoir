# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.31
#
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

"""

aureservoir is an open-source (L-GPL) C++ library for analog
reservoir computing neural networks. The basic class is the ESN
(Echo State Network) class, which can be used in single or double
precision (SingleESN, DoubleESN).

Echo State Networks can be used with different initialization,
training and simulation algorithms - which can be choosen at runtime
from the definitions in the DATA section of the module documentation.
For more info on ESNs see docstrings of DoubleESN or SingleESN.

You can find autogenerated docstrings for most of the methods - for
more detailed documentation see the doxygen documentation of the
whole library at http://grh.mur.at (URL not yet valid).

2007, by
Georg Holzmann
grh _at_ mur _dot_ at
http://grh.mur.at

"""

import _aureservoir
import new
new_instancemethod = new.instancemethod
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


class DoubleESN(_object):
    """
    class for a basic Echo State Network

    This class implements a basic Echo State Network as described in
    articles by Herbert Jaeger on the following page: See:
    http://www.scholarpedia.org/article/Echo_State_Network  The template
    argument T can be float or double. Single Precision (float) saves
    quite some computation time.

    The "echo state" approach looks at RNNs from a new angle. Large RNNs
    are interpreted as "reservoirs" of complex, excitable dynamics.
    Output units "tap" from this reservoir by linearly combining the
    desired output signal from the rich variety of excited reservoir
    signals. This idea leads to training algorithms where only the
    network-to-output connection weights have to be trained. This can be
    done with known, highly efficient linear regression algorithms. from
    See:  http://www.faculty.iu-bremen.de/hjaeger/esn_research.html

    C++ includes: esn.h 
    """
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DoubleESN, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DoubleESN, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self) -> DoubleESN
        __init__(self, DoubleESN src) -> DoubleESN

        Copy Constructor.

        Todo check if maps operator= performs a deep copy !

        Todo bei SIM_BP die restlichen buffer variablen auch kopieren 
        """
        this = _aureservoir.new_DoubleESN(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _aureservoir.delete_DoubleESN
    __del__ = lambda self : None;
    def init(*args):
        """
        init(self)

        throw ( AUExcept)
        Initialization Algorithm for an Echo State Network See:  class
        InitBase 
        """
        return _aureservoir.DoubleESN_init(*args)

    def resetState(*args):
        """
        resetState(self)

        resets the internal state vector x of the reservoir to zero 
        """
        return _aureservoir.DoubleESN_resetState(*args)

    def adapt(*args):
        """adapt(self, double inmtx) -> double"""
        return _aureservoir.DoubleESN_adapt(*args)

    def train(*args):
        """
        train(self, double inmtx, double outmtx, int washout)

        throw ( AUExcept)
        C-style Training Algorithm Interface (data will be copied into a FLENS
        matrix) See:  class TrainBase

        Parameters:
        -----------

        inmtx:  input matrix in row major storage (usual C array) (inputs x
        timesteps)

        outmtx:  output matrix in row major storage (outputs x timesteps) for
        teacher forcing

        washout:  washout time in samples, used to get rid of the transient
        dynamics of the network starting state 
        """
        return _aureservoir.DoubleESN_train(*args)

    def simulate(*args):
        """
        simulate(self, double inmtx, double outmtx)

        throw ( AUExcept)
        C-style Simulation Algorithm Interface with some additional error
        checking. (data will be copied into a FLENS matrix) See:  class
        SimBase

        Parameters:
        -----------

        inmtx:  input matrix in row major storage (usual C array) (inputs x
        timesteps)

        outmtx:  output matrix in row major storage (outputs x timesteps),

        Data must be already allocated! 
        """
        return _aureservoir.DoubleESN_simulate(*args)

    def simulateStep(*args):
        """
        simulateStep(self, double invec, double outvec)

        throw (
        AUExcept) C-style Simulation Algorithm Interface, for single step
        simulation See:  class SimBase Todo see if we can do this in python
        without this additional method

        Parameters:
        -----------

        inmtx:  input vector, size = inputs

        outmtx:  output vector, size = outputs

        Data must be already allocated! 
        """
        return _aureservoir.DoubleESN_simulateStep(*args)

    def setBPCutoff(*args):
        """
        setBPCutoff(self, double f1vec, double f2vec)

        throw (
        AUExcept) Set lowpass/highpass cutoff frequencies for bandpass style
        neurons " (C-style Interface).

        Parameters:
        -----------

        f1:  vector with lowpass cutoff for all neurons (size = neurons)

        f2:  vector with highpass cutoffs (size = neurons) 
        """
        return _aureservoir.DoubleESN_setBPCutoff(*args)

    def setIIRCoeff(*args):
        """setIIRCoeff(self, double bmtx, double amtx)"""
        return _aureservoir.DoubleESN_setIIRCoeff(*args)

    def post(*args):
        """
        post(self)

        posts current parameters to stdoutTodo maybe return a outputstream (if
        stdout is not useful) or just use the << operator ? 
        """
        return _aureservoir.DoubleESN_post(*args)

    def getSize(*args):
        """
        getSize(self) -> int

        reservoir size (nr of neurons) 
        """
        return _aureservoir.DoubleESN_getSize(*args)

    def getInputs(*args):
        """
        getInputs(self) -> int

        nr of inputs to the reservoir 
        """
        return _aureservoir.DoubleESN_getInputs(*args)

    def getOutputs(*args):
        """
        getOutputs(self) -> int

        nr of outputs from the reservoir 
        """
        return _aureservoir.DoubleESN_getOutputs(*args)

    def getNoise(*args):
        """
        getNoise(self) -> double

        current noise level 
        """
        return _aureservoir.DoubleESN_getNoise(*args)

    def getInitParam(*args):
        """
        getInitParam(self, InitParameter key) -> double

        returns an initialization parametern from the parameter map

        Parameters:
        -----------

        key:  the requested parameter

        the value of the parameter 
        """
        return _aureservoir.DoubleESN_getInitParam(*args)

    def getInitAlgorithm(*args):
        """
        getInitAlgorithm(self) -> int

        initialization algorithm 
        """
        return _aureservoir.DoubleESN_getInitAlgorithm(*args)

    def getTrainAlgorithm(*args):
        """
        getTrainAlgorithm(self) -> int

        training algorithm 
        """
        return _aureservoir.DoubleESN_getTrainAlgorithm(*args)

    def getSimAlgorithm(*args):
        """
        getSimAlgorithm(self) -> int

        simulation algorithm 
        """
        return _aureservoir.DoubleESN_getSimAlgorithm(*args)

    def getReservoirAct(*args):
        """
        getReservoirAct(self) -> int

        reservoir activation function 
        """
        return _aureservoir.DoubleESN_getReservoirAct(*args)

    def getOutputAct(*args):
        """
        getOutputAct(self) -> int

        output activation function 
        """
        return _aureservoir.DoubleESN_getOutputAct(*args)

    def getWin(*args):
        """
        getWin(self, double mtx)

        get pointer to input weight matrix data and dimensions WARNING:  This
        data is in fortran style column major storage ! 
        """
        return _aureservoir.DoubleESN_getWin(*args)

    def getWback(*args):
        """
        getWback(self, double mtx)

        get pointer to feedback weight matrix data and dimensions WARNING:
        This data is in fortran style column major storage ! 
        """
        return _aureservoir.DoubleESN_getWback(*args)

    def getWout(*args):
        """
        getWout(self, double mtx)

        get pointer to output weight matrix data and dimensions WARNING:  This
        data is in fortran style column major storage ! 
        """
        return _aureservoir.DoubleESN_getWout(*args)

    def getX(*args):
        """
        getX(self, double vec)

        get pointer to internal state vector x data and length 
        """
        return _aureservoir.DoubleESN_getX(*args)

    def getW(*args):
        """
        getW(self, double wmtx)

        throw ( AUExcept)
        Copies data of the sparse reservoir weight matrix into a dense C-style
        matrix. Memory of the C array must be allocated before!

        Parameters:
        -----------

        wmtx:  pointer to matrix of size (neurons_ x neurons_)

        Todo check if this can be avoided 
        """
        return _aureservoir.DoubleESN_getW(*args)

    def setInitAlgorithm(*args):
        """
        setInitAlgorithm(self, InitAlgorithm alg=INIT_STD)
        setInitAlgorithm(self)

        throw (
        AUExcept) set initialization algorithm 
        """
        return _aureservoir.DoubleESN_setInitAlgorithm(*args)

    def setTrainAlgorithm(*args):
        """
        setTrainAlgorithm(self, TrainAlgorithm alg=TRAIN_LEASTSQUARE)
        setTrainAlgorithm(self)

        throw (
        AUExcept) set training algorithm 
        """
        return _aureservoir.DoubleESN_setTrainAlgorithm(*args)

    def setSimAlgorithm(*args):
        """
        setSimAlgorithm(self, SimAlgorithm alg=SIM_STD)
        setSimAlgorithm(self)

        throw (
        AUExcept) set simulation algorithm 
        """
        return _aureservoir.DoubleESN_setSimAlgorithm(*args)

    def setSize(*args):
        """
        setSize(self, int neurons=10)
        setSize(self)

        throw ( AUExcept)
        set reservoir size (nr of neurons) 
        """
        return _aureservoir.DoubleESN_setSize(*args)

    def setInputs(*args):
        """
        setInputs(self, int inputs=1)
        setInputs(self)

        throw (
        AUExcept) set nr of inputs to the reservoir 
        """
        return _aureservoir.DoubleESN_setInputs(*args)

    def setOutputs(*args):
        """
        setOutputs(self, int outputs=1)
        setOutputs(self)

        throw (
        AUExcept) set nr of outputs from the reservoir 
        """
        return _aureservoir.DoubleESN_setOutputs(*args)

    def setNoise(*args):
        """
        setNoise(self, double noise)

        throw ( AUExcept)
        set noise level for training/simulation algorithm

        Parameters:
        -----------

        noise:  with uniform distribution within [-noise|+noise] 
        """
        return _aureservoir.DoubleESN_setNoise(*args)

    def setInitParam(*args):
        """
        setInitParam(self, InitParameter key, double value)

        set initialization parameter 
        """
        return _aureservoir.DoubleESN_setInitParam(*args)

    def setReservoirAct(*args):
        """
        setReservoirAct(self, ActivationFunction f=ACT_TANH)
        setReservoirAct(self)

        throw (
        AUExcept) set reservoir activation function 
        """
        return _aureservoir.DoubleESN_setReservoirAct(*args)

    def setOutputAct(*args):
        """
        setOutputAct(self, ActivationFunction f=ACT_LINEAR)
        setOutputAct(self)

        throw (
        AUExcept) set output activation function 
        """
        return _aureservoir.DoubleESN_setOutputAct(*args)

    def setWin(*args):
        """
        setWin(self, double inmtx)

        throw ( AUExcept)
        set input weight matrix C-style interface (data will be copied into a
        FLENS matrix)

        Parameters:
        -----------

        inmtx:  pointer to win matrix in row major storage 
        """
        return _aureservoir.DoubleESN_setWin(*args)

    def setW(*args):
        """
        setW(self, double inmtx)

        throw ( AUExcept) set
        reservoir weight matrix C-style interface (data will be copied into a
        FLENS matrix)

        Parameters:
        -----------

        inmtx:  pointer to a dense reservoir matrix in row major storage 
        """
        return _aureservoir.DoubleESN_setW(*args)

    def setWback(*args):
        """
        setWback(self, double inmtx)

        throw ( AUExcept)
        set feedback weight matrix C-style interface (data will be copied into
        a FLENS matrix)

        Parameters:
        -----------

        inmtx:  pointer to wback matrix in row major storage 
        """
        return _aureservoir.DoubleESN_setWback(*args)

    def setWout(*args):
        """
        setWout(self, double inmtx)

        throw ( AUExcept)
        set output weight matrix C-style interface (data will be copied into a
        FLENS matrix)

        Parameters:
        -----------

        inmtx:  pointer to wout matrix in row major storage 
        """
        return _aureservoir.DoubleESN_setWout(*args)

    def setX(*args):
        """
        setX(self, double invec)

        throw ( AUExcept) set
        internal state vector C-style interface (data will be copied into a
        FLENS matrix)

        Parameters:
        -----------

        invec:  pointer to state vector 
        """
        return _aureservoir.DoubleESN_setX(*args)

DoubleESN_swigregister = _aureservoir.DoubleESN_swigregister
DoubleESN_swigregister(DoubleESN)

class SingleESN(_object):
    """
    class for a basic Echo State Network

    This class implements a basic Echo State Network as described in
    articles by Herbert Jaeger on the following page: See:
    http://www.scholarpedia.org/article/Echo_State_Network  The template
    argument T can be float or double. Single Precision (float) saves
    quite some computation time.

    The "echo state" approach looks at RNNs from a new angle. Large RNNs
    are interpreted as "reservoirs" of complex, excitable dynamics.
    Output units "tap" from this reservoir by linearly combining the
    desired output signal from the rich variety of excited reservoir
    signals. This idea leads to training algorithms where only the
    network-to-output connection weights have to be trained. This can be
    done with known, highly efficient linear regression algorithms. from
    See:  http://www.faculty.iu-bremen.de/hjaeger/esn_research.html

    C++ includes: esn.h 
    """
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SingleESN, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SingleESN, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self) -> SingleESN
        __init__(self, SingleESN src) -> SingleESN

        Copy Constructor.

        Todo check if maps operator= performs a deep copy !

        Todo bei SIM_BP die restlichen buffer variablen auch kopieren 
        """
        this = _aureservoir.new_SingleESN(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _aureservoir.delete_SingleESN
    __del__ = lambda self : None;
    def init(*args):
        """
        init(self)

        throw ( AUExcept)
        Initialization Algorithm for an Echo State Network See:  class
        InitBase 
        """
        return _aureservoir.SingleESN_init(*args)

    def resetState(*args):
        """
        resetState(self)

        resets the internal state vector x of the reservoir to zero 
        """
        return _aureservoir.SingleESN_resetState(*args)

    def adapt(*args):
        """adapt(self, float inmtx) -> double"""
        return _aureservoir.SingleESN_adapt(*args)

    def train(*args):
        """
        train(self, float inmtx, float outmtx, int washout)

        throw ( AUExcept)
        C-style Training Algorithm Interface (data will be copied into a FLENS
        matrix) See:  class TrainBase

        Parameters:
        -----------

        inmtx:  input matrix in row major storage (usual C array) (inputs x
        timesteps)

        outmtx:  output matrix in row major storage (outputs x timesteps) for
        teacher forcing

        washout:  washout time in samples, used to get rid of the transient
        dynamics of the network starting state 
        """
        return _aureservoir.SingleESN_train(*args)

    def simulate(*args):
        """
        simulate(self, float inmtx, float outmtx)

        throw ( AUExcept)
        C-style Simulation Algorithm Interface with some additional error
        checking. (data will be copied into a FLENS matrix) See:  class
        SimBase

        Parameters:
        -----------

        inmtx:  input matrix in row major storage (usual C array) (inputs x
        timesteps)

        outmtx:  output matrix in row major storage (outputs x timesteps),

        Data must be already allocated! 
        """
        return _aureservoir.SingleESN_simulate(*args)

    def simulateStep(*args):
        """
        simulateStep(self, float invec, float outvec)

        throw (
        AUExcept) C-style Simulation Algorithm Interface, for single step
        simulation See:  class SimBase Todo see if we can do this in python
        without this additional method

        Parameters:
        -----------

        inmtx:  input vector, size = inputs

        outmtx:  output vector, size = outputs

        Data must be already allocated! 
        """
        return _aureservoir.SingleESN_simulateStep(*args)

    def setBPCutoff(*args):
        """
        setBPCutoff(self, float f1vec, float f2vec)

        throw (
        AUExcept) Set lowpass/highpass cutoff frequencies for bandpass style
        neurons " (C-style Interface).

        Parameters:
        -----------

        f1:  vector with lowpass cutoff for all neurons (size = neurons)

        f2:  vector with highpass cutoffs (size = neurons) 
        """
        return _aureservoir.SingleESN_setBPCutoff(*args)

    def setIIRCoeff(*args):
        """setIIRCoeff(self, float bmtx, float amtx)"""
        return _aureservoir.SingleESN_setIIRCoeff(*args)

    def post(*args):
        """
        post(self)

        posts current parameters to stdoutTodo maybe return a outputstream (if
        stdout is not useful) or just use the << operator ? 
        """
        return _aureservoir.SingleESN_post(*args)

    def getSize(*args):
        """
        getSize(self) -> int

        reservoir size (nr of neurons) 
        """
        return _aureservoir.SingleESN_getSize(*args)

    def getInputs(*args):
        """
        getInputs(self) -> int

        nr of inputs to the reservoir 
        """
        return _aureservoir.SingleESN_getInputs(*args)

    def getOutputs(*args):
        """
        getOutputs(self) -> int

        nr of outputs from the reservoir 
        """
        return _aureservoir.SingleESN_getOutputs(*args)

    def getNoise(*args):
        """
        getNoise(self) -> double

        current noise level 
        """
        return _aureservoir.SingleESN_getNoise(*args)

    def getInitParam(*args):
        """
        getInitParam(self, InitParameter key) -> float

        returns an initialization parametern from the parameter map

        Parameters:
        -----------

        key:  the requested parameter

        the value of the parameter 
        """
        return _aureservoir.SingleESN_getInitParam(*args)

    def getInitAlgorithm(*args):
        """
        getInitAlgorithm(self) -> int

        initialization algorithm 
        """
        return _aureservoir.SingleESN_getInitAlgorithm(*args)

    def getTrainAlgorithm(*args):
        """
        getTrainAlgorithm(self) -> int

        training algorithm 
        """
        return _aureservoir.SingleESN_getTrainAlgorithm(*args)

    def getSimAlgorithm(*args):
        """
        getSimAlgorithm(self) -> int

        simulation algorithm 
        """
        return _aureservoir.SingleESN_getSimAlgorithm(*args)

    def getReservoirAct(*args):
        """
        getReservoirAct(self) -> int

        reservoir activation function 
        """
        return _aureservoir.SingleESN_getReservoirAct(*args)

    def getOutputAct(*args):
        """
        getOutputAct(self) -> int

        output activation function 
        """
        return _aureservoir.SingleESN_getOutputAct(*args)

    def getWin(*args):
        """
        getWin(self, float mtx)

        get pointer to input weight matrix data and dimensions WARNING:  This
        data is in fortran style column major storage ! 
        """
        return _aureservoir.SingleESN_getWin(*args)

    def getWback(*args):
        """
        getWback(self, float mtx)

        get pointer to feedback weight matrix data and dimensions WARNING:
        This data is in fortran style column major storage ! 
        """
        return _aureservoir.SingleESN_getWback(*args)

    def getWout(*args):
        """
        getWout(self, float mtx)

        get pointer to output weight matrix data and dimensions WARNING:  This
        data is in fortran style column major storage ! 
        """
        return _aureservoir.SingleESN_getWout(*args)

    def getX(*args):
        """
        getX(self, float vec)

        get pointer to internal state vector x data and length 
        """
        return _aureservoir.SingleESN_getX(*args)

    def getW(*args):
        """
        getW(self, float wmtx)

        throw ( AUExcept)
        Copies data of the sparse reservoir weight matrix into a dense C-style
        matrix. Memory of the C array must be allocated before!

        Parameters:
        -----------

        wmtx:  pointer to matrix of size (neurons_ x neurons_)

        Todo check if this can be avoided 
        """
        return _aureservoir.SingleESN_getW(*args)

    def setInitAlgorithm(*args):
        """
        setInitAlgorithm(self, InitAlgorithm alg=INIT_STD)
        setInitAlgorithm(self)

        throw (
        AUExcept) set initialization algorithm 
        """
        return _aureservoir.SingleESN_setInitAlgorithm(*args)

    def setTrainAlgorithm(*args):
        """
        setTrainAlgorithm(self, TrainAlgorithm alg=TRAIN_LEASTSQUARE)
        setTrainAlgorithm(self)

        throw (
        AUExcept) set training algorithm 
        """
        return _aureservoir.SingleESN_setTrainAlgorithm(*args)

    def setSimAlgorithm(*args):
        """
        setSimAlgorithm(self, SimAlgorithm alg=SIM_STD)
        setSimAlgorithm(self)

        throw (
        AUExcept) set simulation algorithm 
        """
        return _aureservoir.SingleESN_setSimAlgorithm(*args)

    def setSize(*args):
        """
        setSize(self, int neurons=10)
        setSize(self)

        throw ( AUExcept)
        set reservoir size (nr of neurons) 
        """
        return _aureservoir.SingleESN_setSize(*args)

    def setInputs(*args):
        """
        setInputs(self, int inputs=1)
        setInputs(self)

        throw (
        AUExcept) set nr of inputs to the reservoir 
        """
        return _aureservoir.SingleESN_setInputs(*args)

    def setOutputs(*args):
        """
        setOutputs(self, int outputs=1)
        setOutputs(self)

        throw (
        AUExcept) set nr of outputs from the reservoir 
        """
        return _aureservoir.SingleESN_setOutputs(*args)

    def setNoise(*args):
        """
        setNoise(self, double noise)

        throw ( AUExcept)
        set noise level for training/simulation algorithm

        Parameters:
        -----------

        noise:  with uniform distribution within [-noise|+noise] 
        """
        return _aureservoir.SingleESN_setNoise(*args)

    def setInitParam(*args):
        """
        setInitParam(self, InitParameter key, float value)

        set initialization parameter 
        """
        return _aureservoir.SingleESN_setInitParam(*args)

    def setReservoirAct(*args):
        """
        setReservoirAct(self, ActivationFunction f=ACT_TANH)
        setReservoirAct(self)

        throw (
        AUExcept) set reservoir activation function 
        """
        return _aureservoir.SingleESN_setReservoirAct(*args)

    def setOutputAct(*args):
        """
        setOutputAct(self, ActivationFunction f=ACT_LINEAR)
        setOutputAct(self)

        throw (
        AUExcept) set output activation function 
        """
        return _aureservoir.SingleESN_setOutputAct(*args)

    def setWin(*args):
        """
        setWin(self, float inmtx)

        throw ( AUExcept)
        set input weight matrix C-style interface (data will be copied into a
        FLENS matrix)

        Parameters:
        -----------

        inmtx:  pointer to win matrix in row major storage 
        """
        return _aureservoir.SingleESN_setWin(*args)

    def setW(*args):
        """
        setW(self, float inmtx)

        throw ( AUExcept) set
        reservoir weight matrix C-style interface (data will be copied into a
        FLENS matrix)

        Parameters:
        -----------

        inmtx:  pointer to a dense reservoir matrix in row major storage 
        """
        return _aureservoir.SingleESN_setW(*args)

    def setWback(*args):
        """
        setWback(self, float inmtx)

        throw ( AUExcept)
        set feedback weight matrix C-style interface (data will be copied into
        a FLENS matrix)

        Parameters:
        -----------

        inmtx:  pointer to wback matrix in row major storage 
        """
        return _aureservoir.SingleESN_setWback(*args)

    def setWout(*args):
        """
        setWout(self, float inmtx)

        throw ( AUExcept)
        set output weight matrix C-style interface (data will be copied into a
        FLENS matrix)

        Parameters:
        -----------

        inmtx:  pointer to wout matrix in row major storage 
        """
        return _aureservoir.SingleESN_setWout(*args)

    def setX(*args):
        """
        setX(self, float invec)

        throw ( AUExcept) set
        internal state vector C-style interface (data will be copied into a
        FLENS matrix)

        Parameters:
        -----------

        invec:  pointer to state vector 
        """
        return _aureservoir.SingleESN_setX(*args)

SingleESN_swigregister = _aureservoir.SingleESN_swigregister
SingleESN_swigregister(SingleESN)

CONNECTIVITY = _aureservoir.CONNECTIVITY
ALPHA = _aureservoir.ALPHA
IN_CONNECTIVITY = _aureservoir.IN_CONNECTIVITY
IN_SCALE = _aureservoir.IN_SCALE
IN_SHIFT = _aureservoir.IN_SHIFT
FB_CONNECTIVITY = _aureservoir.FB_CONNECTIVITY
FB_SCALE = _aureservoir.FB_SCALE
FB_SHIFT = _aureservoir.FB_SHIFT
LEAKING_RATE = _aureservoir.LEAKING_RATE
TIKHONOV_FACTOR = _aureservoir.TIKHONOV_FACTOR
IP_LEARNRATE = _aureservoir.IP_LEARNRATE
IP_MEAN = _aureservoir.IP_MEAN
IP_VAR = _aureservoir.IP_VAR
INIT_STD = _aureservoir.INIT_STD
SIM_STD = _aureservoir.SIM_STD
SIM_SQUARE = _aureservoir.SIM_SQUARE
SIM_LI = _aureservoir.SIM_LI
SIM_BP = _aureservoir.SIM_BP
SIM_FILTER = _aureservoir.SIM_FILTER
SIM_FILTER2 = _aureservoir.SIM_FILTER2
TRAIN_PI = _aureservoir.TRAIN_PI
TRAIN_LS = _aureservoir.TRAIN_LS
TRAIN_RIDGEREG = _aureservoir.TRAIN_RIDGEREG
TRAIN_PI_SQUARE = _aureservoir.TRAIN_PI_SQUARE
ACT_LINEAR = _aureservoir.ACT_LINEAR
ACT_TANH = _aureservoir.ACT_TANH
ACT_TANH2 = _aureservoir.ACT_TANH2
ACT_SIGMOID = _aureservoir.ACT_SIGMOID


