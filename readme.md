# PC/SC Wrapper for Python 
PCSCReader class provides an interface to communicate with PC/SC smart card readers.

This class handles connection management, card activation, and APDU exchange with smart cards
through PC/SC compatible readers. It supports reader selection by name or interactive selection,
and provides colored console output for debugging APDU communication.

High Level PC/SC Reader Methods:
    - connect(pcsc_reader_name): Establishes connection to a PC/SC reader by name or interactive selection
    - activateCard(): Activates the smart card and displays its ATR
    - disconnect(): Disconnects from the reader and releases resources
    - Exchange(cmdApdu, expectedSW1SW2, description): Sends command APDU and receives response APDU 


## Use case examples
Note: The use case examples are used for education purposes only. 


## Installation
Remark: Tested with Python version 3.13.3
```
pip install -r requirements.txt
```

**Recommendation**: Use Python Virtual Environment (venv)
- See https://www.geeksforgeeks.org/python/creating-python-virtual-environment-windows-linux/ 


## Alternative Installation
- ```pip install colorama``` (pip3 install colorama or python -m pip install colorama)
- ```pip install pyscard``` 
- ```pip install cryptography```
- ```pip install ndeflib```