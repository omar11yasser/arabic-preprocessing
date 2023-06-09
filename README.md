# Arabic text preprocessing 
In this repo I will try to implement various preprocessing technique on arabic text.
please note that it's still a work in progress.

## Removing arabic prepositions
In the first phase **remove_propositions_from_sentences()** was implemented it use two function to remove sufixes like 'هن' and 'هم' and prefixes like 'ب' and others.
This function take a sentence and return processed sentence. It is advised to use it as .apply(remove_propositions_from_sentences) on a pandas series.

There is two functions that remove_propositions_from_sentences act as an interface to **hun_hum_sufix_removal()** and **remove_prefixe_wsufixes()** both take a word and return a preprocessed word.
You can use both thos functions seperately but not if both will be used it is advised to use **hun_hum_sufix_removal()** first.

This fuction follow the work in Conditional Arabic Light Stemmer: Condlight. https://iajit.org/PDF/Special%20Issue%202018,%20No.%203A/17411.pdf

Please share all your comments and feedback as it will be valuable for me and this work.
