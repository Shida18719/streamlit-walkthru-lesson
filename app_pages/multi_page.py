import streamlit as st

class MultiPage:

    def __init__(self, app_name) -> None:
        self.pages = []
        self.app_name = app_name

        st.set_page_config(
            page_title = self.app_name,
            page_icon = "🖥️"
        )

    def app_page(self, title, func) -> None:
        """
        Create a class method use to add pages to the object,
        it takes the args of title and func
        and annotate it to say the output is none
        """
        self.pages.append({"title": title, "function": func})

    def run(self):
        """
        Method to run. Create a title on each page which is the app_name
        and add menu to the pages
        """
        st.title(self.app_name)
        page = st.sidebar.radio('Menu', self.pages, format_func=lambda page: page['title'])
        page['function']()
