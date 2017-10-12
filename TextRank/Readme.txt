

Datasets:

This dataset is found in:
https://github.com/snkim/AutomaticKeyphraseExtraction
"i have used the 'Hulth' datasets  "

main.py 
This file will be acting as an running interface , simply to separate the code from the running code

Textrank.py

this will have the text rank implementation
#in this you can see two graphs being implemented
graph_building1()-- simply the word co -occurence based graph
graph_building2()-- from david mojors implementation(https://github.com/davidadamojr/TextRank)

Testingfile.py
This will run across all the documents and will generate a comaprative keywords list and the metrics

Metric used:

Precision: C(correct)/C(extract)
Recall: C(correct)/C(standard)
F_Measure:2*Precision*Recall/(Precision+Recall)


Files generated:

You will have 2 outputfiles being generated as 
'phrase1.json'== co-occurence based graph building
'phrase2.json'== levenshiet distance based graph building

Manual Comparison:

The outputs can be compared with the author give outputs, which are available with ease,but i have provided it as 2 json files(user_uncontroled.json,user_controled.json) here controlled means a striped version of the outputs as in datasets.
