from shiny import *

app_ui = ui.page_fluid(
    ui.h3("HTTP request headers"),
    ui.output_text_verbatim("headers", placeholder=True),
    ui.h3("User and groups"),
    ui.output_text_verbatim("user_groups", placeholder=True),
)


def server(input: Inputs, output: Outputs, session: Session):
    @output()
    @render_text()
    def headers():
        s = ""
        for key, value in session.http_conn.headers.items():
            s += f"{key}: {value}\n"

        return s

    @output()
    @render_text()
    def user_groups():
        return f"session.user: {session.user}\nsession.groups: {session.groups}"


app = App(app_ui, server)