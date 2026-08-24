# Wardrobe-AI-App
Hello fellow reader, this project is strictly a learning project I created in my summer before starting University using python and Streamlit with generous help from ChatGPT. My initial Idea was to create an app that customizes an outfit with my clothes for any occasion I prompt it to. 


So at first I started to begin familiarizing myself with Streamlit and setting up a simple interface, then I learned how to connect a free database, MongoDB Community Edition, to store image metadata. Afterwards, I connected free cloud storage, Cloudinary, to Streamlit and passed on the image url to MongoDB. My next step in my plan was to add AI models. In the beginning, I was manually entering the metadata by clicking certain tags and I found that pretty annoying so I opted to automate it through AI. I was going to locally run the model but then I realized my Laptop could not handle the computation so I used HuggingFace Inference API instead, I used google/gemma-4-31B-it. 

Looking back, I should have kept the manual inputs of metadata as the model API was not always reliable. Sometimes the requests would not go through or some metadata of the image would be wrong. For example, I had a sage green blouse but the model identified it as grey due to the lighting. So I think a mixture of human and AI input would be good, like the user would provide input on categories that are harder for the AI to identify like 'material', and especially for user specific categories like 'occasion' or 'aesthetic'. 

As for curating an outfit, I wanted to use vector search and embedding models but that was too advanced for me and my hardware right now. I ran into the same problem of running the models locally. but the embedding models did not have an Inference API this time. So I shifted my focus to improving the interface. Specifically, I added delete buttons for each item as before I had to go into both MongoDB and Cloudinary to delete my clothes. 

So my plans are to use what I've learned from this experience and carry them over into other projects or comeback and revamp this one with embedding models once I have more capable hardware, or more simply add keyword search. I could re-create the app with different frameworks like react.js and javascript. And even add different features such as a project I had vibecoded previously to help upcycle clothes. So in this app it could recommend old clothes or very unpopular clothes in the closet and could create an upcycled preview as inspiration for the user. 

Anyways, this is a final look of the interface: <img width="1782" height="1513" alt="image" src="https://github.com/user-attachments/assets/51affbcd-2bd6-4c29-a0f1-26798e233a8a" />

