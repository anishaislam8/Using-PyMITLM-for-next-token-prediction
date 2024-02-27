import pymitlm

w = 5
padding = w * 2

lines = ["r hsl",
"inlet random outlet",
"inlet route moses msg zexy/multiplex~ outlet~",
"inlet~ canvas throw~",
"osc~ *~ dac~",
"floatatom t msg",
"floatatom floatatom pack send msg cnv",
"t msg list_prepend l2s list send",
"tgl tgl vsl cnv cnv catch~"]

# model fails to predict ranking for 
# "inlet route moses msg zexy/multiplex~ outlet~" and "floatatom floatatom pack send msg cnv"

m = pymitlm.PyMitlm("testcorpus_subset", 4, "ModKN", True)
line = lines[3]
line = "<s> " * padding + line
print("Line: ", line)
sentence_tokens = line.split(" ")
print("Sentence tokens: ", sentence_tokens)

context = ' '.join(sentence_tokens[:-1])  # Use all words except the last one as context
length_of_context = len(sentence_tokens) - 1

true_next_word = sentence_tokens[-1]

highest_ranking = m.predict(context).split("\n")[0]
print("Highest ranking: ", highest_ranking)

predicted_next_word = highest_ranking.split("\t")[1].split(" ")[length_of_context]

print("True next word: ", true_next_word)
print("Predicted next word: ", predicted_next_word)
      



