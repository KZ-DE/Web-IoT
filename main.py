from utils.header import *

pages = {
    "Login or Sign In": [
        st.Page(page='./page/login.py', title="Login page"),
        st.Page(page='./page/SignIn.py', title="Sign In page"),

    ]
}

st.navigation(pages).run()
