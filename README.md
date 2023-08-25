## Raw SRAM Memory Content Collection Module

This module is dedicated to collecting raw SRAM memory content on Arduino Uno.

### Possible workflow of this module can be described as follows:
1. Burn the bootloader on the Arduino Uno board:
*  This can be done by using another board as a parallel programmer [more details](https://support.arduino.cc/hc/en-us/articles/4841602539164-Burn-the-bootloader-on-UNO-Mega-and-classic-Nano-using-another-Arduino#ide). We are using Funduino Mega board (having same configurations as Arduino Mega) as a parallel programmer.
*  Perform necessary connections between Funduino Mega as a programming board and Arduino Mega as a target board (more about pin connection details in the above link). Pictorial illustration below <img src="boards-connection.png" alt="boards-connection" width="600"/>
*  Follow the sequence mentioned in the above document to upload the ISP sketch on Funduino Mega and burn the bootloader on Arduino Uno.

2. Upload response collection sketch:
* Uploading the sketch on Arduino Uno using Funduino Mega as an ISP [more details](https://www.makerguides.com/what-does-burn-bootloader-do-in-arduino-ide/#:~:text=Is%20it%20necessary%20to%20use,code%20using%20an%20external%20programmer).

3. Generate responses:
* Once the sketch is uploaded on Arduino Uno and connect it to a serial output to visualize the memory content.
* This can be done by connecting Arduino Uno to a computer via a PuTTY client configured in a serial output format with the baud rate same as mentioned in the sketch.
* Once the board is connected to a computer, memory contents can be seen in a PuTTY serial output without the need for an additional IDE.

4. Hamming Distance calculation:
* After generating a couple of responses, you may want to calculate the Intra Hamming Distance (HD) between the two responses. This can be done  by the HD calculator submodule, which takes two response files and calculates the HD between the two responses.
* Furthermore, calculating the Intra HD between multiple responses is automated via another submodule, uploaded in the repo. It will take the folder name containing all the responses and the initial response file name to compare it with all other responses. Results of the hamming distance would be saved in a CSV file.
* Plotting a graph of Intra HD can be done from that CSV, which is present in another submodule, uploaded in the repository.
