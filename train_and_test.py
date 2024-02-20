import pymitlm

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

import numpy as np

w = 5
padding = w * 2

''' create the corpus file '''
'''

with open("data/train_data_subset.txt", "r") as f:
      lines = f.readlines()
      for line in lines:
        line = line.strip()
        train_data = "<s> " * padding + line + " </s>" * padding

        # write data to a file called testcorpus
        with open("testcorpus_subset", "a") as f:
              f.write(train_data+"\n")

'''


def evaluate_modified_mitlm_model(model):
      y_true = []
      y_pred = []
      
      with open("data/test_data_subset.txt", "r", encoding="utf8") as f:
            lines = f.readlines()
            
            for line in lines:

                  line = line.strip()
                  line = "<s> " * padding + line
                  sentence_tokens = line.split(" ")
                  
                  context = ' '.join(sentence_tokens[:-1])  # Use all words except the last one as context
                  length_of_context = len(sentence_tokens) - 1
                  
                  true_next_word = sentence_tokens[-1]
                  
                  highest_ranking = model.predict(context).split("\n")[0]

                  # bug
                  if highest_ranking == "":
                        continue
                  predicted_next_word = highest_ranking.split("\t")[1].split(" ")[length_of_context]
                  
                  y_true.append(true_next_word)
                  y_pred.append(predicted_next_word)
            
            print("y_true: ", len(y_true))
            print("y_pred: ", len(y_pred))
                  
                  

      accuracy = accuracy_score(y_true, y_pred)
      precision = precision_score(y_true, y_pred, average='weighted', zero_division=np.nan)
      recall = recall_score(y_true, y_pred, average='weighted', zero_division=np.nan)
      f1 = f1_score(y_true, y_pred, average='weighted', zero_division=np.nan)

      return accuracy, precision, recall, f1

orders = [2, 3, 4, 6, 8, 10, 15]
accuracies = []
precisions = []
recalls = []
f1s = []

for order in orders:
      m = pymitlm.PyMitlm("testcorpus_subset", order, "ModKN", True)
      accuracy, precision, recall, f1 = evaluate_modified_mitlm_model(m)
      accuracies.append(accuracy)
      precisions.append(precision)
      recalls.append(recall)
      f1s.append(f1)

print("Accuracy: ", accuracies)
print("Precision: ", precisions)
print("Recall: ", recalls)
print("F1: ", f1s)
      



