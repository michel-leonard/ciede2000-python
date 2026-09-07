# This function written in Python is not affiliated with the CIE (International Commission on Illumination),
# and is released into the public domain. It is provided "as is" without any warranty, express or implied.

# The classic CIEDE2000 implementation, which operates on two L*a*b* colors, and returns their difference.
# "l" ranges from 0 to 100, while "a" and "b" are unbounded and commonly clamped to the range of -128 to 127.
def ciede2000(l1, a1, b1, l2, a2, b2, kl = 1.0, kc = 1.0, kh = 1.0, canonical = False) :
	from math import pi, sqrt, atan2, sin, exp
	# Working in Python with the CIEDE2000 color-difference formula.
	# kl, kc, kh are parametric factors to be adjusted according to
	# different viewing parameters such as textures, backgrounds...
	n = (sqrt(a1 * a1 + b1 * b1) + sqrt(a2 * a2 + b2 * b2)) * 0.5
	n = n * n * n * n * n * n * n
	# A factor involving chroma raised to the power of 7 designed to make
	# the influence of chroma on the total color difference more accurate.
	n = 1.0 + 0.5 * (1.0 - sqrt(n / (n + 6103515625.0)))
	# Application of the chroma correction factor.
	c1 = sqrt(a1 * a1 * n * n + b1 * b1)
	c2 = sqrt(a2 * a2 * n * n + b2 * b2)
	# atan2 is preferred over atan because it accurately computes the angle of
	# a point (x, y) in all quadrants, handling the signs of both coordinates.
	h1 = atan2(b1, a1 * n)
	h2 = atan2(b2, a2 * n)
	h1 += 2.0 * pi * (h1 < 0.0)
	h2 += 2.0 * pi * (h2 < 0.0)
	# When the hue angles lie in different quadrants, the straightforward
	# average can produce a mean that incorrectly suggests a hue angle in
	# the wrong quadrant, the next lines handle this issue.
	h_mean = (h1 + h2) * 0.5
	h_delta = (h2 - h1) * 0.5
	if pi + 1E-14 < abs(h2 - h1) :
		h_delta += pi
		if canonical and pi + 1E-14 < h_mean :
			# Sharma's implementation, OpenJDK, ...
			h_mean -= pi
		else :
			# Lindbloom's implementation, Netflix's VMAF, ...
			h_mean += pi
	p = 36.0 * h_mean - 55.0 * pi
	n = (c1 + c2) * 0.5
	n = n * n * n * n * n * n * n
	# The hue rotation correction term is designed to account for the
	# non-linear behavior of hue differences in the blue region.
	r_t = -2.0 * sqrt(n / (n + 6103515625.0)) \
			* sin(pi / 3.0 * exp(p * p / (-25.0 * pi * pi)))
	n = (l1 + l2) * 0.5
	n = (n - 50.0) * (n - 50.0)
	# Lightness.
	l = (l2 - l1) / (kl * (1.0 + 0.015 * n / sqrt(20.0 + n)))
	# These coefficients adjust the impact of different harmonic
	# components on the hue difference calculation.
	t = 1.0	+ 0.24 * sin(2.0 * h_mean + pi * 0.5) \
		+ 0.32 * sin(3.0 * h_mean + 8.0 * pi / 15.0) \
		- 0.17 * sin(h_mean + pi / 3.0) \
		- 0.20 * sin(4.0 * h_mean + 3.0 * pi / 20.0)
	n = c1 + c2
	# Hue.
	h = 2.0 * sqrt(c1 * c2) * sin(h_delta) / (kh * (1.0 + 0.0075 * n * t))
	# Chroma.
	c = (c2 - c1) / (kc * (1.0 + 0.0225 * n))
	# The result accurately reflects the geometric distance in the color space.
	return sqrt(l * l + h * h + c * c + c * h * r_t) # Given a tolerance of 3.1e-13

# If you remove the constant 1E-14, the code will continue to work, but CIEDE2000
# interoperability between all programming languages will no longer be guaranteed.

# Source code tested by Michel LEONARD
# Website: ciede2000.pages-perso.free.fr
