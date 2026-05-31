#
#  Copyright (c) 2026, Gerhard H. Schalk
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
from enum import Enum
from py_pcsc_reader.cmd_apdu import *
from py_pcsc_reader.resp_apdu import *
from py_pcsc_reader.pcsc_reader import *


if __name__ == '__main__':
    try:
        reader = PCSCReader()
        reader.connect()
        reader.activateCard()
        
        # Select Master File
        reader.Exchange('00 A4 00 0C 02 3F 00',
            description='Select Master File ...',
            expectedSW1SW2=0x9000
        )

        # Select eCard Application
        reader.Exchange('00 A4 04 0C 08 D0 40 00 00 17 01 01 01',
            description='Select eCard Application ...',
            expectedSW1SW2=0x9000
        )

        # Read Binary
        readBinary = CmdApdu()
        readBinary.CLA = 0x00
        readBinary.INS = 0xB0
        readBinary.P1 = 0x81 
        readBinary.P2 = 0x00
        readBinary.Le = 0x00

        reader.Exchange(readBinary,
                      description='Read File SFID = 0x01 ...',
                      expectedSW1SW2=0x9000
        )

        #ToDo: Read File SFID = 0x02


        reader.disconnect()


    except Exception as e:
        print(COLOR.RED.value + f'Exception: {e}')