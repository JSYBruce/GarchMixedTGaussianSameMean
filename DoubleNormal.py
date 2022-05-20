# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from customtyping import Float64Array, Int32Array, ArrayLike, ArrayLike1D, Float64Array
from typing import Callable, List, Optional, Sequence, Tuple, Union
from scipy.special import gamma
from numpy import (
    abs,
    array,
    asarray,
    empty,
    exp,
    int64,
    integer,
    isscalar,
    log,
    nan,
    ndarray,
    ones_like,
    pi,
    sign,
    sqrt,
    sum,
)

import scipy.stats as stats

class DoubleNormal():
    """
    t + normal distribution for use with ARCH models

    Parameters
    ----------
    """

    def __init__(
        self) -> None:
        self._name = "T+Normal+Alpha+Mean"
        self.name = "T+Normal+Alpha+Mean"
    def constraints(self) -> Tuple[Float64Array, Float64Array]:
        return empty(0), empty(0)

    def bounds(self, resids: Float64Array) -> List[Tuple[float, float]]:
        return []

    def loglikelihood(
        self,
        parameters: Union[Sequence[float], ArrayLike1D],
        resids: ArrayLike,
        sigma1: ArrayLike,
        sigma2: ArrayLike,
        weight: Float64Array,
        individual: bool = False,
    ) -> Union[float, Float64Array]:
        r"""Computes the log-likelihood of assuming residuals are normally
        distributed, conditional on the variance

        Parameters
        ----------
        parameters : ndarray
            The normal likelihood has no shape parameters. Empty since the
            standard normal has no shape parameters.
        resids  : ndarray
            The residuals to use in the log-likelihood calculation
        sigma2 : ndarray
            Conditional variances of resids
        individual : bool, optional
            Flag indicating whether to return the vector of individual log
            likelihoods (True) or the sum (False)

        Returns
        -------
        ll : float
            The log-likelihood

        Notes
        -----
        The log-likelihood of a single data point x is

        .. math::

            \ln f\left(x\right)=-\frac{1}{2}\left(\ln2\pi+\ln\sigma^{2}
            +\frac{x^{2}}{\sigma^{2}}\right)

        """
        nu = parameters[1]
        sigma1 = sigma1 * (nu - 2)
        px = gamma((nu + 1) / 2) / (sigma1* pi )**0.5 / (gamma(nu / 2)) / (1 + (resids)**2/sigma1)**(0.5*(nu+1))
        lls = log( weight * px + (1-weight)/sqrt(2*pi*sigma2)*exp(-0.5*(resids)**2 /sigma2) )
        
        if individual:
            return lls
        else:
            return sum(lls)

    def starting_values(self, std_resid: Float64Array) -> Float64Array:
        return empty(0)
    
    
    def cdf(
        self,
        weight: Float64Array,
        resids: Union[Sequence[float], ArrayLike1D],
        parameters: Union[None, Sequence[float], ArrayLike1D] = None,
    ) -> Float64Array:
        nu = parameters
        var = nu / (nu - 2)
        return weight * stats.norm.cdf(asarray(resids)) + (1 - weight) * stats.t(nu, scale=1.0 / sqrt(var)).cdf(asarray(resids)) 
    