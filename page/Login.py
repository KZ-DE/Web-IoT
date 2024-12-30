from utils.header import *

try:
    authenticator.login()
except Exception as e:
    st.error(e)
finally:
    st.page_link(page='./page/login.py',
                 label="have a acount ? goes to Login")

if st.session_state['authentication_status']:
    authenticator.logout()
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Some content')
elif st.session_state['authentication_status'] is False:
    st.error('Username/password is incorrect')
elif st.session_state['authentication_status'] is None:
    st.warning('Please enter your username and password')

for items in st.session_state.items():
    st.write(items)

with open('./data/data.yaml', 'w') as file:
    yaml.dump(config, file, default_flow_style=False)
