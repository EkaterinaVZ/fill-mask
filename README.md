# Fill-mask![image](https://user-images.githubusercontent.com/80875367/150012330-38df6b01-bee5-4e6b-8def-a8b7abf28579.png)

___Masked language modeling (bold italic)___
__________
### &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<a href="https://share.streamlit.io/ekaterinavz/fillmask/uber_pickups.py">app on Streamlit</a>&#9989;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<a href="https://fill-mask.herokuapp.com/docs">app on Heroku</a>&#9989;

----

## Example for use in Streamlit and Heroku:

![image](https://user-images.githubusercontent.com/80875367/150005724-29046fa2-8e0f-43f8-b59c-0bc8538e596f.png) 
&emsp;&emsp;&emsp;&emsp;&emsp;![image](https://user-images.githubusercontent.com/80875367/150077365-52318f18-c6cc-416d-b33a-9b105902bea8.png)
```
```
## Example code for Curl:
   curl -X 'POST' \
  'http://127.0.0.1:8000/predict/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "He plays football every [MASK]."
   }'
```
...................................................................................................................................
```
   ## ALBERT Base v2 &#9997;
----
[released of the model at this page](https://huggingface.co/albert-base-v2)
----

   Pretrained model on English language using a masked language modeling (MLM) objective. It was introduced in
   this paper and first released in this repository. This model, as all ALBERT models, is uncased: it does not make a difference between english and English.


   #### Model description
  ALBERT is a transformers model pretrained on a large corpus of English data in a self-supervised fashion.
  Masked language modeling (MLM): taking a sentence, the model randomly masks 15% of the words in the input then run the entire masked sentence through the 
  model and has to       predict the masked words. This is different from traditional recurrent neural networks (RNNs) that usually see the words one after 
  the other, or from autoregressive models       like GPT which internally mask the future tokens. It allows the model to learn a bidirectional representation
  of the sentence.
  Sentence Ordering Prediction (SOP): ALBERT uses a pretraining loss based on predicting the ordering of two consecutive segments of text.
  This way, the model learns an inner representation of the English language that can then be used to extract features useful for downstream tasks: 
  if you have a dataset of labeled sentences for instance, you can train a standard classifier using the features produced by the ALBERT model as inputs.
```
This model has the following configuration:
```
__________________________________________________________________________________________________________________________________
	* 12 repeating layers
	* 128 embedding dimension
	* 768 hidden dimension
	* 12 attention heads
	* 11M parameters


[![Python application](https://github.com/EkaterinaVZ/fill-mask/actions/workflows/python-app.yml/badge.svg)](https://github.com/EkaterinaVZ/fill-mask/actions/workflows/python-app.yml)
