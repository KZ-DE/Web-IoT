from utils.header import *

try:
    email, username, name = authenticator.register_user(
        pre_authorized=config['pre-authorized']['emails'], captcha=False)
    if email:
        st.success('User registered successfully')
except Exception as e:
    st.error(e)
finally:
    st.page_link(page='./page/login.py',
                 label="have a acount ? goes to Login")

for items in st.session_state.items():
    st.write(items)

with open('./data/data.yaml', 'w') as file:
    yaml.dump(config, file, default_flow_style=False)
