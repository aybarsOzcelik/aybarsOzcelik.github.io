from flask import Flask, render_template, jsonify, request, redirect
import sqlite3

app = Flask(__name__)


@app.route('/get_all_services')
def get_all_services():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    all_services = cursor.execute(
        "SELECT * FROM services"
    ).fetchall()
    conn.close()

    return jsonify({'all_services': all_services})


@app.route('/get_plasma_machines')
def get_plasma_machines():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    plasma_machines = cursor.execute(
        "SELECT * FROM allMachines WHERE machine_type = 'plasma'").fetchall()

    conn.close()

    return jsonify({'plasma_machines': plasma_machines})


@app.route('/get_laser_machines')
def get_laser_machines():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    laser_machines = cursor.execute(
        "SELECT * FROM allMachines WHERE machine_type = 'laser'").fetchall()

    conn.close()

    return jsonify({'laser_machines': laser_machines})


@app.route('/newMachine')
def newMachine():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    machine_types = cursor.execute(
        "SELECT DISTINCT machine_type FROM machines").fetchall()
    machine_models = cursor.execute(
        "SELECT DISTINCT machine_model FROM machines").fetchall()

    conn.close()

    return render_template('newMachine.html', machine_types=machine_types, machine_models=machine_models)


@app.route('/services')
def services():
    return render_template('services.html')


@app.route('/service')
def service():
    return render_template('service.html')


@app.route('/get_data')
def get_data():
    # Veritabanına bağlanın, "data.db" kısmını projenize uygun şekilde güncelleyin
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    # Plazma tablosundan verileri çek
    plasma_data = cursor.execute("SELECT * FROM plasma").fetchall()

    # Lazer tablosundan verileri çek
    laser_data = cursor.execute("SELECT * FROM laser").fetchall()

    conn.close()

    return jsonify({'plasma': plasma_data, 'laser': laser_data})


@app.route('/add_machine', methods=['POST'])
def add_machine():
    if request.method == 'POST':
        company_name = request.form['companyName']
        machine_type = request.form['machineType']
        choisen_model = request.form['choisen_model']
        dimensions = request.form['dimensions']
        nesting = request.form['nesting']
        powerUnit = request.form['powerUnit']
        powerUnitSerial = request.form['powerUnitSerial']
        headModel = request.form['headModel']
        headSerialNumb = request.form['headSerialNumb']
        startDate = request.form['startDate']
        endDate = request.form['endDate']
        remainingWarranty = request.form['remainingWarranty']

        # Diğer form verilerini alın

        # Veritabanına bağlanın ve form verilerini kaydedin
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO allMachines (company_name, machine_type, machine_model_no,dimensions,nesting,powerUnit,powerUnitSerial, headModel, headSerialNumb, startDate, endDate, remainingWarranty) VALUES (?,?,?,?,?, ?, ?, ?, ?, ?,?,?)",
                       (company_name, machine_type, choisen_model, dimensions, nesting, powerUnit, powerUnitSerial, headModel, headSerialNumb, startDate, endDate, remainingWarranty))
        # Diğer verileri de ilgili sütunlara kaydedin

        conn.commit()
        conn.close()

        return render_template('index.html', success_message="Yeni makine başarıyla eklenmiştir.")


@app.route('/')
def index():
    # Veritabanına bağlanın ve makine türlerini çekin
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    machine_types = cursor.execute(
        "SELECT DISTINCT machine_type FROM machines").fetchall()

    conn.close()

    return render_template('index.html', machine_types=machine_types)


@app.route('/get_machine_models/<machine_type>')
def get_machine_models(machine_type):
    # Veritabanına bağlanın ve seçilen makine türüne ait modelleri çekin
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    machine_models = cursor.execute(
        "SELECT DISTINCT machine_model FROM machines WHERE machine_type=?", (machine_type,)).fetchall()

    conn.close()

    return jsonify({'models': [model[0] for model in machine_models]})


if __name__ == '__main__':
    app.run(debug=True)
