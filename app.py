from flask import Flask, json, request
import sqlite3

app = Flask(__name__)
app.config["DEBUG"] = True
application = app

@app.route('/players/resetallplease', methods=['POST'])
def reset_players():
    success = False

    if request.method == 'POST':
        try:
            with sqlite3.connect("database.db") as con:
                cur = con.cursor()

                cur.execute("DELETE FROM players")
                con.commit()

                success = True
        except:
            con.rollback()
            success = False

        finally:
            return json.dumps({'success': success})
            con.close()

@app.route('/players/all', methods=['GET'])
def get_players():
    players = []

    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM players")

    rows = cur.fetchall()

    for row in rows:
        players.append({'name': row['name'], 'level': row['level']})

    return json.dumps(players)

@app.route('/players/get', methods=['GET'])
def get_players_level():
    players = []

    try:
        name = request.args.get('name')

        with sqlite3.connect("database.db") as con:
            con.row_factory = sqlite3.Row

            cur = con.cursor()
            cur.execute("SELECT * FROM players WHERE name='" + name + "'")

            rows = cur.fetchall()

            for row in rows:
                players.append({'name': row['name'], 'level': row['level']})

            return json.dumps(players)
    except:
        return "There was an Error"

@app.route('/players/add', methods=['POST'])
def post_players():
    success = False

    if request.method == 'POST':
        try:
            name = request.args.get('name')
            level = int(request.args.get('level'))

            with sqlite3.connect("database.db") as con:
                cur = con.cursor()

                cur.execute("INSERT INTO players (name, level) VALUES (?,?)", (name, level))
                con.commit()

                success = True
        except:
            con.rollback()
            success = False

        finally:
            return json.dumps({'success': success})
            con.close()


@app.route('/players/delete', methods=['POST'])
def delete_players():
    success = False

    if request.method == 'POST':
        try:
            name = request.args.get('name')
            level = int(request.args.get('level'))

            with sqlite3.connect("database.db") as con:
                cur = con.cursor()

                cur.execute("DELETE FROM players WHERE name ='" + name + "'")
                con.commit()

                success = True
        except:
            con.rollback()
            success = False

        finally:
            return json.dumps({'success': success})
            con.close()

@app.route('/players/update', methods=['POST'])
def update_players():
    success = False

    if request.method == 'POST':
        try:
            name = request.args.get('name')
            level = int(request.args.get('level'))

            with sqlite3.connect("database.db") as con:
                cur = con.cursor()

                cur.execute('UPDATE players SET "level"=? WHERE name=?', (int(level), name))
                con.commit()

                success = True
        except:
            con.rollback()
            success = False

        finally:
            return json.dumps({'success': success})
            con.close()


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>What the feck are you doing?<br>There's nothing to see there.</p>", 404

if __name__ == '__main__':

    app.run()