import math, numpy

MAX_LOG_RATE = 1e3
BASE_TOL = 1e-12

def irr_binary_search(stream, tol=BASE_TOL):
    rate_lo, rate_hi = -MAX_LOG_RATE, +MAX_LOG_RATE
    sgn = numpy.sign(stream[0]) # f(x) is decreasing
    for steps in range(100):
        rate = (rate_lo + rate_hi)/2
        r = numpy.arange(len(stream))
        # Factor exp(m) out because it doesn't affect the sign
        m = max(-rate * r)
        f = numpy.exp(-rate * r - m)
        t = numpy.dot(f, stream)
        if abs(t) < tol * math.exp(-m):
            break
        if t * sgn > 0:
            rate_hi = rate
        else:
            rate_lo = rate
    rate = (rate_lo + rate_hi) / 2
    return math.exp(rate) - 1


def irr_newton(stream, tol=BASE_TOL):
    rate = 0.0
    for steps in range(50):
        r = numpy.arange(len(stream))
        # Factor exp(m) out of the numerator & denominator for numerical stability
        m = max(-rate * r)
        f = numpy.exp(-rate * r - m)
        t = numpy.dot(f, stream)
        if abs(t) < tol * math.exp(-m):
            break
        u = numpy.dot(f * r, stream)
        # Clip the update to avoid jumping into some numerically unstable place
        rate = rate + numpy.clip(t / u, -1.0, 1.0)

    return math.exp(rate) - 1


irr = irr_binary_search
