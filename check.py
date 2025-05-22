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
    {'label': 'Burp in Hindi Tragedy', 'value': '4'},
    {'label': 'The Cheating', 'value': '5'},
    {'label':'MOOD-I Tragedy','value':'6'},
    {'label':'Conclusion','value':'7'}
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
    elif option=="6":
        return "Remember in MOOD I you said 'Ill even Hug Arpit' . My jealousy , and rage took over my brain and I used the name of Shreya Pandey to make u feel jealous. Such a shameful act from my end. I literally went to justify my action , increasing your rage to infinity. I am so so sorry for that kind of behaviour. Please shout your heart out if anything is sustained in your heart. I promise to hear you out calmy and with maturity meri jaan." 
    elif option=="7":
        return html.Div([html.H1("Meri Jaan"),html.P("Lafzon mei kaid pyaar bas hai kiya, Dil mei sanjo ke kuch khaas tha rakha, safar ke sapne the motiyon se sajile, hatane the kaante par khud ban gaya ",html.Br(),"I wont let any of those prick you . Not even I will unintentionally or intentionally become one of those thorns. I really love you from the bottom of my heart and will definitely prove it . You are the only person i Trust blindly on , infront of whom i love to be natural , love to be me. But in the race to achieve peace i just focused on mine . I am really guilty of making you feel so worthless . You are the most precious person and i can engrave it on my arms. Please be by my side and please thoda sa bharosa karlena if possible. Ill give my 200% to this relationship and we will make it together the most beautiful one. We will bring back the love , smile and respect .",html.Br(),"Meri Jaan , There was no one above you , There is no one above you , There will be no one ever above you")])
# Run the app
import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8050))
    app.run(host='0.0.0.0', port=port, debug=True)

