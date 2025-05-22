# Import required libraries
import pandas as pd
import plotly.graph_objects as go
import dash
from dash import dcc, html
from dash.dependencies import Input, Output


# Create Dash app
app = dash.Dash(__name__)

text_options = [
    {'label': 'Slept without solving', 'value': '1'},
    {'label': 'Fought when u were already sick', 'value': '2'},
    {'label': 'Lost attention', 'value': '3'},
    {'label': 'Burp ka Hindi Vivaad', 'value': '4'},
    {'label': 'The Cheating', 'value': '5'}
]

# App layout
app.layout = html.Div(style={
    'background': 'linear-gradient(to right, #ffe6f0, #e6ccff)',  # pink to lavender gradient
    'minHeight': '100vh',
    'padding': '30px'},children=[
    html.H1(
        '❤️To Win My Cutiee Ka Love Back❤️',
        style={'textAlign': 'center', 'color': 'purple', 'font-size': 40}
    ),

    html.Div([
        "Lets Solve",
        dcc.Dropdown(
            id='Problems',
            options=text_options,
            value="1",
            style={'color': 'purple',
        'backgroundColor': '#ffe6f0',  # soft pink background
        'border': '2px solid #cc66ff',
        'borderRadius': '15px',
        'padding': '10px',
        'font-size': '20px',
        'font-family': "'Comic Sans MS', 'Cursive'",
        'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.2)',
        'textAlign': 'center',
        'marginTop': '10px',
        'height': '60px',}
        ),
    ], style={
        'height': '60px',
        'fontSize': '20px',
        'backgroundColor': 'White',      # ✅ Set background color
        'color': 'black',                # ✅ Text color
        'border': '1px solid #ccc',      # ✅ Border
        'borderRadius': '5px',           # Optional: Rounded corners
        'padding': '10px'}),

    html.Br(), 
    html.Br(),
    html.Br(),

    html.Div(
    id='dropdown-output',
    style={
        'fontSize': '24px',
        'color': '#4b004b',
        'backgroundColor': '#fff0f5',
        'padding': '35px',
        'borderRadius': '20px',
        'border': '2px solid #cc66ff',
        'boxShadow': '0 4px 12px rgba(0, 0, 0, 0.2)',
        'fontFamily': "'Comic Sans MS', 'Comic Neue', 'Cursive'",
        'maxWidth': '80%',
        'margin': 'auto',
        'whiteSpace': 'pre-wrap'
    }
),
    html.Div("Made with all my ❤️ only for you Meri Jaan.", style={
    'textAlign': 'center',
    'marginTop': '50px',
    'fontSize': '18px',
    'color': '#9900cc',
    'fontFamily': "'Brush Script MT', cursive"
})


])

# Callback to update graph
@app.callback(
    Output(component_id='dropdown-output', component_property='children'),
    Input(component_id='Problems', component_property='value')
)
def update_output(option):
    if option=="1":
        return "That day I Slept without solving. I truly acknowledge this grave mistake which has harmed your respect and overall your love for me. I will patiently hear all ur heart out on this without justifying my mistakes and without saying those irritating sorrys. Such a thing will not occur ."
    elif option=="2":
        return "I argued and hurt you the day you were too sick. Not even god shall forgive me for this. Instead of showning presence of mind and patience i brought in my ego and defamed love completely that day. In my worst to worst dream i'll never let ego , impatience and anger come in the path of our beautiful love. First is you .. Then the problem ... Then Me ..  "
    elif option=="3":
        return html.Div([html.P("1. You wanted me to watch and focus on movie but I was continously losing my attention and in turn making you lose your interest . It irritated you immensely and i argued for long . I never understood but i do now that it simply meant huge disrespect of you. The one person who should have heard you and paid attention to your interest and excitement destroyed the moment. I am ready hear all of your thoughts and harsh feeling on this ."),
                         html.P("2. You were saying something and i said something to some worker outside the music room . It was huge disrespect of yours and i still feel extremely guilty for that . I love you So much meri jaan . I wont let it happen ever to you .")])
    elif option=="4":
        return "I used that bad word and argued a lot and even shouted at you like anything. It should have respected what you like and what you dont. I truly acknowledge it."
    elif option=="5":
        return "Defending Shreya Pandey, Chatting with Shreya Pandey. You hate that person and I simply let away what you hated like the most inhuman person. No one can forgive me and i have no words for my rubbish behaviour. Call it immaturity , lack of understanding, lack of knowledge of how things in relationship should work, lack of presence of mind. I am ready to hear all you have to say about it. 1000 slangs are also less for my act . Then i also celebrated her birthday. I know how hurt you would be because of all these. If and only if u can believe me ill never let any such thing happen . I wont let u be hurt at all. You are priority and u will be my biggest priority. Call me if u want to shout on me . Ill not object or defend or argue . I didnt listen then but ill listen everything X 3 this time Pakaa!!."
# Run the app
if __name__ == '__main__':
    app.run(port=8050, debug=True)
