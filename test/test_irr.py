import unittest, random, math, numpy, time, functools
import irr

class _Base(unittest.TestCase):
    def test(self):
        for test in range(1000):
            d, r = self.case()
            self.assertAlmostEqual(irr.irr(d), r)


class SimpleBondTest(_Base):
    def case(self):
        r = math.exp(random.gauss(0, 1)) - 1
        x = random.gauss(0, 1)
        d = [x / (1 + r), -x]
        return d, r


class SlightlyLongerBondTest(_Base):
    def case(self, n=10):
        r = math.exp(random.gauss(0, 1)) - 1
        x = random.gauss(0, 1)
        d = [x] + [0.0] * (n-2) + [-x * (1+r)**(n-1)]
        return d, r


class MoreNonzeroTest(_Base):
    def case(self, n=10):
        r = math.exp(random.gauss(0, 1)) - 1
        d = [random.random() for i in range(n-1)]
        d.append(-sum([x * (1+r)**(n-i-1) for i, x in enumerate(d)]))
        return d, r


class PerformanceTest(unittest.TestCase):
    def test(self):
        us_times = []
        np_times = []
        ns = [10, 20, 50, 100]
        for n in ns:
            k = 100
            sums = [0.0, 0.0]
            for j in range(k):
                r = math.exp(random.gauss(0, 1.0 / n)) - 1
                x = random.gauss(0, 1)
                d = [x] + [0.0] * (n-2) + [-x * (1+r)**(n-1)]

                results = []
                for i, f in enumerate([irr.irr, numpy.irr]):
                    t0 = time.time()
                    results.append(f(d))
                    sums[i] += time.time() - t0

                if not numpy.isnan(results[1]):
                    self.assertAlmostEqual(results[0], results[1])
            for times, sum in zip([us_times, np_times], sums):
                times.append(sum/k)

        try:
            from matplotlib import pyplot
            import seaborn
        except ImportError:
            return

        pyplot.plot(ns, us_times, label='Our library')
        pyplot.plot(ns, np_times, label='Numpy')
        pyplot.xlabel('n')
        pyplot.ylabel('time(s)')
        pyplot.yscale('log')
        pyplot.savefig('plot.png')


