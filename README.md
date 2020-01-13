# Stock_Correlation

System which is finding correlation between stock market and news headlines.

Main part of this project is sentiment classifier created with GRU neural network.

GRU can be considered as a variation of the LSTM and improved simple recurrent neural network.

This architecture uses update gate and reset gate.

Basically, these are two vectors which decide what information should be passed to the output.

![GRU cell](https://user-images.githubusercontent.com/29351335/72227862-87a58580-35a1-11ea-876d-ce8b1070ade1.png)

To run project i suggest downloading pretrained weights available here: https://drive.google.com/drive/folders/1vH7o5Za-7tl2oABI7odvnOrzJEG5QlJd?usp=sharing

Next you have to download headlines which sentiment will be classified. 

Examples can be found in repository but script api.py downloads new ones (to run script you have to have account on newsapi.org).

Final step is running notebook which contains last part of project.
