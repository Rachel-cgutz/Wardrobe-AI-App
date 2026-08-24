import streamlit as st
import cloudinary_config
import cloudinary.uploader
from database import get_database
from models.vision import get_metadata

st.title('Lily\'s Closet (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ ')
st.subheader('A personalized digital closet ready for any occasion.🌟')

#Set up sessionstate to avoid calling API multiple times
if 'image_url' not in st.session_state:
    st.session_state.image_url = None
if 'metadata' not in st.session_state:
    st.session_state.metadata = None
if 'delete_id' not in st.session_state:
    st.session_state.delete_id = None

#Connect to database
db = get_database()
collection = db['clothes']

#Image uploader
uploaded_file = st.file_uploader(
    'Upload clothing images', type=['jpg','png','jpeg'])

category = st.selectbox(
    'Select category to upload:', ['Tops', 'Bottoms']
)


# #Select tags to describe clothes
# options = ['Summer', 'Winter', 'Fall', 'Formal', 'Casual', 'Colorful', 'Plain']
# descriptions = st.pills('Descibe your outfit', options, selection_mode='multi')
# st.markdown(f'You selected:{descriptions}')

if uploaded_file and st.session_state.image_url is None:

#Upload to Cloudinary storage ONCE
    cloud_result = cloudinary.uploader.upload(uploaded_file)

    st.session_state.image_url = cloud_result['secure_url'] #url to view image in st
    st.session_state.public_id = cloud_result['public_id'] #url to find image in cloud

    #Send to vision model
    st.session_state.metadata = get_metadata(st.session_state.image_url)
    
    if st.session_state.metadata is None:
        st.error('AI unavailable. Please try again later.')
        cloudinary.uploader.destroy(st.session_state.public_id)

        st.session_state.image_url = None
        st.session_state.public_id = None
        st.session_state.metadata = None

#Save to MongoDB
#Add insert button and show preview
if (st.session_state.image_url and st.session_state.metadata is not None):

    st.image(st.session_state.image_url, width=300)

    if st.button('Add Item'):

        clothing_item = {
            'category': category,
            'image_url': st.session_state.image_url,
            'public_id': st.session_state.public_id,
            'metadata': st.session_state.metadata
        }
        mongo_result = collection.insert_one(clothing_item)

        if mongo_result.inserted_id:
            st.success('Saved to Closet')

            #Clear temporary data
            st.session_state.image_url = None
            st.session_state.public_id = None
            st.session_state.metadata = None

            st.rerun()

        else: 
            st.warning('Error Ocurred. Item not added.')

#display images in expander
categories = ['Tops', 'Bottoms']
for category in categories:

    items = collection.find({'category': category})

    with st.expander(category.title()):
        cols = st.columns(4)

        for i, item in enumerate(items):
            with cols[i % 4]:
                
                st.image(item['image_url'])
                
                #Delete button
                if st.button('Delete', key=f"delete_{category}_{item['_id']}"):  #Unique keys for each clothing item to distinguish delete buttons
                    
                    st.session_state.delete_id = item['_id']
                    st.rerun()

#Delete confirmation
if st.session_state.delete_id is not None:

    item = collection.find_one({
        '_id': st.session_state.delete_id
    })

    if item:
        st.warning('Are you sure you want to delete this item?')

        col1, col2 = st.columns(2)

        with col1:
            if st.button("Yes", key="confirm_delete"):

                cloudinary.uploader.destroy(
                    item['public_id']
                )

                result = collection.delete_one({
                    '_id': st.session_state.delete_id
                })

                if result.deleted_count == 1:
                    st.session_state.delete_id = None
                    st.success("Item deleted!")
                    st.rerun()

        with col2:
            if st.button("Cancel", key="cancel_delete"):

                st.session_state.delete_id = None
                st.rerun()







