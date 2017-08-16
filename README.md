[![Travis status](https://img.shields.io/travis/better/irr/master.svg?style=flat)](https://travis-ci.org/better/irr)

This repo contains a custom implementation of `numpy.irr` built from scratch. It is used to compute the [internal rate of return](https://en.wikipedia.org/wiki/Internal_rate_of_return), also called APR, which is useful in a wide range of financial circumstances.

What's wrong with `numpy.irr`? It's extremely slow and usually returns `nan`.

There are two implementations available in this package. `irr.irr` defaults to `irr.irr_binary_search` which is slower but more stable. There is also `irr.irr_newton` which is much faster but sometimes doesn't converge.

Binary Search
-------------

![binary search](https://raw.githubusercontent.com/better/irr/master/binary_search.gif)

Newton's method
-------------

![newton](https://raw.githubusercontent.com/better/irr/master/newton.gif)

Misc
----

This repo uses the [MIT License](https://github.com/better/irr/blob/master/LICENSE)
