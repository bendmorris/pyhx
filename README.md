**pyhx** is a simple import hook for importing Haxe directly into Python! Once 
installed, you can directly `import` Haxe source files in your Python code. If 
the Haxe file has been modified more recently than its compiled Python version, 
it will be recompiled.

## Setup

To install pyhx, run `python setup.py install`.

Using pyhx requires Haxe to be installed. It will work out of the box if the 
haxe binary is on your executable path; otherwise, pass the path to haxe as an 
argument to `pyhx.install()`.

## Usage

`PyHxTest.hx`

```haxe
class PyHxTest {
    public static function main() {
        trace("HELLO FROM HAXE!");
    }
}
```

`test.py`

```python
import pyhx
pyhx.install()

from PyHxTest import PyHxTest
PyHxTest.main()
```
