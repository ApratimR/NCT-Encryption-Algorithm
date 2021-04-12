# NECTA (No Cipher Text Encryption Algorithm)

A **EXPERIMENTAL** symmetric encryption algorithm which instead of generating cipher/encrypted text generates the instruction to recreate the main Data.

### BUT WHY make such a thing???

* common block cipher symmetric encryption algos use either:
	* Feistel cipher structure
	* OR SP(Substitution & Permutation) Network Structure
* so I thought of using some unconventional method to encrypt data
* and as for why do such a thing ??? rather than using conventional methods
* i love to do cryptography related stuff with twists

### Some Notes
* it uses one of my own Hash algo [FNNH] based on Neural network structures
* it is heavy of instruction cycles so it will take too much time if the `stress` parameter set high

### Requirements

* make sure you have `NUMPY` (Thise was made on version `1.19.2`)
* make sure you have the `FNNH` (run the command `pip install FNNH` to install)


### HOW TO USE

```python
from NCTEA import NECTA

key = "test"
data = "qwerty"

data = NECTA(data,key)
print(data)
#AbFHFtLM

data = NECTA(data,key,mode=2)
print(data)
#qwerty
```
