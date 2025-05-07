API Documentation
=============

This page documents the public API provided by the `naive_kyber` package.

.. note::

   This package is intended for educational use only and is **not** suitable for production cryptographic systems.

Module: ``naive_kyber.functions``
----------------------------------

.. automodule:: naive_kyber.functions
    :members:
    :undoc-members:
    :show-inheritance:


Public Functions
----------------

.. autofunction:: naive_kyber.keygen

.. autofunction:: naive_kyber.encrypt

.. autofunction:: naive_kyber.decrypt


Data Structures and Internal Modules
------------------------------------

These modules contain the implementation details for Kyber KEM functionality.
They're useful for digging into the mechanics of the algorithm.

.. toctree::
   :maxdepth: 1

   naive_kyber.parameters
   naive_kyber.poly
   naive_kyber.matrix
   naive_kyber.cbd
   naive_kyber.serialize
   naive_kyber.pke
