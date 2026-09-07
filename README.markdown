Browse : [Lua](https://github.com/michel-leonard/ciede2000-lua) · [MATLAB](https://github.com/michel-leonard/ciede2000-matlab) · [Microsoft Excel](https://github.com/michel-leonard/ciede2000-excel) · [PHP](https://github.com/michel-leonard/ciede2000-php) · [Perl](https://github.com/michel-leonard/ciede2000-perl) · **Python** · [R](https://github.com/michel-leonard/ciede2000-r) · [Ruby](https://github.com/michel-leonard/ciede2000-ruby) · [Rust](https://github.com/michel-leonard/ciede2000-rust) · [SQL](https://github.com/michel-leonard/ciede2000-sql) · [Swift](https://github.com/michel-leonard/ciede2000-swift)

# CIEDE2000 color difference formula in Python

This page presents the CIEDE2000 color difference, implemented in the Python programming language.

![Logo](https://raw.githubusercontent.com/michel-leonard/ciede2000-color-matching/refs/heads/main/docs/assets/images/logo.jpg)

## About

Here you’ll find the first rigorously correct implementation of CIEDE2000 that doesn’t use any conversion between degrees and radians. Set parameter `canonical` to obtain results in line with your existing pipeline.

`canonical`|The algorithm operates...|
|:--:|-|
`False`|in accordance with the CIEDE2000 values currently used by many industry players|
`True`|in accordance with the CIEDE2000 values provided by [this](https://hajim.rochester.edu/ece/sites/gsharma/ciede2000/) academic MATLAB function|

## Our CIEDE2000 offer

These 2 production-ready files, released in 2026, contain the CIEDE2000 algorithm.

Source File|Type|Bits|Purpose|Advantage|
|:--:|:--:|:--:|:--:|:--:|
[ciede2000.py](./ciede2000.py)|`float`|64|Scientific|Interoperability|

This implementation is designed for those who only work with vectors.

Source File|Type|Bits|Purpose|Advantage|
|:--:|:--:|:--:|:--:|:--:|
[ciede2000-numpy.py](./ciede2000-numpy.py)|`float32`|32|General|Lightness, Speed|
[ciede2000-numpy.py](./ciede2000-numpy.py)|`float64`|64|Scientific|Interoperability|
[ciede2000-numpy.py](./ciede2000-numpy.py)|`float96`|96|Metrology|Higher Precision|

`ciede2000` has a light memory cost, allocating no more than 9 temporary vectors at any one time.

### Software Versions

- Python 2
- Python 3

### Example Usage

We calculate the CIEDE2000 distance between two colors, first without and then with parametric factors.

```python
# Example of two L*a*b* colors
l1, a1, b1 = 98.8, 71.4, 6.4
l2, a2, b2 = 93.9, 43.4, -3.3

delta_e = ciede2000(l1, a1, b1, l2, a2, b2)
print(delta_e) # CIEDE2000 = 9.407476583096802

# Example of parametric factors used in the textile industry
kl, kc, kh = 2.0, 1.0, 1.0

# Perform a CIEDE2000 calculation compliant with that of Gaurav Sharma
canonical = True

delta_e = ciede2000(l1, a1, b1, l2, a2, b2, kl, kc, kh, canonical)
print(delta_e) # CIEDE2000 = 9.067053686706924
```

**Note**: this example uses scalars, but if you prefer, it would have worked just as well with numpy vectors.

### Test Results

LEONARD’s tests are based on well-chosen L\*a\*b\* colors, with various parametric factors `kL`, `kC` and `kH`.

<details>
<summary>Display test results for ciede2000.py</summary>

```
CIEDE2000 Verification Summary :
          Compliance : [ ] CANONICAL [X] SIMPLIFIED
  First Checked Line : 20.0,0.05,-30.0,30.0,0.0,128.0,1.0,1.0,1.0,53.41746217641311
           Precision : 11 decimal digits
           Successes : 100000000
               Error : 0
            Duration : 643.57 seconds
     Average Delta E : 67.13
   Average Deviation : 4.8e-15
   Maximum Deviation : 1.4e-13
```

```
CIEDE2000 Verification Summary :
          Compliance : [X] CANONICAL [ ] SIMPLIFIED
  First Checked Line : 20.0,0.05,-30.0,30.0,0.0,128.0,1.0,1.0,1.0,53.41765416511742
           Precision : 11 decimal digits
           Successes : 100000000
               Error : 0
            Duration : 641.72 seconds
     Average Delta E : 67.13
   Average Deviation : 5.2e-15
   Maximum Deviation : 1.4e-13
```

</details>


<details>
<summary>Display test results for ciede2000-numpy.py</summary>

```
 CIEDE2000 Verification Summary :
          Compliance : [ ] CANONICAL [X] SIMPLIFIED
  First Checked Line : 60.0,-0.0,32.0,68.0,0.00008,-127.9995,1.0,1.0,1.0,54.15960745600093
           Precision : 11 decimal digits
           Successes : 100000000
               Error : 0
            Duration : 485.06 seconds
     Average Delta E : 67.13
   Average Deviation : 6.6e-15
   Maximum Deviation : 3.1e-13
```

```
CIEDE2000 Verification Summary :
          Compliance : [X] CANONICAL [ ] SIMPLIFIED
  First Checked Line : 60.0,-0.0,32.0,68.0,0.00008,-127.9995,1.0,1.0,1.0,54.15941680953167
           Precision : 11 decimal digits
           Successes : 100000000
               Error : 0
            Duration : 485.90 seconds
     Average Delta E : 67.13
   Average Deviation : 6.9e-15
   Maximum Deviation : 3.1e-13
```

</details>

## Public Domain Licence

You are free to use these files, even for commercial purposes.
