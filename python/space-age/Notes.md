`setattr` can be used to add methods to a python class.

```python
 def __init__(self, seconds):
        self.seconds = seconds
        for planet, ratio in self.PLANET_RATIOS:
            setattr(self, 'on_' + planet, self._planet_years(ratio))

    def _planet_years(self, ratio):
        return lambda ratio=ratio: round(self.seconds / ratio, 2)
```


