from flask import Flask, request, render_template_string
import wikipedia

app = Flask(__name__)

@app.route('/')
def index():
    """Render the search form."""
    return '''
    <h1>Wikipedia Search</h1>
    <form action="/search" method="post">
        <label for="query">Enter a search term:</label>
        <input type="text" id="query" name="query">
        <button type="submit">Search</button>
    </form>
    '''

@app.route('/search', methods=['POST'])
def search():
    """Handle Wikipedia search."""
    query = request.form.get('query', '')
    if not query:
        return '<h1>Please enter a search term.</h1>'
    try:
        page = wikipedia.page(query, autosuggest=False)
        return f'''
        <h1>{page.title}</h1>
        <p>{page.summary[:500]}...</p>
        <a href="{page.url}" target="_blank">Read more on Wikipedia</a>
        '''
    except wikipedia.DisambiguationError as e:
        options = ''.join(f'<li>{option}</li>' for option in e.options)
        return f'''
        <h1>Disambiguation required</h1>
        <p>Your query matched multiple results. Please try one of the following:</p>
        <ul>{options}</ul>
        '''
    except wikipedia.PageError:
        return '<h1>No matching page found. Try another search term.</h1>'

if __name__ == '__main__':
    app.run(debug=True)
