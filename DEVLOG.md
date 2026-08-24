07/04/2026
  Followed Streamlit tutorial (https://youtu.be/KcXag5QRsHg?si=RrRnCRUHIMepr0AE).
  Learned some basic Streamlit functions, looked at streamlit doc for how to make a 
  multi-select bar. It's not perfect but it works.
  Next, Im planning to learn more about Streamlit to eventually create a basic app
  that supports image uploads.

07/06/2026
  I learned how to upload images in Streamlit by myself.
  I attempted to sort the images into different folders on Streamlit which was
  hard(for me) and nobody posted anything about my problem online:( 
  I ended up asking AI how to upload images into different folders - the response
  was to instead create lists instead of folders and using the expander function
  I want to try in the future not relying on AI alot, but Streamlit is a new tool to
  me. I want to get more familiar with streamlit functions before I dive deeper.

07/13/2026
  I forgot to log the previous days--I mainly just was researching some databases
  and free cloud storage software I can add. I ended up on MongoDB because it was
  JSON based which gives more flexibilty if I needed to change or update data
  fields, and JSON is easier to learn than SQL for PostgreSQL databases--this led
  me to learn a little of how to read and write JSON files, tutorial i watched:
  (https://youtu.be/jABj-SEhtBc?si=v95eLzr0YEeeCPox). I felt overwhelmed reading
  MongoDB documentation and it took me a while to set up, but I got it done. My next
  goal is to connect a MongoDB database to streamlit.

07/18/2026
  Checking in, I watched this tutorial (https://youtu.be/H5ucAW9jdkQ?
  si=ic8YD6HvsPmEuG40) on how to connect MongoDB database to
  Streamlit and learned about CRUD (Create, Read, Update, Delete--i think) which are
  ways to handle data. Next I need to learn how to connect a cloud storage to
  actually store the images in - i was thinking of goocle cloud because it has the
  most resources and tuts on how to connect it to streamlit. I didn't end up using
  GCS because I don't have any credit card info so I opted to use Cloudinary free
  because it doesn't ask but there are less resources on how to connect it to streamlit
  so I asked ChatGPT (⊙_⊙;)

07/21/2026
  I combined all that I learned from tutorials and ChatGPT to create a baseline of the 
  application. I can upload photos in streamlit and have it be stored in the cloud and MongoDB. 
  On my own I learned how to add pills(multi-select tags) and limit image
  upload size -- I had to make a config.toml file. Also I didn't know that I could connect my
  files into github, I thought it was just like copy-paste ur code into a doc, 
  so I'm going to do that --still learning 👻. I followed this tutorial to push
  my code to the repo (https://youtu.be/ueQs5pQ8ZMM?si=_AgmyhP7nctcSuww).

07/28/2026 I created the layout of the app and how it is right now and what I want it to do next. So integrating a model from huggingface will be my next step. <img width="4284" height="5712" alt="image" src="https://github.com/user-attachments/assets/4547ecf6-be33-4856-8864-ded8fbcbe7bd" />

08/17/2026 I know I've been slacking a bit lately--I haven't upated the log in a while. I got to implement gemma from huggingface with help from ChatGPT. and afterwards I was keen on implementing an embedding model for semantic search. I researched a little bit about embeddings and vector search but as I was trying to test an embedding model on my laptop-it just wasn't working. My computer was too slow since I don't have a proper GPU to run the model. So now I'm opting to try something more feasible on my hardware--keyword search and filtering.

08/24/2026 So I decided to actually implement delete buttons for each item so I don't have to go to MongoDB and cloudinary directly to delete an item--I did this with help from ChatGPT once again. So now since school is starting I'm going to leave this project at bay for now. If i do come back i might add keyword search, if my hardware is good an embedding model, and if my skills are good create a javascript backend and a react.js front end --or any more 'real' frontend, backend frameworks.
