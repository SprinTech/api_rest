import datetime

import streamlit as st

st.title('Personal diary API')

# Create sidebar element
user = st.sidebar.selectbox("Select type of user", ['Coach', 'Client', 'Sentiment analysis'])

# ------ ADD COACH ACTIONS -------- #
if user == 'Coach':
    coach_action = st.sidebar.selectbox("What do you want to do ?",
                                        ['Add new client', 'Delete client', 'Update client information',
                                         'Get client information', 'Get list of clients'])

    # Add new client to database
    if coach_action == 'Add new client':
        st.markdown('------')
        st.subheader('Add user form')

        # Create form to add client information
        with st.form(key='add_client_form'):
            first_name = st.text_input(label='First name')
            last_name = st.text_input(label='Last name')
            mail = st.text_input(label='Mail')
            phone = st.text_input(label='Phone')
            submit_button = st.form_submit_button(label='Submit')

            if submit_button:
                st.write(f'Client {last_name} {first_name} has been successfully added to database !')

    # Delete client from database
    if coach_action == 'Delete client':
        st.markdown('------')
        st.write('Which client do you want to remove ?')
        user_id = st.number_input(label="User ID", min_value=1, step=1)

        if user_id:
            st.write(f"User {user_id} has been successfully removed from database !")

    # Update client information
    if coach_action == 'Update client information':
        st.markdown('------')
        st.subheader('Update client information form')

        user_id = st.number_input(label="User ID", min_value=1, step=1)

        if user_id:
            with st.form(key='update_client_form'):
                first_name = st.text_input(label='First name')
                last_name = st.text_input(label='Last name')
                mail = st.text_input(label='Mail')
                phone = st.text_input(label='Phone')
                submit_button = st.form_submit_button(label='Submit')

                if submit_button:
                    st.write(f'Information about client {last_name} {first_name} has been successfully updated !')

    # Display information about clients
    if coach_action == 'Get list of clients':
        st.markdown('------')
        pass

    # Get list of client
    if coach_action == 'Get client information':
        st.markdown('------')
        user_id = st.number_input(label="User ID", min_value=1, step=1)

# ------ ADD CLIENT ACTIONS ------ #
if user == 'Client':
    client_action = st.sidebar.selectbox("What do you want to do ?",
                                         ['Add new post', 'Update today post', 'Read posts'])

    # Add new post to database
    if client_action == 'Add new post':
        st.markdown('------')
        st.subheader('How do you feel today ? Write all you are thinking about !')

        user_text = st.text_input(label='Your message')

        if user_text:
            st.write('You message has been successfully registered. See you tomorrow ! :)')

    # Update old post
    if client_action == 'Update today post':
        st.markdown('------')
        st.subheader('Which message do you want to update ?')

        pass

    # Read all post that have been written
    if client_action == 'Read posts':
        st.markdown('------')
        st.subheader('Which message do you want to check ?')

        start_date = st.date_input('Start date', datetime.date.today())
        end_date = st.date_input('End date', datetime.date.today())

        pass

# ------ ADD SENTIMENT ANALYSIS PLOT ------ #
if user == 'Sentiment analysis':
    sentiment_analysis_action = st.sidebar.selectbox("Which wheel of emotion do you want to check",
                                                     ['Global wheel of emotion', 'Individual wheel of emotion'])

    # Check global wheel of emotion
    if sentiment_analysis_action == 'Global wheel of emotion':
        st.markdown('------')
        pass

    # Check global wheel of emotion
    if sentiment_analysis_action == 'Individual wheel of emotion':
        st.markdown('------')
        st.write('From which user do you want to check wheel of emotion ?')

        user_id = st.number_input(label="User ID", min_value=1, step=1)

        if user_id:
            pass
