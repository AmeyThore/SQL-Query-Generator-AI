import streamlit as st
import google.generativeai as genai

GOOGLE_API_KEY  = "AIzaSyDDtRnlaVIW53b_X15dHwnWqeeRgOGewRI"

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def main():
    st.set_page_config(page_title ="SQL Query Generator 🤖" ,page_icon=":robot:")
    st.markdown(
        """
                <div style="text-align: center;">
                    <h1>SQL Query Generator 🤖🕵️‍♂️🌐</h1>
                    <h3>I can generate SQL querires for you!</h3>
                    <h4>with explination as well</h4>
                    <p>This tool is a single tool that allows you to generate SQL queries based on your inputs</p>
                </div>


        """,
        unsafe_allow_html= True,
    )
    
    text_input = st.text_area("Enter your Query here in the plain text: ")

    

    submit = st.button(label='Generate SQL Query')

    if submit:
        # response= model.generate_content(text_input)

        # print(response.text)
        # st.write(response.text)
        with st.spinner("Generating sql query..."):
            template=f"""
            
                    Create a SQL query snippet using the below text:

                        ```
                        {text_input}

                        ```
                    I just want SQL query.

                    """
            formatted_template = template.format(text_input=text_input)
            # st.write(formatted_template)
            respomse=model.generate_content(formatted_template)
            sql_query = respomse.text
            #st.write(sql_query)
            
            sql_query = sql_query.strip().lstrip("```sql").rstrip("```")

            expected_output =f"""
                    What would be the expected response of this SQL query snippet:

                        ```
                        {sql_query}

                        ```
                        
                    Provide sample tabular Response with no explination:

                    """
            expected_output_formatted = expected_output.format(sql_query=sql_query)
            e_output=model.generate_content(expected_output_formatted)
            e_output=e_output.text
            #st.write(e_output)

            explination =f"""

                        Explain this SQL query

                        ```
                        {sql_query}

                        ```

                       Provides the simplest explination:

                    """
            explination_formatted= explination.format(sql_query=sql_query)
            explination=model.generate_content(explination_formatted)
            explination = explination.text
            #st.write(explination)

            with st.container():
                st.success("SQL Query Generated Successfully! Here is your Query Below:")
                st.code(sql_query, language="sql")

                st.success("Expectes output of this SQL query will be:")
                st.markdown(e_output)

                st.success("Explination of the above SQL Query:")
                st.markdown(explination)
main()

