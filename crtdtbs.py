import sqlite3

# Veritabanına bağlanın veya oluşturun
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# 'machines' tablosunu oluşturun (Eğer tablo zaten varsa bu adımı atlayabilirsiniz)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS services (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company_name TEXT,
        telephone TEXT,
        task TEXT,
        responsible TEXT,
        power_source TEXT,
        machine_model_no TEXT,
        nesting TEXT,
        userIssues TEXT,
        determination TEXT,
        transactions TEXT,
        result TEXT,
        partname TEXT,
        quantily TEXT,
        report TEXT,
        warranty_status TEXT,
        error_source TEXT,
        service_start_time TEXT,
        service_end_time TEXT,
        total_service_time TEXT,
        service_officer_signature TEXT,
        company_responsible TEXT    
    )
''')

# Değişiklikleri kaydedin ve bağlantıyı kapatın
conn.commit()
conn.close()
