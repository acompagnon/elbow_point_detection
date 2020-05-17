# Elbow point detection

Function to detect elbow point in a curve.

elbow_point_detection.elbow_point_detector.detect_elbow

**detect_elbow(x, y)**

Parameters:
- x (list): x axis values.
- y (list): y axis values.

Returns:
- elbow_x: elbow point x axis value.
- elbow_y: elbow point y axis value.

```
>>> from elbow_point_detector import detect_elbow
>>> y =  [1018.3610201975621, 1013.313401149943, 997.0671389216888, 991.6623770169268, 645.2962023269747, 645.8890594698319, 504.17464327096684, 454.8791230308529]
>>> x = list(range(len(y)))
>>> detect_elbow(x, y)
(4, 645.2962023269747)
```

# Source

Finding a “Kneedle” in a Haystack:
Detecting Knee Points in System Behavior
Ville Satopaa†,Jeannie Albrecht†, David Irwin‡, and Barath Raghavan§
https://raghavan.usc.edu/papers/kneedle-simplex11.pdf
