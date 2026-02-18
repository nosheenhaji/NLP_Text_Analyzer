import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
from nltk.stem import PorterStemmer
ps = PorterStemmer()
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()
import spacy
nlp = spacy.load("en_core_web_sm")
from spacy import displacy
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
st.title("A Comprehensive NLP Text Analyzer")
st.header("Paste your text or upload a file. Select your analysis type and watch as our tool deconstructs and visualizes your data exactly how you want it ")
st.sidebar.header("Pick your preferred NLP task from the list below and click to process your text")
select=st.sidebar.selectbox('Choose Any One',('Word_Tokenizer','Sentence_Tokenizer','Word_Counter','Remove_StopWords','Porter_Stemmer','Lemmatization','Named_Entity_Recognition(NER)'))
choose=st.sidebar.selectbox('Choose Action',['Text Input','File Upload'])
if select == 'Word_Tokenizer':
    if choose == 'Text Input':
        input_text_1= st.text_input('Paste your Text:')
        tokens = word_tokenize(input_text_1)
        st.write(tokens)
    elif choose == 'File Upload':
        file_uploader_1=st.file_uploader('Upload A Text File',type=['txt'])
        if file_uploader_1 is not None:
            string_dat=file_uploader_1.read().decode('utf-8')
            if st.button('Process File'):
                file_process = word_tokenize(string_dat)
                result_tex = " ".join(file_process)
                st.text_area("Processed Text", result_tex, height=150)
                st.download_button(
                label="Download Processed File",
                data=result_tex,
                file_name="Word_Tokenize.txt",
                mime="text/plain",
            )
elif select == 'Sentence_Tokenizer':
    if choose == 'Text Input':
        input_text_2= st.text_input('Paste your Text:')
        sent_tokens = sent_tokenize(input_text_2)
        st.write(sent_tokens)
    elif choose == 'File Upload':
        file_uploader_2=st.file_uploader('Upload A Text File',type=['txt'])
        if file_uploader_2 is not None:
            strin_data=file_uploader_2.read().decode('utf-8')
            if st.button('Process File'):
                file_process = sent_tokenize(strin_data)
                reult_text = " ".join(file_process)
                st.text_area("Processed Text", reult_text, height=150)
                st.download_button(
                label="Download Processed File",
                data=reult_text,
                file_name="Sentence_Tokenize.txt",
                mime="text/plain",
            )
elif select =='Word_Counter':
    if choose == 'Text Input':
        token_1= st.text_input('Paste your Text:')
        count_tokens = len(token_1.split())
        st.write(count_tokens)
    elif choose == 'File Upload':
        file_uploaer_3=st.file_uploader('Upload A Text File',type=['txt'])
        if file_uploaer_3 is not None:
            string_data=file_uploaer_3.read().decode('utf-8')
            if st.button('Process File'):
                fil_process = len(string_data.split())
                file_process_1=str(fil_process)
                reslt_text = " ".join(file_process_1)
                st.text_area("Processed Text", reslt_text, height=150)
                st.download_button(
                label="Download Processed File",
                data=reslt_text,
                file_name="count_Tokenize_words.txt",
                mime="text/plain",
            )
elif select == 'Remove_StopWords':
    if choose == 'Text Input':
        input_text_4= st.text_area('Paste your Text:')
        if input_text_4:
            word_tokens = word_tokenize(input_text_4)
            remove_stopwords = [w for w in word_tokens if w.lower() not in stop_words ]
            st.write (remove_stopwords)
    elif choose == 'File Upload':
        file_uploader_5=st.file_uploader('Upload A Text File',type=['txt'])
        if file_uploader_5 is not None:
            string_data=file_uploader_5.read().decode('utf-8')
            if st.button('Process File'):
                toke=word_tokenize(string_data)
                file_process = [w for w in toke if w.lower() if w not in stop_words]
                result_text = " ".join(file_process)
                st.text_area("Processed Text", result_text, height=150)
                st.download_button(
                label="Download Processed File",
                data=result_text,
                file_name="Remove_StopWords.txt",
                mime="text/plain",
            )
elif select == 'Porter_Stemmer':
    if choose == 'Text Input':
        input_Text_6= st.text_area('Paste your Text:')
        Port_stemm = [ps.stem(w) for w in input_Text_6.split()]
        st.write(Port_stemm)
    elif choose == 'File Upload':
        file_uplader_6=st.file_uploader('Upload A Text File',type=['txt'])
        if file_uplader_6 is not None:
            strig_data=file_uplader_6.read().decode('utf-8')
            if st.button('Process File'):
                file_procss = [ps.stem(w) for w in strig_data.split()]
                rsult_text = " ".join(file_procss)
                st.text_area("Processed Text", rsult_text, height=150)
                st.download_button(
                label="Download Processed File",
                data=rsult_text,
                file_name="porter_Stemmer.txt",
                mime="text/plain",
            )
elif select == 'Lemmatization':
    if choose == 'Text Input':
        inputtext_7= st.text_area('Paste your Text:')
        tags=st.selectbox('Select any One',['','v','n','a','r'])
        st.header("Explain:")
        st.write("v --->  Verb")
        st.write("n --->  Noun")
        st.write("a --->  Adjective")
        st.write("r --->  Adverb")
        if st.button('Process'):
            words = inputtext_7.split()  
            lemmatized_words = [lemmatizer.lemmatize(word, pos=tags) for word in words]
            st.write("Lemmatized Text:")
            st.write(" ".join(lemmatized_words))
elif select == 'Named_Entity_Recognition(NER)':
    if choose == 'Text Input':
        inpt_text_9= st.text_input('Paste your Text:')
        if inpt_text_9:
            doc=nlp(inpt_text_9)
            entities=[(ent.text,ent.label_) for ent in doc.ents]
            html = displacy.render(doc, style="ent")
            st.markdown(html, unsafe_allow_html=True)
            st.write("Named_Entity_Recognition_(NER)")
            st.write(entities)
    elif choose == 'File Upload':
        file_uloader_9=st.file_uploader('Upload A Text File',type=['txt'])
        if file_uloader_9 is not None:
            strig_data=file_uloader_9.read().decode('utf-8')
            if st.button('Process File'):
                doc =nlp(strig_data)
                entitie=[(ent.text,ent.label_) for ent in doc.ents]
                result_text = "\n".join([f"{text} → {label}" for text, label in entitie])
                st.text_area("Processed Text", result_text, height=150)
                st.download_button(
                label="Download Processed File",
                data=result_text,
                file_name="Named_Entity_Recognition(NER).txt",
                mime="text/plain",
            )